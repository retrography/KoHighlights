# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Apps\DEV\PROJECTS\KoHighlights\gui_edit.ui'
#
# Created: Sun Mar 31 18:17:28 2019
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

class Ui_TextDialog(object):
    def setupUi(self, TextDialog):
        TextDialog.setObjectName("TextDialog")
        TextDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        TextDialog.resize(360, 180)
        TextDialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        TextDialog.setModal(False)
        self.verticalLayout = QVBoxLayout(TextDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.high_edit_txt = QTextEdit(TextDialog)
        self.high_edit_txt.setFrameShape(QFrame.WinPanel)
        self.high_edit_txt.setAcceptRichText(False)
        self.high_edit_txt.setObjectName("high_edit_txt")
        self.verticalLayout.addWidget(self.high_edit_txt)
        self.btn_box = QFrame(TextDialog)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_box.sizePolicy().hasHeightForWidth())
        self.btn_box.setSizePolicy(sizePolicy)
        self.btn_box.setObjectName("btn_box")
        self.horizontalLayout = QHBoxLayout(self.btn_box)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QSpacerItem(175, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ok_btn = QPushButton(self.btn_box)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout.addWidget(self.ok_btn)
        self.cancel_btn = QPushButton(self.btn_box)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        self.verticalLayout.addWidget(self.btn_box)

        self.retranslateUi(TextDialog)
        QtCore.QObject.connect(self.cancel_btn, QtCore.SIGNAL("clicked()"), TextDialog.close)
        QtCore.QObject.connect(self.ok_btn, QtCore.SIGNAL("clicked()"), TextDialog.close)
        QtCore.QMetaObject.connectSlotsByName(TextDialog)

    def retranslateUi(self, TextDialog):
        self.ok_btn.setToolTip(QApplication.translate("TextDialog", "Check online for an updated version", None))
        self.ok_btn.setText(QApplication.translate("TextDialog", "OK", None))
        self.cancel_btn.setText(QApplication.translate("TextDialog", "Cancel", None))

import images_rc
