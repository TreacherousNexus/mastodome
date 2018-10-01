#!/usr/bin/env python
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

from PyQt4 import QtCore, QtGui
from config.translations import Translations
from config.icons_pics import Pics
from rest.credentials import Credentials
from rest import api
import validators

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


class ui_login_dialog(object):

    def setupUi(self, loginDialog):
        loginDialog.setObjectName(_fromUtf8("loginDialog"))
        loginDialog.resize(400, 300)
        loginDialog.setMinimumSize(QtCore.QSize(400, 300))
        loginDialog.setMaximumSize(QtCore.QSize(400, 300))
        pics = Pics()
        loginDialog.setWindowIcon(QtGui.QIcon(pics.loginLogoImg))
        self.new_session = None
        self.buttonBox = QtGui.QDialogButtonBox(loginDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayoutWidget = QtGui.QWidget(loginDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 120, 341, 101))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.mServerLabel = QtGui.QLabel(self.formLayoutWidget)
        self.mServerLabel.setObjectName(_fromUtf8("mServerLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.mServerLabel)
        self.mServerLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.mServerLineEdit.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        self.mServerLineEdit.setObjectName(_fromUtf8("mServerLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.mServerLineEdit)
        self.unameLabel = QtGui.QLabel(self.formLayoutWidget)
        self.unameLabel.setObjectName(_fromUtf8("unameLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.unameLabel)
        self.uNameLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.uNameLineEdit.setObjectName(_fromUtf8("uNameLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.uNameLineEdit)
        self.pwdLabel = QtGui.QLabel(self.formLayoutWidget)
        self.pwdLabel.setObjectName(_fromUtf8("pwdLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.pwdLabel)
        self.pwdLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.pwdLineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.pwdLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.pwdLineEdit.setObjectName(_fromUtf8("pwdLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.pwdLineEdit)
        self.lblMastoLogo = QtGui.QLabel(loginDialog)
        self.lblMastoLogo.setGeometry(QtCore.QRect(140, 50, 120, 20))
        self.lblMastoLogo.setObjectName(_fromUtf8("lblMastoLogo"))

        self.retranslate_ui(loginDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), loginDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), loginDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(loginDialog)
        loginDialog.accepted.connect(self.complete_login)

    def retranslate_ui(self, loginDialog):
        lingo = Translations()
        pics = Pics()
        loginDialog.setWindowTitle(_translate("loginDialog", lingo.load("loginDialog"), None))
        self.mServerLabel.setText(_translate("loginDialog", lingo.load("mServerLabel"), None))
        self.unameLabel.setText(_translate("loginDialog", lingo.load("unameLabel"), None))
        self.pwdLabel.setText(_translate("loginDialog", lingo.load("pwdLabel"), None))

        self.lblMastoLogo.resize(120, 120)
        mastodon_mascot = QtGui.QPixmap(pics.loginMascotImg).scaled(self.lblMastoLogo.size())
        self.lblMastoLogo.setPixmap(mastodon_mascot)
        self.lblMastoLogo.move(140, 5)

        self.mServerLineEdit.setText("https://")
        self.mServerLineEdit.setFocus(True)

    def complete_login(self):
        server_url = str(self.mServerLineEdit.text())
        user_name = str(self.uNameLineEdit.text())

        if not validators.url(server_url):
            print('Not a valid server URL')
            raise ValueError

        if not validators.email(user_name):
            print('Not a valid user name')
            raise ValueError

        login_attempt = Credentials(server_url)
        try:
            if not login_attempt.is_client_registered():
                login_attempt.client_register()
        except Exception as inst:
            print type(inst)
            raise

        user_pwd = str(self.pwdLineEdit.text())
        try:
            if not login_attempt.is_user_registered():
                login_attempt.user_register(user_name, user_pwd)
        except Exception as inst:
            print type(inst)
            raise

        try:
            new_session = api.Session(server_url)
            new_session.initialise_session(user_name, user_pwd)
            self.new_session = new_session
        except Exception as inst:
            print type(inst)
            raise

    def get_new_session(self):
        return self.new_session
