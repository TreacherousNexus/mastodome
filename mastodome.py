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


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import mainwindow

def window():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = mainwindow.MainWindow(MainWindow)
    ui.link_slots()
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
