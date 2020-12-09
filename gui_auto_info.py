# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Apps\DEV\PROJECTS\KoHighlights\gui_auto_info.ui'
#
# Created: Sun Mar  3 11:56:15 2019
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from boot_config import *

if QT4:  # ___ ______________ DEPENDENCIES __________________________
    from PySide.QtGui import *
    from PySide import QtCore
else:
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
    from PySide2 import QtCore
    
class Ui_AutoInfo(object):
    def setupUi(self, AutoInfo):
        AutoInfo.setObjectName("AutoInfo")
        AutoInfo.setWindowModality(QtCore.Qt.NonModal)
        AutoInfo.resize(300, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AutoInfo.sizePolicy().hasHeightForWidth())
        AutoInfo.setSizePolicy(sizePolicy)
        AutoInfo.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        AutoInfo.setModal(True)
        self.verticalLayout = QVBoxLayout(AutoInfo)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(AutoInfo)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFrameShape(QFrame.Box)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(AutoInfo)
        QtCore.QMetaObject.connectSlotsByName(AutoInfo)

    def retranslateUi(self, AutoInfo):
        AutoInfo.setWindowTitle(QApplication.translate("AutoInfo", "Info", None))

import images_rc
