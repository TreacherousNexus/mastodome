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

class ui_dialog_about(object):
    def setupUi(self, DialogAbout):
        DialogAbout.setObjectName(_fromUtf8("DialogAbout"))
        DialogAbout.resize(400, 446)
        icons = Icons()
        DialogAbout.setWindowIcon(QtGui.QIcon(icons.actionAboutIcon))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogAbout.sizePolicy().hasHeightForWidth())
        DialogAbout.setSizePolicy(sizePolicy)
        DialogAbout.setMinimumSize(QtCore.QSize(400, 446))
        DialogAbout.setMaximumSize(QtCore.QSize(400, 446))
        self.lblLogo = QtWidgets.QLabel(DialogAbout)
        self.lblLogo.setGeometry(QtCore.QRect(140, 70, 121, 20))
        self.lblLogo.setObjectName(_fromUtf8("lblLogo"))
        self.lblAppVersion = QtWidgets.QLabel(DialogAbout)
        self.lblAppVersion.setGeometry(QtCore.QRect(10, 160, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblAppVersion.setFont(font)
        self.lblAppVersion.setTextFormat(QtCore.Qt.RichText)
        self.lblAppVersion.setScaledContents(False)
        self.lblAppVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAppVersion.setObjectName(_fromUtf8("lblAppVersion"))
        self.lblAppDesc = QtWidgets.QLabel(DialogAbout)
        self.lblAppDesc.setGeometry(QtCore.QRect(10, 210, 381, 51))
        self.lblAppDesc.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAppDesc.setWordWrap(True)
        self.lblAppDesc.setObjectName(_fromUtf8("lblAppDesc"))
        self.lblCopyright = QtWidgets.QLabel(DialogAbout)
        self.lblCopyright.setGeometry(QtCore.QRect(10, 270, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblCopyright.setFont(font)
        self.lblCopyright.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lblCopyright.setWordWrap(True)
        self.lblCopyright.setObjectName(_fromUtf8("lblCopyright"))

        self.retranslate_ui(DialogAbout)
        QtCore.QMetaObject.connectSlotsByName(DialogAbout)

    def retranslate_ui(self, DialogAbout):
        lingo = Translations()
        pics = Pics()
        this_config = config.Config()
        DialogAbout.setWindowTitle(_translate("DialogAbout", lingo.load("DialogAbout")
                                              + " "
                                              + this_config.APP_NAME, None))
        self.lblAppVersion.setText(_translate("DialogAbout", this_config.APP_NAME
                                              + " "
                                              + this_config.APP_VERSION, None))
        self.lblAppDesc.setText(_translate("DialogAbout", this_config.APP_NAME + " " + lingo.load("lblAppDesc"), None))
        self.lblCopyright.setText(_translate("DialogAbout", "<html><head/><body><p align=\"center\">"
                                             + lingo.load("lblCopyright")
                                             + "<br/><a href=\""
                                             + this_config.APP_WEBSITE
                                             + "\"><span style=\" text-decoration: underline; color:#0000ff;\">"
                                             + this_config.APP_WEBSITE
                                             + "</span></a></p></body></html>", None))

        self.lblLogo.resize(250, 250)
        mastodome_mascot = QtGui.QPixmap(pics.aboutMascoutImg).scaled(self.lblLogo.size())
        self.lblLogo.setPixmap(mastodome_mascot)
        self.lblLogo.move(75, 20)
        self.lblAppVersion.move(10, 280)
        self.lblAppDesc.move(10, 310)
        self.lblCopyright.move(10, 360)
