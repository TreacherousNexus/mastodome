#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

    Mastodome - Desktop Client for Mastodon
    Copyright (C) 2018 Bobby Moss bob[at]bobstechsite.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

from PyQt5 import QtCore, QtGui, QtWidgets
from config.translations import Translations
from config.icons_pics import Icons, Pics
from config import config
from gui import login, about
from rest import toots, fetch, api
import validators


class MainWindow2(object):

    def __init__(self, main_window):
        self.current_session = None
        self.config = config.Config()
        self.visibleStream = "home"
        pics = Pics()
        main_window.setWindowIcon(QtGui.QIcon(pics.appLogoImg))
        main_window.setObjectName("MainWindow")
        main_window.setWindowModality(QtCore.Qt.NonModal)
        main_window.resize(1153, 685)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayoutNewToot = QtWidgets.QVBoxLayout()
        self.verticalLayoutNewToot.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayoutNewToot.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayoutNewToot.setObjectName("verticalLayoutNewToot")
        self.horizontalLayoutStreamButtons = QtWidgets.QHBoxLayout()
        self.horizontalLayoutStreamButtons.setObjectName("horizontalLayoutStreamButtons")
        self.btnHome = QtWidgets.QPushButton(self.centralwidget)
        self.btnHome.setObjectName("btnHome")
        self.horizontalLayoutStreamButtons.addWidget(self.btnHome)
        self.btnLocal = QtWidgets.QPushButton(self.centralwidget)
        self.btnLocal.setObjectName("btnLocal")
        self.horizontalLayoutStreamButtons.addWidget(self.btnLocal)
        self.btnPublic = QtWidgets.QPushButton(self.centralwidget)
        self.btnPublic.setObjectName("btnPublic")
        self.horizontalLayoutStreamButtons.addWidget(self.btnPublic)
        self.verticalLayoutNewToot.addLayout(self.horizontalLayoutStreamButtons)
        self.plainTextEditToot = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditToot.setObjectName("plainTextEditToot")
        self.verticalLayoutNewToot.addWidget(self.plainTextEditToot)
        self.horizontalLayoutTooButtons = QtWidgets.QHBoxLayout()
        self.horizontalLayoutTooButtons.setObjectName("horizontalLayoutTooButtons")
        self.btnCW = QtWidgets.QPushButton(self.centralwidget)
        self.btnCW.setObjectName("btnCW")
        self.horizontalLayoutTooButtons.addWidget(self.btnCW)
        self.cmbPrivacy = QtWidgets.QComboBox(self.centralwidget)
        self.cmbPrivacy.setObjectName("cmbPrivacy")
        self.horizontalLayoutTooButtons.addWidget(self.cmbPrivacy)
        self.btnToot = QtWidgets.QPushButton(self.centralwidget)
        self.btnToot.setObjectName("btnToot")
        self.horizontalLayoutTooButtons.addWidget(self.btnToot)
        self.verticalLayoutNewToot.addLayout(self.horizontalLayoutTooButtons)
        self.lineEditCW = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCW.setObjectName("lineEditCW")
        self.verticalLayoutNewToot.addWidget(self.lineEditCW)
        self.listViewLoggedInAccounts = QtWidgets.QListView(self.centralwidget)
        self.listViewLoggedInAccounts.setObjectName("listViewLoggedInAccounts")
        self.verticalLayoutNewToot.addWidget(self.listViewLoggedInAccounts)
        self.horizontalLayout_4.addLayout(self.verticalLayoutNewToot)
        self.verticalLayoutViewToots = QtWidgets.QVBoxLayout()
        self.verticalLayoutViewToots.setObjectName("verticalLayoutViewToots")
        self.listViewToots = QtWidgets.QListView(self.centralwidget)
        self.listViewToots.setObjectName("listViewToots")
        self.listViewToots.setAlternatingRowColors(True)
        self.verticalLayoutViewToots.addWidget(self.listViewToots)
        self.horizontalLayout_4.addLayout(self.verticalLayoutViewToots)
        self.verticalLayoutNotifications = QtWidgets.QVBoxLayout()
        self.verticalLayoutNotifications.setObjectName("verticalLayoutNotifications")
        self.listViewNotifications = QtWidgets.QListView(self.centralwidget)
        self.listViewNotifications.setObjectName("listViewNotifications")
        self.listViewNotifications.setAlternatingRowColors(True)
        self.verticalLayoutNotifications.addWidget(self.listViewNotifications)
        self.horizontalLayout_4.addLayout(self.verticalLayoutNotifications)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1153, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.actionLogin = QtWidgets.QAction(main_window)
        self.actionLogin.setObjectName("actionLogin")
        self.actionLogout = QtWidgets.QAction(main_window)
        self.actionLogout.setObjectName("actionLogout")
        self.actionExit = QtWidgets.QAction(main_window)
        self.actionExit.setObjectName("actionExit")
        self.actionRefresh = QtWidgets.QAction(main_window)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionPreferences = QtWidgets.QAction(main_window)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionHelp = QtWidgets.QAction(main_window)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(main_window)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionLogin)
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionRefresh)
        self.menuEdit.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.translate_gui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def translate_gui(self, main_window):
        lingo = Translations()
        main_title = lingo.load("MainWindow") + self.config.APP_NAME + " " + self.config.APP_VERSION
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", main_title))

    def link_slots(self):
        self.setup_top_menu()
        self.setup_buttons()
        self.setup_tootbox()

    def setup_top_menu(self):
        _translate = QtCore.QCoreApplication.translate
        lingo = Translations()
        icons = Icons()

        self.menuFile.setTitle(_translate("MainWindow", lingo.load("menuFile")))
        self.menuEdit.setTitle(_translate("MainWindow", lingo.load("menuEdit")))
        self.menuHelp.setTitle(_translate("MainWindow", lingo.load("menuHelp")))

        self.actionLogin.setText(_translate("MainWindow", lingo.load("actionLogin")))
        self.actionLogin.setShortcut(lingo.load("actionLoginShortcut"))
        self.actionLogin.setStatusTip(lingo.load("actionLoginTooltip"))
        self.actionLogin.setIcon(QtGui.QIcon(icons.actionLoginLockedIcon))
        # self.actionLogin.triggered.connect(self.login_user)

        self.actionLogout.setText(_translate("MainWindow", lingo.load("actionLogout")))
        self.actionLogout.setShortcut(lingo.load("actionLogoutShortcut"))
        self.actionLogout.setStatusTip(lingo.load("actionLogoutTooltip"))
        self.actionLogout.setIcon(QtGui.QIcon(icons.actionLogoutIcon))
        self.actionLogout.setEnabled(False)
        # self.actionLogout.triggered.connect(self.logoff_user)

        self.actionExit.setText(_translate("MainWindow", lingo.load("actionExit")))
        self.actionExit.setShortcut(lingo.load("actionExitShortcut"))
        self.actionExit.setStatusTip(lingo.load("actionExitTooltip") + " " + self.config.APP_NAME)
        self.actionExit.setIcon(QtGui.QIcon(icons.actionExiticon))
        self.actionExit.triggered.connect(QtGui.QGuiApplication.quit)

        self.actionRefresh.setText(_translate("MainWindow", lingo.load("actionRefresh")))
        self.actionRefresh.setShortcut(lingo.load("actionRefreshShortcut"))
        self.actionRefresh.setStatusTip(lingo.load("actionRefreshTooltip"))
        self.actionRefresh.setIcon(QtGui.QIcon(icons.actionRefreshIcon))
        # self.actionRefresh.triggered.connect(self.reload_panels)

        self.actionPreferences.setText(_translate("MainWindow", lingo.load("actionPreferences")))
        self.actionPreferences.setStatusTip(lingo.load("actionPreferencesTooltip"))
        self.actionPreferences.setIcon(QtGui.QIcon(icons.actionPrefIcon))
        self.actionPreferences.setEnabled(False)

        self.actionHelp.setText(_translate("MainWindow", lingo.load("actionHelp")))
        self.actionHelp.setShortcut(lingo.load("actionHelpShortcut"))
        self.actionHelp.setStatusTip(lingo.load("actionHelpTooltip"))
        self.actionHelp.setIcon(QtGui.QIcon(icons.actionHelpIcon))
        self.actionHelp.setEnabled(False)

        self.actionAbout.setText(_translate("MainWindow", lingo.load("actionAbout")))
        self.actionAbout.setStatusTip(lingo.load("actionAboutTooltip") + " " + self.config.APP_NAME)
        self.actionAbout.setIcon(QtGui.QIcon(icons.actionAboutIcon))
        self.actionAbout.triggered.connect(self.display_about)

    def setup_buttons(self):
        _translate = QtCore.QCoreApplication.translate
        lingo = Translations()
        icons = Icons()

        self.btnHome.setShortcut(lingo.load("btnHomeShortcut"))
        self.btnHome.setStatusTip(lingo.load("btnHomeTooltip")
                                  + " (" + lingo.load("btnHomeShortcut") + ")")
        self.btnHome.setIcon(QtGui.QIcon(icons.btnHomeIcon))
        # self.btnHome.clicked.connect(self.load_stream_home)
        self.btnHome.setEnabled(False)

        self.btnLocal.setShortcut(lingo.load("btnLocalShortcut"))
        self.btnLocal.setStatusTip(lingo.load("btnLocalTooltip")
                                   + " (" + lingo.load("btnLocalShortcut") + ")")
        self.btnLocal.setIcon(QtGui.QIcon(icons.btnLocalIcon))
        # self.btnLocal.clicked.connect(self.load_stream_local)
        self.btnLocal.setEnabled(False)

        self.btnPublic.setShortcut(lingo.load("btnPublicShortcut"))
        self.btnPublic.setStatusTip(lingo.load("btnPublicTooltip")
                                    + " (" + lingo.load("btnPublicShortcut") + ")")
        self.btnPublic.setIcon(QtGui.QIcon(icons.btnPublicIcon))
        # self.btnPublic.clicked.connect(self.load_stream_public)
        self.btnPublic.setEnabled(False)

        self.btnCW.setText(_translate("MainWindow", lingo.load("btnCW")))
        self.btnCW.setStatusTip(lingo.load("btnCWTooltipInactive"))
        self.btnCW.clicked.connect(self.hide_show_cw)
        self.btnCW.setEnabled(False)

        self.btnToot.setText(_translate("MainWindow", lingo.load("btnToot")))
        self.btnToot.setShortcut(lingo.load("btnTootShortcut"))
        self.btnToot.setStatusTip(lingo.load("btnTootTooltip")
                                  + " (" + lingo.load("btnTootShortcut") + ")")
        self.btnToot.setEnabled(False)
        # self.btnToot.clicked.connect(self.send_toot)

    def setup_tootbox(self):
        lingo = Translations()
        icons = Icons()
        self.lineEditCW.setMaxLength(self.config.GUI_TOOT_MAX_SIZE_CHARS)
        self.lineEditCW.textChanged.connect(self.check_toot_box)
        self.lineEditCW.setVisible(False)
        self.lineEditCW.setEnabled(False)

        self.plainTextEditToot.textChanged.connect(self.check_toot_box)
        self.plainTextEditToot.setEnabled(False)

        privacy_options = dict(lingo.load("cmbPrivacy"))
        self.cmbPrivacy.clear()
        self.cmbPrivacy.addItem(QtGui.QIcon(icons.cmbPublicToot), privacy_options["public"])
        self.cmbPrivacy.addItem(QtGui.QIcon(icons.cmbUnlistedToot), privacy_options["unlisted"])
        self.cmbPrivacy.addItem(QtGui.QIcon(icons.cmbFollowerOnlyToot), privacy_options["followers-only"])
        self.cmbPrivacy.addItem(QtGui.QIcon(icons.cmbDirectMessageToot), privacy_options["direct-message"])
        self.cmbPrivacy.setEnabled(False)

        self.listViewLoggedInAccounts.setEnabled(False)

    def check_toot_box(self):
        current_length = len(self.plainTextEditToot.toPlainText())
        max_length = self.config.GUI_TOOT_MAX_SIZE_CHARS
        if self.lineEditCW.isEnabled():
            max_length -= len(self.lineEditCW.text())
        self.btnToot.setEnabled(0 < current_length < max_length)

        if current_length >= max_length:
            self.plainTextEditToot.setStyleSheet("color: rgb(206, 92, 92);")
        else:
            self.plainTextEditToot.setStyleSheet("")

    def hide_show_cw(self):
        if self.lineEditCW.isEnabled():
            self.lineEditCW.setVisible(False)
            self.lineEditCW.setEnabled(False)
        else:
            self.lineEditCW.setEnabled(True)
            self.lineEditCW.setVisible(True)

    def display_about(self):
        about_dialog = QtWidgets.QDialog()
        about_dialog.ui = about.ui_dialog_about()
        about_dialog.ui.setupUi(about_dialog)
        about_dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        about_dialog.exec_()
