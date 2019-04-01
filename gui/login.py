# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from mastodon.Mastodon import MastodonError
from config.translations import Translations
from config.icons_pics import Pics
from rest.credentials import Credentials
from rest import api
import validators


class ui_login_dialog(object):

    def setupUi(self, loginDialog):
        loginDialog.setObjectName("loginDialog")
        loginDialog.resize(400, 300)
        loginDialog.setMinimumSize(QtCore.QSize(400, 300))
        loginDialog.setMaximumSize(QtCore.QSize(400, 300))
        pics = Pics()
        loginDialog.setWindowIcon(QtGui.QIcon(pics.loginLogoImg))
        self.new_session = None
        self.logged_in_domain = None
        self.latest_exception = None
        self.logged_in_user = None
        self.buttonBox = QtWidgets.QDialogButtonBox(loginDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
                            QtWidgets.QDialogButtonBox.Cancel
                            | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(loginDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 120, 341, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(
                                QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.mServerLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.mServerLabel.setObjectName("mServerLabel")
        self.formLayout.setWidget(0,
                                  QtWidgets.QFormLayout.LabelRole,
                                  self.mServerLabel)
        self.mServerLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.mServerLineEdit.setInputMethodHints(
                                QtCore.Qt.ImhUrlCharactersOnly)
        self.mServerLineEdit.setObjectName("mServerLineEdit")
        self.formLayout.setWidget(0,
                                  QtWidgets.QFormLayout.FieldRole,
                                  self.mServerLineEdit)
        self.unameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.unameLabel.setObjectName("unameLabel")
        self.formLayout.setWidget(1,
                                  QtWidgets.QFormLayout.LabelRole,
                                  self.unameLabel)
        self.uNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.uNameLineEdit.setObjectName("uNameLineEdit")
        self.formLayout.setWidget(1,
                                  QtWidgets.QFormLayout.FieldRole,
                                  self.uNameLineEdit)
        self.pwdLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.pwdLabel.setObjectName("pwdLabel")
        self.formLayout.setWidget(2,
                                  QtWidgets.QFormLayout.LabelRole,
                                  self.pwdLabel)
        self.pwdLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pwdLineEdit.setInputMethodHints(
                            QtCore.Qt.ImhHiddenText
                            | QtCore.Qt.ImhNoAutoUppercase
                            | QtCore.Qt.ImhNoPredictiveText)
        self.pwdLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwdLineEdit.setObjectName("pwdLineEdit")
        self.formLayout.setWidget(2,
                                  QtWidgets.QFormLayout.FieldRole,
                                  self.pwdLineEdit)
        self.lblMastoLogo = QtWidgets.QLabel(loginDialog)
        self.lblMastoLogo.setGeometry(QtCore.QRect(140, 50, 120, 20))
        self.lblMastoLogo.setObjectName("lblMastoLogo")

        self.retranslate_ui(loginDialog)

        self.buttonBox.accepted.connect(loginDialog.accept)
        self.buttonBox.rejected.connect(loginDialog.reject)

        QtCore.QMetaObject.connectSlotsByName(loginDialog)
        loginDialog.accepted.connect(self.complete_login)

    def retranslate_ui(self, loginDialog):
        lingo = Translations()
        pics = Pics()
        _translate = QtCore.QCoreApplication.translate
        loginDialog.setWindowTitle(_translate("loginDialog",
                                              lingo.load("loginDialog"),
                                              None))
        self.mServerLabel.setText(_translate("loginDialog",
                                             lingo.load("mServerLabel"),
                                             None))
        self.unameLabel.setText(_translate("loginDialog",
                                           lingo.load("unameLabel"),
                                           None))
        self.pwdLabel.setText(_translate("loginDialog",
                                         lingo.load("pwdLabel"),
                                         None))

        self.lblMastoLogo.resize(120, 120)
        mastodon_mascot = QtGui.QPixmap(
                        pics.loginMascotImg).scaled(self.lblMastoLogo.size())
        self.lblMastoLogo.setPixmap(mastodon_mascot)
        self.lblMastoLogo.move(140, 5)

        self.mServerLineEdit.setText("https://")
        self.mServerLineEdit.setFocus(True)

    def complete_login(self):
        server_url = str(self.mServerLineEdit.text())
        user_name = str(self.uNameLineEdit.text())

        if not validators.url(server_url):
            print('Not a valid server URL')
            self.latest_exception = ValueError("Not a valid server URL")
            raise ValueError

        if not validators.email(user_name):
            print('Not a valid user name')
            self.latest_exception = ValueError("Not a valid user name")
            raise ValueError

        self.logged_in_domain = server_url
        login_attempt = Credentials(server_url, user_name)

        try:
            if not login_attempt.is_client_registered():
                login_attempt.client_register()
        except MastodonError as m:
            print(type(m))
            self.latest_exception = MastodonError(m)
            raise

        user_pwd = str(self.pwdLineEdit.text())
        try:
            if not login_attempt.is_user_registered():
                login_attempt.user_register(user_pwd)
        except MastodonError as m:
            print(type(m))
            self.latest_exception = MastodonError(m)
            raise

        try:
            self.create_session(server_url, user_name, user_pwd)
        except MastodonError as m:
            print(type(m))
            self.latest_exception = MastodonError(m)
            raise

    def create_session(self, server_url, user_name, user_pwd):
        new_session = api.Session(server_url, user_name)
        new_session.initialise_session(user_pwd)
        self.new_session = new_session
        self.logged_in_domain = server_url
        self.logged_in_user = user_name

    def set_domain_and_user(self, server_url, user_name):
        if type(server_url) is str and type(user_name) is str:
            self.mServerLineEdit.setText(server_url)
            self.uNameLineEdit.setText(user_name)
            self.pwdLineEdit.setFocus(True)

    def get_new_session(self):
        return self.new_session

    def get_logged_in_domain(self):
        return self.logged_in_domain

    def get_logged_in_user(self):
        return self.logged_in_user

    def get_latest_exception(self):
        return self.latest_exception
