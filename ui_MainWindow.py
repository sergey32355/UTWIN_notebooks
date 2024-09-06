# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowJLNwqn.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_ui_MainWindow(object):
    def setupUi(self, ui_MainWindow):
        if not ui_MainWindow.objectName():
            ui_MainWindow.setObjectName(u"ui_MainWindow")
        ui_MainWindow.resize(964, 809)
        self.centralwidget = QWidget(ui_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 961, 711))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.horizontalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 321, 681))
        self.horizontalLayoutWidget_2 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 20, 321, 621))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.horizontalLayoutWidget_2)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout_2.addWidget(self.listWidget)

        self.OpenInpProjectButton = QPushButton(self.groupBox)
        self.OpenInpProjectButton.setObjectName(u"OpenInpProjectButton")
        self.OpenInpProjectButton.setGeometry(QRect(0, 640, 81, 41))
        self.ListOptionsCombo = QComboBox(self.groupBox)
        self.ListOptionsCombo.addItem("")
        self.ListOptionsCombo.setObjectName(u"ListOptionsCombo")
        self.ListOptionsCombo.setGeometry(QRect(160, 645, 151, 31))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(83, 653, 81, 16))
        self.verticalLayoutWidget = QWidget(self.tab)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(320, 20, 631, 661))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayoutWidget_3 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(0, 0, 621, 291))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_4 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(0, 290, 621, 301))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.OpenInpProjectButton_2 = QPushButton(self.tab_3)
        self.OpenInpProjectButton_2.setObjectName(u"OpenInpProjectButton_2")
        self.OpenInpProjectButton_2.setGeometry(QRect(-2, 590, 121, 41))
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")

        self.verticalLayout.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        self.ExitButton = QPushButton(self.centralwidget)
        self.ExitButton.setObjectName(u"ExitButton")
        self.ExitButton.setGeometry(QRect(890, 710, 75, 51))
        ui_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ui_MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 964, 22))
        ui_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ui_MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        ui_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ui_MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ui_MainWindow)
    # setupUi

    def retranslateUi(self, ui_MainWindow):
        ui_MainWindow.setWindowTitle(QCoreApplication.translate("ui_MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("ui_MainWindow", u"Element list", None))
        self.OpenInpProjectButton.setText(QCoreApplication.translate("ui_MainWindow", u"Open file", None))
        self.ListOptionsCombo.setItemText(0, QCoreApplication.translate("ui_MainWindow", u"Conduits", None))

        self.label.setText(QCoreApplication.translate("ui_MainWindow", u"Show options:", None))
        self.OpenInpProjectButton_2.setText(QCoreApplication.translate("ui_MainWindow", u"Show graph in figure", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("ui_MainWindow", u"Graph overview", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("ui_MainWindow", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ui_MainWindow", u"\".inp\" Projects", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("ui_MainWindow", u"Tab 2", None))
        self.ExitButton.setText(QCoreApplication.translate("ui_MainWindow", u"Exit", None))
    # retranslateUi

