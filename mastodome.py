#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from gui import mainwindow

def window():
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = mainwindow.MainWindow(MainWindow)
    ui.link_slots()
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    window()
