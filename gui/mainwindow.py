#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from config.translations import Translations
from config.icons_pics import Icons, Pics
from config import config
from gui import login, about
from rest import toots, fetch, api
import validators

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class MainWindow(object):

    def __init__(self, main_window):
        self.current_session = None
        self.config = config.Config()
        self.visibleStream = "home"
        main_window.setObjectName(_fromUtf8("MainWindow"))
        main_window.resize(849, 603)
        main_window.setMinimumSize(QtCore.QSize(849, 603))
        main_window.setMaximumSize(QtCore.QSize(849, 603))
        pics = Pics()
        main_window.setWindowIcon(QtGui.QIcon(pics.appLogoImg))
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 171, 561))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.vLayoutLeftColumn = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vLayoutLeftColumn.setContentsMargins(5, 5, 5, 5)
        self.vLayoutLeftColumn.setObjectName(_fromUtf8("vLayoutLeftColumn"))
        self.vLayoutToot = QtWidgets.QVBoxLayout()
        self.vLayoutToot.setObjectName(_fromUtf8("vLayoutToot"))
        self.vLayoutTootBox = QtWidgets.QVBoxLayout()
        self.vLayoutTootBox.setObjectName(_fromUtf8("vLayoutTootBox"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btnHomeStream = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnHomeStream.setObjectName(_fromUtf8("btnHomeStream"))
        self.horizontalLayout.addWidget(self.btnHomeStream)
        self.btnLocalStream = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnLocalStream.setObjectName(_fromUtf8("btnLocalStream"))
        self.horizontalLayout.addWidget(self.btnLocalStream)
        self.btnPublicStream = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnPublicStream.setObjectName(_fromUtf8("btnPublicStream"))
        self.horizontalLayout.addWidget(self.btnPublicStream)
        self.vLayoutTootBox.addLayout(self.horizontalLayout)
        self.plainTextTootBox = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextTootBox.setObjectName(_fromUtf8("plainTextTootBox"))
        self.vLayoutTootBox.addWidget(self.plainTextTootBox)
        self.vLayoutToot.addLayout(self.vLayoutTootBox)
        self.vLayoutTootBtn = QtWidgets.QVBoxLayout()
        self.vLayoutTootBtn.setObjectName(_fromUtf8("vLayoutTootBtn"))
        self.btnToot = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnToot.setObjectName(_fromUtf8("btnToot"))
        self.vLayoutTootBtn.addWidget(self.btnToot)
        self.vLayoutToot.addLayout(self.vLayoutTootBtn)
        self.vLayoutLeftColumn.addLayout(self.vLayoutToot)
        self.vLayoutPanelOpts = QtWidgets.QVBoxLayout()
        self.vLayoutPanelOpts.setObjectName(_fromUtf8("vLayoutPanelOpts"))
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblStatus = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
        self.verticalLayout.addWidget(self.lblStatus)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.vLayoutPanelOpts.addLayout(self.verticalLayout)
        self.vLayoutLeftColumn.addLayout(self.vLayoutPanelOpts)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(170, 0, 331, 561))
        self.verticalLayoutWidget_6.setObjectName(_fromUtf8("verticalLayoutWidget_6"))
        self.vLayoutCentreColumn = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.vLayoutCentreColumn.setContentsMargins(5, 5, 5, 5)
        self.vLayoutCentreColumn.setObjectName(_fromUtf8("vLayoutCentreColumn"))
        self.listOfToots = QtWidgets.QListView(self.verticalLayoutWidget_6)
        self.listOfToots.setObjectName(_fromUtf8("listOfToots"))
        self.listOfToots.setAlternatingRowColors(True)
        self.vLayoutCentreColumn.addWidget(self.listOfToots)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(510, 0, 331, 561))
        self.verticalLayoutWidget_7.setObjectName(_fromUtf8("verticalLayoutWidget_7"))
        self.vLayoutRightColumn = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.vLayoutRightColumn.setContentsMargins(5, 5, 5, 5)
        self.vLayoutRightColumn.setObjectName(_fromUtf8("vLayoutRightColumn"))
        self.listOfNotifications = QtWidgets.QListView(self.verticalLayoutWidget_7)
        self.listOfNotifications.setObjectName(_fromUtf8("listOfNotifications"))
        self.listOfNotifications.setAlternatingRowColors(True)
        self.vLayoutRightColumn.addWidget(self.listOfNotifications)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuInsert = QtWidgets.QMenu(self.menubar)
        self.menuInsert.setObjectName(_fromUtf8("menuInsert"))
        self.menuRSS = QtWidgets.QMenu(self.menubar)
        self.menuRSS.setObjectName(_fromUtf8("menuRSS"))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        main_window.setStatusBar(self.statusbar)
        self.actionLogin = QtWidgets.QAction(main_window)
        self.actionLogin.setObjectName(_fromUtf8("actionLogin"))
        self.actionLogout = QtWidgets.QAction(main_window)
        self.actionLogout.setObjectName(_fromUtf8("actionLogout"))
        self.actionExit = QtWidgets.QAction(main_window)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionRefresh = QtWidgets.QAction(main_window)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.actionPreferences = QtWidgets.QAction(main_window)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionOnline_Help = QtWidgets.QAction(main_window)
        self.actionOnline_Help.setObjectName(_fromUtf8("actionOnline_Help"))
        self.actionAbout = QtWidgets.QAction(main_window)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionLink = QtWidgets.QAction(main_window)
        self.actionLink.setObjectName(_fromUtf8("actionLink"))
        self.actionSubscribe_to = QtWidgets.QAction(main_window)
        self.actionSubscribe_to.setObjectName(_fromUtf8("actionSubscribe_to"))
        self.menuFile.addAction(self.actionLogin)
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionRefresh)
        self.menuEdit.addAction(self.actionPreferences)
        self.menuHelp.addAction(self.actionOnline_Help)
        self.menuHelp.addAction(self.actionAbout)
        self.menuInsert.addAction(self.actionLink)
        self.menuInsert.addSeparator()
        self.menuRSS.addAction(self.actionSubscribe_to)
        self.menuRSS.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuInsert.menuAction())
        self.menubar.addAction(self.menuRSS.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.translate_gui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def translate_gui(self, main_window):
        lingo = Translations()
        main_title = lingo.load("MainWindow") + self.config.APP_NAME + " " + self.config.APP_VERSION
        main_window.setWindowTitle(_translate("MainWindow", main_title, None))
        self.btnToot.setText(_translate("MainWindow", lingo.load("btnToot"), None))
        self.lblStatus.setText(_translate("MainWindow", lingo.load("lblStatus"), None))
        self.menuFile.setTitle(_translate("MainWindow", lingo.load("menuFile"), None))
        self.menuEdit.setTitle(_translate("MainWindow", lingo.load("menuEdit"), None))
        self.menuHelp.setTitle(_translate("MainWindow", lingo.load("menuHelp"), None))
        self.menuInsert.setTitle(_translate("MainWindow", lingo.load("menuInsert"), None))
        self.menuRSS.setTitle(_translate("MainWindow", lingo.load("menuRSS"), None))
        self.actionLogin.setText(_translate("MainWindow", lingo.load("actionLogin"), None))
        self.actionLogout.setText(_translate("MainWindow", lingo.load("actionLogout"), None))
        self.actionExit.setText(_translate("MainWindow", lingo.load("actionExit"), None))
        self.actionRefresh.setText(_translate("MainWindow", lingo.load("actionRefresh"), None))
        self.actionPreferences.setText(_translate("MainWindow", lingo.load("actionPreferences"), None))
        self.actionOnline_Help.setText(_translate("MainWindow", lingo.load("actionOnline_Help"), None))
        self.actionAbout.setText(_translate("MainWindow", lingo.load("actionAbout"), None))
        self.actionLink.setText(_translate("MainWindow", lingo.load("actionLink"), None))
        self.actionSubscribe_to.setText(_translate("MainWindow", lingo.load("actionSubscribe_to"), None))

    def link_slots(self):
        self.setup_top_menu()
        self.setup_buttons()
        self.setup_tootbox()

    def setup_top_menu(self):
        lingo = Translations()
        icons = Icons()

        self.actionLogin.setIcon(QtGui.QIcon(icons.actionLoginLockedIcon))
        self.actionLogin.setShortcut(lingo.load("actionLoginShortcut"))
        self.actionLogin.setStatusTip(lingo.load("actionLoginTooltip"))
        self.actionLogin.triggered.connect(self.login_user)

        self.actionLogout.setIcon(QtGui.QIcon(icons.actionLogoutIcon))
        self.actionLogout.setShortcut(lingo.load("actionLogoutShortcut"))
        self.actionLogout.setStatusTip(lingo.load("actionLogoutTooltip"))
        self.actionLogout.triggered.connect(self.logoff_user)
        self.actionLogout.setEnabled(False)

        self.actionExit.setIcon(QtGui.QIcon(icons.actionExiticon))
        self.actionExit.setShortcut(lingo.load("actionExitShortcut"))
        self.actionExit.setStatusTip(lingo.load("actionExitTooltip") + " " + self.config.APP_NAME)
        self.actionExit.triggered.connect(QtGui.QGuiApplication.quit)

        self.actionRefresh.setIcon(QtGui.QIcon(icons.actionRefreshIcon))
        self.actionRefresh.setShortcut(lingo.load("actionRefreshShortcut"))
        self.actionRefresh.setStatusTip(lingo.load("actionRefreshTooltip"))
        self.actionRefresh.triggered.connect(self.reload_panels)

        self.actionPreferences.setIcon(QtGui.QIcon(icons.actionPrefIcon))
        self.actionPreferences.setStatusTip(lingo.load("actionPreferencesTooltip"))
        self.actionPreferences.setEnabled(False)

        self.actionLink.setIcon(QtGui.QIcon(icons.actionLinkIcon))
        self.actionLink.setStatusTip(lingo.load("actionLinkTooltip"))
        self.actionLink.setEnabled(False)

        self.actionSubscribe_to.setIcon(QtGui.QIcon(icons.actionSubscribeIcon))
        self.actionSubscribe_to.setStatusTip(lingo.load("actionSubscribe_toTooltip"))
        self.actionSubscribe_to.setEnabled(False)

        self.actionOnline_Help.setIcon(QtGui.QIcon(icons.actionHelpIcon))
        self.actionOnline_Help.setShortcut(lingo.load("actionOnline_HelpShortcut"))
        self.actionOnline_Help.setStatusTip(lingo.load("actionOnline_HelpTooltip"))
        self.actionOnline_Help.setEnabled(False)

        self.actionAbout.setIcon(QtGui.QIcon(icons.actionAboutIcon))
        self.actionAbout.setStatusTip(lingo.load("actionAboutTooltip") + " " + self.config.APP_NAME)
        self.actionAbout.triggered.connect(self.display_about)

    def setup_buttons(self):
        lingo = Translations()
        icons = Icons()
        self.btnHomeStream.setIcon(QtGui.QIcon(icons.btnHomeIcon))
        self.btnHomeStream.setShortcut(lingo.load("btnHomeStreamShortcut"))
        self.btnHomeStream.setStatusTip(lingo.load("btnHomeStreamTooltip")
                                        + " (" + lingo.load("btnHomeStreamShortcut") + ")")
        self.btnHomeStream.clicked.connect(self.load_stream_home)

        self.btnLocalStream.setIcon(QtGui.QIcon(icons.btnLocalIcon))
        self.btnLocalStream.setShortcut(lingo.load("btnLocalStreamShortcut"))
        self.btnLocalStream.setStatusTip(lingo.load("btnLocalStreamTooltip")
                                         + " (" + lingo.load("btnLocalStreamShortcut") + ")")
        self.btnLocalStream.clicked.connect(self.load_stream_local)

        self.btnPublicStream.setIcon(QtGui.QIcon(icons.btnPublicIcon))
        self.btnPublicStream.setShortcut(lingo.load("btnPublicStreamShortcut"))
        self.btnPublicStream.setStatusTip(lingo.load("btnPublicStreamTooltip")
                                          + " (" + lingo.load("btnPublicStreamShortcut") + ")")
        self.btnPublicStream.clicked.connect(self.load_stream_public)

        self.btnToot.setStatusTip(lingo.load("btnTootTooltip"))
        self.btnToot.clicked.connect(self.send_toot)
        self.btnToot.setEnabled(False)

    def setup_tootbox(self):
        self.plainTextTootBox.setFocus(True)
        self.plainTextTootBox.textChanged.connect(self.check_toot_box)

    def login_user(self):
        lingo = Translations()
        self.lblStatus.setText(lingo.load("lblStatusAction"))
        dialog = QtWidgets.QDialog()
        dialog.ui = login.ui_login_dialog()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.accepted.connect(lambda: self.complete_login(dialog))
        dialog.rejected.connect(self.cancelled_login)
        dialog.destroyed.connect(lambda: self.check_login_status(dialog))
        dialog.exec_()

    def complete_login(self, dialog):
        self.current_session = dialog.ui.get_new_session()
        lingo = Translations()
        if self.current_session is not None:
            self.actionLogin.setEnabled(False)
            icons = Icons()
            self.actionLogin.setIcon(QtGui.QIcon(icons.actionLoginUnlockedIcon))
            self.actionLogout.setEnabled(True)
            status_start = lingo.load("lblStatusComplete")
            self.lblStatus.setText(status_start + ": " + self.current_session.get_account_username()
                                   + "@" + self.current_session.get_session_domain())
            self.btnToot.setEnabled(True)
            self.disable_all_stream_buttons()
            self.reload_panels()
            self.enable_correct_stream_button()

    def cancelled_login(self):
        lingo = Translations()
        self.lblStatus.setText(lingo.load("lblStatus"))

    def check_login_status(self, dialog):
        problem = dialog.ui.get_latest_exception()
        if problem is not None:
            error_msg = QtWidgets.QErrorMessagee()
            error_msg.showMessage(str(problem))
            error_msg.exec_()
            lingo = Translations()
            self.lblStatus.setText(lingo.load("lblStatus"))

    def logoff_user(self):
        if self.current_session is not None:
            existing_session = api.Session(self.current_session.get_session_domain(),
                                           self.current_session.get_session_username())
            existing_session.load_session(self.current_session)
            existing_session.clear_session()
            self.current_session = None
            self.actionLogout.setEnabled(False)
            self.actionLogin.setEnabled(True)
            icons = Icons()
            self.actionLogin.setIcon(QtGui.QIcon(icons.actionLoginLockedIcon))
            lingo = Translations()
            self.lblStatus.setText(lingo.load("lblStatus"))
            self.btnToot.setEnabled(False)
            self.reset_panels()
            fetch.clear_image_cache()

    def display_about(self):
        about_dialog = QtWidgets.QDialog()
        about_dialog.ui = about.ui_dialog_about()
        about_dialog.ui.setupUi(about_dialog)
        about_dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        about_dialog.exec_()

    def send_toot(self):
        if self.current_session is not None:
            potential_toot = str(self.plainTextTootBox.toPlainText())
            if validators.length(potential_toot, max=self.config.GUI_TOOT_MAX_SIZE_CHARS):
                self.current_session.send_toot(potential_toot)
                self.plainTextTootBox.clear()
            else:
                print('Toot too long')
                raise ValueError
            lingo = Translations()
            self.btnToot.setEnabled(False)
            self.btnToot.setText(lingo.load("btnTootLoad"))
            self.reload_panels()
            self.btnToot.setEnabled(True)
            self.btnToot.setText(lingo.load("btnToot"))

    def reload_panels(self):
        if self.current_session is not None:
            self.load_stream_notifications()
            if self.visibleStream == "home":
                self.load_stream_home()
            elif self.visibleStream == "local":
                self.load_stream_local()
            elif self.visibleStream == "public":
                self.load_stream_public()

    def reset_panels(self):
        notifications_model = QtGui.QStandardItemModel(self.listOfNotifications)
        toots_model = QtGui.QStandardItemModel(self.listOfToots)
        self.listOfNotifications.setModel(notifications_model)
        self.listOfToots.setModel(toots_model)

    def load_stream_home(self):
        if self.current_session is not None:
            self.visibleStream = "home"
            self.disable_all_stream_buttons()
            self.load_stream_toots(self.current_session.get_home_stream())
            self.enable_correct_stream_button()

    def load_stream_local(self):
        if self.current_session is not None:
            self.visibleStream = "local"
            self.disable_all_stream_buttons()
            self.load_stream_toots(self.current_session.get_local_stream())
            self.enable_correct_stream_button()

    def load_stream_public(self):
        if self.current_session is not None:
            self.visibleStream = "public"
            self.disable_all_stream_buttons()
            self.load_stream_toots(self.current_session.get_public_stream())
            self.enable_correct_stream_button()

    def disable_all_stream_buttons(self):
        self.btnHomeStream.setEnabled(False)
        self.btnLocalStream.setEnabled(False)
        self.btnPublicStream.setEnabled(False)

    def enable_correct_stream_button(self):
        self.btnHomeStream.setEnabled(self.visibleStream is not "home")
        self.btnLocalStream.setEnabled(self.visibleStream is not "local")
        self.btnPublicStream.setEnabled(self.visibleStream is not "public")

    def load_stream_toots(self, toot_stream):
        if self.current_session is not None:
            lingo = Translations()
            model = QtGui.QStandardItemModel(self.listOfNotifications)
            stream_to_load = toots.Toots(toot_stream)
            stream_to_load.process()
            for timestamp, toot in list(stream_to_load.get_toots().items()):
                item = QtGui.QStandardItem()
                icon = QtGui.QIcon()
                image = QtGui.QImage()
                if toot.is_boost():
                    boosted_toot, boosted_timestamp = toot.get_boost_with_timestamp()
                    image.load(fetch.get_image(boosted_toot.get_avatar()))
                    output = boosted_toot.get_display_name() + " " + lingo.load("stream_toot_fetched") + ":\n\"" \
                             + boosted_toot.get_content().rstrip() + "\""
                    item.setText(output + "\n" + lingo.load("stream_boost_fetched") + ": " + toot.get_display_name())
                elif toot.is_reply():
                    image.load(fetch.get_image(toot.get_avatar()))
                    item.setText(toot.get_display_name() + " " + lingo.load("stream_reply_fetched") + ":\n\""
                                 + toot.get_content().rstrip() + "\"")
                else:
                    image.load(fetch.get_image(toot.get_avatar()))
                    item.setText(toot.get_display_name() + " " + lingo.load("stream_toot_fetched") + ":\n\""
                                 + toot.get_content().rstrip() + "\"")
                icon.addPixmap(QtGui.QPixmap(image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(icon)
                model.appendRow(item)
            self.listOfToots.setModel(model)

    def load_stream_notifications(self):
        if self.current_session is not None:
            lingo = Translations()
            model = QtGui.QStandardItemModel(self.listOfNotifications)

            notifications = self.current_session.get_notifications()
            for timestamp, notification in list(notifications.items()):
                item = QtGui.QStandardItem()
                if notification.n_type == "follow":
                    item.setText(notification.get_display_name() + " " + lingo.load("notify_follow") + ".")
                elif notification.n_type == "reblog":
                    item.setText(notification.get_display_name() + " " + lingo.load("notify_reblog") + " " + notification.status['uri'])
                elif notification.n_type == "favourite":
                    item.setText(notification.get_display_name() + " " + lingo.load("notify_fav") + " " + notification.status['uri'])
                elif notification.n_type == "mention":
                    item.setText(notification.get_display_name() + " " + lingo.load("notify_mention") + " " + notification.status['uri'])
                icon = QtGui.QIcon()
                image = QtGui.QImage()
                image.load(fetch.get_image(notification.get_avatar()))
                icon.addPixmap(QtGui.QPixmap(image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(icon)
                model.appendRow(item)
            self.listOfNotifications.setModel(model)

    def check_toot_box(self):
        current_length = self.plainTextTootBox.toPlainText().length()
        self.btnToot.setEnabled(0 < current_length < self.config.GUI_TOOT_MAX_SIZE_CHARS)

        if current_length >= self.config.GUI_TOOT_MAX_SIZE_CHARS:
            self.plainTextTootBox.setStyleSheet("background-color: rgb(206, 92, 92);")
        else:
            self.plainTextTootBox.setStyleSheet("background-color: rgb(255, 255, 255);")
