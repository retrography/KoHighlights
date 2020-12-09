# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Apps\DEV\PROJECTS\KoHighlights\gui_about.ui'
#
# Created: Thu Feb  6 12:55:05 2020
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

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.setWindowModality(QtCore.Qt.ApplicationModal)
        About.resize(480, 560)
        About.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        About.setModal(False)
        self.verticalLayout = QVBoxLayout(About)
        self.verticalLayout.setObjectName("verticalLayout")
        self.about_tabs = QTabWidget(About)
        self.about_tabs.setTabShape(QTabWidget.Rounded)
        self.about_tabs.setObjectName("about_tabs")
        self.info_tab = QWidget()
        self.info_tab.setObjectName("info_tab")
        self.verticalLayout_2 = QVBoxLayout(self.info_tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_2 = QScrollArea(self.info_tab)
        self.scrollArea_2.setStyleSheet("QScrollArea {background-color:transparent;}")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 454, 485))
        self.scrollAreaWidgetContents_2.setStyleSheet("background-color:transparent;")
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setContentsMargins(6, 0, 6, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.text_lbl = QLabel(self.scrollAreaWidgetContents_2)
        self.text_lbl.setText("")
        self.text_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.text_lbl.setWordWrap(True)
        self.text_lbl.setOpenExternalLinks(True)
        self.text_lbl.setObjectName("text_lbl")
        self.verticalLayout_6.addWidget(self.text_lbl)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.about_tabs.addTab(self.info_tab, "")
        self.log_tab = QWidget()
        self.log_tab.setObjectName("log_tab")
        self.verticalLayout_8 = QVBoxLayout(self.log_tab)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.log_txt = QPlainTextEdit(self.log_tab)
        self.log_txt.setFrameShape(QFrame.WinPanel)
        self.log_txt.setDocumentTitle("")
        self.log_txt.setUndoRedoEnabled(False)
        self.log_txt.setReadOnly(True)
        self.log_txt.setPlainText("")
        self.log_txt.setObjectName("log_txt")
        self.verticalLayout_8.addWidget(self.log_txt)
        self.about_tabs.addTab(self.log_tab, "")
        self.verticalLayout.addWidget(self.about_tabs)
        self.btn_box = QFrame(About)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_box.sizePolicy().hasHeightForWidth())
        self.btn_box.setSizePolicy(sizePolicy)
        self.btn_box.setObjectName("btn_box")
        self.horizontalLayout = QHBoxLayout(self.btn_box)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.about_qt_btn = QPushButton(self.btn_box)
        self.about_qt_btn.setObjectName("about_qt_btn")
        self.horizontalLayout.addWidget(self.about_qt_btn)
        spacerItem = QSpacerItem(92, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.updates_btn = QPushButton(self.btn_box)
        self.updates_btn.setObjectName("updates_btn")
        self.horizontalLayout.addWidget(self.updates_btn)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.close_btn = QPushButton(self.btn_box)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.verticalLayout.addWidget(self.btn_box)

        self.retranslateUi(About)
        self.about_tabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.close_btn, QtCore.SIGNAL("clicked()"), About.close)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        self.about_tabs.setTabText(self.about_tabs.indexOf(self.info_tab), QApplication.translate("About", "Information", None))
        self.about_tabs.setTabText(self.about_tabs.indexOf(self.log_tab), QApplication.translate("About", "Log", None))
        self.about_qt_btn.setText(QApplication.translate("About", "About Qt", None))
        self.updates_btn.setToolTip(QApplication.translate("About", "Check online for an updated version", None))
        self.updates_btn.setText(QApplication.translate("About", "Check for Updates", None))
        self.close_btn.setText(QApplication.translate("About", "Close", None))

import images_rc
