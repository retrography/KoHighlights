# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Apps\DEV\PROJECTS\KoHighlights\gui_status.ui'
#
# Created: Sat Mar 30 00:34:32 2019
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
    
class Ui_Status(object):
    def setupUi(self, Status):
        Status.setObjectName("Status")
        Status.resize(277, 55)
        Status.setWindowTitle("")
        self.horizontalLayout_2 = QHBoxLayout(Status)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QFrame(Status)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.anim_lbl = QLabel(self.frame)
        self.anim_lbl.setText("")
        self.anim_lbl.setObjectName("anim_lbl")
        self.horizontalLayout.addWidget(self.anim_lbl)
        self.show_items_btn = QToolButton(self.frame)
        self.show_items_btn.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        icon = QIcon()
        icon.addPixmap(QPixmap(":/stuff/show_pages.png"), QIcon.Normal, QIcon.Off)
        self.show_items_btn.setIcon(icon)
        self.show_items_btn.setIconSize(QtCore.QSize(24, 24))
        self.show_items_btn.setChecked(False)
        self.show_items_btn.setPopupMode(QToolButton.InstantPopup)
        self.show_items_btn.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.show_items_btn.setObjectName("show_items_btn")
        self.horizontalLayout.addWidget(self.show_items_btn)
        self.horizontalLayout_2.addWidget(self.frame)
        self.act_page = QAction(Status)
        self.act_page.setCheckable(True)
        self.act_page.setObjectName("act_page")
        self.act_date = QAction(Status)
        self.act_date.setCheckable(True)
        self.act_date.setObjectName("act_date")
        self.act_text = QAction(Status)
        self.act_text.setCheckable(True)
        self.act_text.setObjectName("act_text")
        self.act_comment = QAction(Status)
        self.act_comment.setCheckable(True)
        self.act_comment.setObjectName("act_comment")

        self.retranslateUi(Status)
        QtCore.QMetaObject.connectSlotsByName(Status)

    def retranslateUi(self, Status):
        self.show_items_btn.setToolTip(QApplication.translate("Status", "Show/Hide elements of Highlights. Also affects\n"
"what will be saved to the text/html files.", None))
        self.show_items_btn.setStatusTip(QApplication.translate("Status", "Show/Hide elements of Highlights. Also affects what will be saved to the text/html files.", None))
        self.show_items_btn.setText(QApplication.translate("Status", "Show in Highlights", None))
        self.act_page.setText(QApplication.translate("Status", "Page", None))
        self.act_date.setText(QApplication.translate("Status", "Date", None))
        self.act_text.setText(QApplication.translate("Status", "Highlight", None))
        self.act_comment.setText(QApplication.translate("Status", "Comment", None))

import images_rc
