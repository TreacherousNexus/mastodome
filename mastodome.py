#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
