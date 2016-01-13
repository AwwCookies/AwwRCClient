import sys
import socket
import time
import json

from collections import defaultdict

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui import ui_main
from ui import ui_connect


class Channel:
    def __init__(self, network, name, topic="", messages="", users=[]):
        self.network = network
        self.name = name
        self.topic = "Hello, World!"
        self.message_buffer = messages
        self.users = users

    def set_topic(self, text):
        self.topic = text

    def add_message(self, text):
        self.message_buffer += text

    def on_join(self, nick, ip):
        self.add_message("<p>%s (%s) join %s</p>" % (nick, ip, self.name))

    def on_message(self, nick, ip, message):
        self.add_message("<p>%s: %s</p>" % (nick, message))

    def add_user(self, user):
        pass

    def remove_user(self, user):
        pass

    def text(self):
        return self.message_buffer


class ConnectDialog(QDialog, ui_connect.Ui_Dialog):
    def __init__(self, parent=None):
        super(ConnectDialog, self).__init__(parent)
        self.setupUi(self)


class AwwRCClient(QThread):
    def __init__(self, name, address, port, nick):
        super(AwwRCClient, self).__init__()
        self.name = name
        try:
            self.sock = socket.socket()
            self.sock.connect((address, port))
            self.connected = True
        except:
            self.connected = False

    def run(self):
        if self.connected:
            while True:
                data = self.sock.recv(1024)
                if data.split("\n")[0].startswith("{"):
                    print(data)
                    try:
                        d = json.loads(data)
                    except:
                        d = {"type": "error"}
                    self.emit(SIGNAL("message"), self, d)
                else:
                    break
                data = None


class Client(QMainWindow, ui_main.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Client, self).__init__(parent)
        self.setupUi(self)
        self.clients = {}
        self.current_view = {
            "network": None,
            "channel": None,
            "client": None,
        }
        self.line_command_hist = []
        self.channel_views = {}
        self.channel_buffers = defaultdict(dict)
        self.connect(self.line_command, SIGNAL("returnPressed()"), self.command)
        self.connect_to_server("AwwRC", "192.168.123.123", 5050, start=True)

    def get_channel(self, network, channel):
        self.create_channel_view(network, channel)
        return self.channel_buffers[network][channel]

    def command(self):
        text = str(self.sender().text())
        self.line_command_hist.append(text)
        if text.startswith("/"):
            if text.startswith("/join"):
                if len(text.split()) == 2:
                    self.current_view["client"].sock.send("chanjoin %s" % text.split()[1])
                elif len(text.split()) == 3:
                    self.current_view["client"].sock.send("chanjoin %s %s" % (text.split()[1], text.split()[2]))
            else:
                self.current_view["client"].sock.send(text.replace("/", "", 1))
        else:
            if self.current_view["channel"]:
                self.current_view["client"].sock.send("chanmsg %s %s" % (self.current_view["channel"], text))
                self.line_command.clear()

    def on_message(self, c, data):
        if data["type"] == "CHANMSG":
            self.on_channel_message(c.name, data["channel"], data["message"], data["nick"], data["ip"])
        elif data["type"] == "CHANJOIN" or data["type"] == "YOUJOIN":
            self.on_channel_join(c.name, data["channel"], data["nick"], data["ip"])
        elif data["type"] == "CHANTOPIC":
            self.on_channel_topic(c.name, data["channel"], data["topic"])
        else:
            self.append_text(c.name, "~status", str(data))

    def on_channel_join(self, network, channel, nick, ip):
        self.get_channel(network, channel).on_join(nick, ip)

    def on_channel_message(self, network, channel, message, nick, ip):
        self.get_channel(network, channel).on_message(nick, ip, message)
        if self.current_view["channel"] == channel:
            self.text_browser.setText(self.get_channel(network, channel).text())

    def on_channel_topic(self, network, channel, topic):
        self.get_channel(network, channel).set_topic(topic)

    def append_text(self, network, channel, text, autoscroll=True):
        self.create_channel_view(network, channel)
        self.channel_buffers[network][channel].add_message(text)
        if autoscroll:
            sb = self.text_browser.verticalScrollBar()
            sb.setValue(sb.maximum())
        return self.channel_buffers[network][channel].text()

    def connect_to_server(self, network_name=None, address=None, port=None, dialog=False, start=False):
        if dialog:
            con_dlg = ConnectDialog()
            if con_dlg.exec_():
                network_name = str(con_dlg.line_something.text())
                address = str(con_dlg.line_address.text())
                port = int(con_dlg.spinbox_port.value())
                nick = str(con_dlg.line_nick.text())
                _client = AwwRCClient(network_name, address, port, nick)
                self.clients[network_name] = _client
                self.switch_current_view(network_name, channel_name=None, client=self.clients[network_name])
                self.connect(self.clients[network_name], SIGNAL("message"), self.on_message)
                if start:
                    self.clients[network_name].start()
                return self.clients[network_name]
        elif all([address, port, network_name]):
            _client = AwwRCClient(network_name, address, port, network_name)
            self.clients[network_name] = _client
            self.switch_current_view(network_name, channel_name=None, client=self.clients[network_name])
            self.connect(self.clients[network_name], SIGNAL("message"), self.on_message)
            self.create_channel_view(network_name, "~status")
            if start:
                self.clients[network_name].start()
            return self.clients[network_name]
        else:
            pass

    def create_channel_view(self, network_name, channel_name, r=False):
        chan_names = [self.channel_buffers[network_name][x].name for x in self.channel_buffers[network_name]]
        print chan_names

        if channel_name in chan_names and not r:
            pass
        else:
            if network_name in self.channel_views:
                channel = QTreeWidgetItem()
                channel.setText(0, channel_name)
                self.channel_views[network_name].addChild(channel)
                self.channel_buffers[network_name][channel_name] = Channel(network_name, channel_name)
            else:
                network = QTreeWidgetItem()
                network.setText(0, network_name)
                self.channel_views[network_name] = network
                self.tree_networks.addTopLevelItem(network)
                self.channel_buffers[network_name][network_name] = Channel(network_name, "~status")
                self.connect(self.tree_networks, SIGNAL("itemClicked(QTreeWidgetItem*, int)"), self.on_tree_clicked)
                self.create_channel_view(network_name, channel_name, r=True)

    def on_tree_clicked(self, item, col):
        parent = item.parent()
        if parent:
            self.switch_buffer(str(parent.text(col)), str(item.text(col)))
        else:
            self.switch_buffer(str(item.text(col)), str(item.text(col)))

    def switch_buffer(self, network_name, channel_name):
        if network_name in self.channel_buffers:
            if channel_name in self.channel_buffers[network_name]:
                print("switched views")
                print(self.channel_buffers[network_name][channel_name])
                self.text_browser.setText(self.channel_buffers[network_name][channel_name].text())
                self.line_topic.setText(self.get_channel(network_name, channel_name).topic)
                self.switch_current_view(network_name, channel_name, self.clients[network_name])

    def switch_current_view(self, network_name, channel_name, client=None):
        self.current_view = {
            "network": network_name,
            "channel": channel_name,
            "client": client
        }


app = QApplication(sys.argv)
client = Client()
client.show()
app.exec_()