# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1056, 540)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.line_topic = QtGui.QLineEdit(self.centralwidget)
        self.line_topic.setText(_fromUtf8(""))
        self.line_topic.setObjectName(_fromUtf8("line_topic"))
        self.verticalLayout.addWidget(self.line_topic)
        self.text_browser = QtGui.QTextBrowser(self.centralwidget)
        self.text_browser.setObjectName(_fromUtf8("text_browser"))
        self.verticalLayout.addWidget(self.text_browser)
        self.line_command = QtGui.QLineEdit(self.centralwidget)
        self.line_command.setObjectName(_fromUtf8("line_command"))
        self.verticalLayout.addWidget(self.line_command)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dock_net_chan = QtGui.QDockWidget(MainWindow)
        self.dock_net_chan.setObjectName(_fromUtf8("dock_net_chan"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tree_networks = QtGui.QTreeWidget(self.dockWidgetContents)
        self.tree_networks.setObjectName(_fromUtf8("tree_networks"))
        self.gridLayout_2.addWidget(self.tree_networks, 1, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_servers_count = QtGui.QLabel(self.dockWidgetContents)
        self.label_servers_count.setObjectName(_fromUtf8("label_servers_count"))
        self.horizontalLayout.addWidget(self.label_servers_count)
        self.label_channels_count = QtGui.QLabel(self.dockWidgetContents)
        self.label_channels_count.setObjectName(_fromUtf8("label_channels_count"))
        self.horizontalLayout.addWidget(self.label_channels_count)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.dock_net_chan.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock_net_chan)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.dockWidgetContents_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.list_userlist = QtGui.QListWidget(self.dockWidgetContents_2)
        self.list_userlist.setObjectName(_fromUtf8("list_userlist"))
        self.gridLayout_3.addWidget(self.list_userlist, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_ops_count = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_ops_count.setObjectName(_fromUtf8("label_ops_count"))
        self.horizontalLayout_2.addWidget(self.label_ops_count)
        self.label_users_count = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_users_count.setObjectName(_fromUtf8("label_users_count"))
        self.horizontalLayout_2.addWidget(self.label_users_count)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1056, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuServer = QtGui.QMenu(self.menubar)
        self.menuServer.setObjectName(_fromUtf8("menuServer"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuWindow = QtGui.QMenu(self.menubar)
        self.menuWindow.setObjectName(_fromUtf8("menuWindow"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout_AwwRC = QtGui.QAction(MainWindow)
        self.actionAbout_AwwRC.setObjectName(_fromUtf8("actionAbout_AwwRC"))
        self.actionAbout_Qt = QtGui.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(_fromUtf8("actionAbout_Qt"))
        self.menuHelp.addAction(self.actionAbout_AwwRC)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuServer.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tree_networks.headerItem().setText(0, _translate("MainWindow", "Networks", None))
        self.label_servers_count.setText(_translate("MainWindow", "Servers", None))
        self.label_channels_count.setText(_translate("MainWindow", "Channels", None))
        self.label_ops_count.setText(_translate("MainWindow", "Ops", None))
        self.label_users_count.setText(_translate("MainWindow", "Users", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuServer.setTitle(_translate("MainWindow", "Server", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.menuWindow.setTitle(_translate("MainWindow", "Window", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionAbout_AwwRC.setText(_translate("MainWindow", "About AwwRC", None))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt", None))

