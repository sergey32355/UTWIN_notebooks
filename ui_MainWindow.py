# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowERhSsm.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QVBoxLayout,
    QWidget)

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
        self.verticalLayoutWidget.setGeometry(QRect(320, 100, 631, 581))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayoutWidget_3 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(0, 0, 621, 251))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_4 = QWidget(self.tab_3)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(0, 250, 621, 261))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.OpenInpProjectButton_3 = QPushButton(self.tab_3)
        self.OpenInpProjectButton_3.setObjectName(u"OpenInpProjectButton_3")
        self.OpenInpProjectButton_3.setGeometry(QRect(120, 590, 121, 41))
        self.OpenInpProjectButton_2 = QPushButton(self.tab_3)
        self.OpenInpProjectButton_2.setObjectName(u"OpenInpProjectButton_2")
        self.OpenInpProjectButton_2.setGeometry(QRect(0, 510, 131, 41))
        self.Listallnodes_btnclick = QPushButton(self.tab_3)
        self.Listallnodes_btnclick.setObjectName(u"Listallnodes_btnclick")
        self.Listallnodes_btnclick.setGeometry(QRect(130, 510, 111, 41))
        self.ListOptionsCombo_2 = QComboBox(self.tab_3)
        self.ListOptionsCombo_2.addItem("")
        self.ListOptionsCombo_2.addItem("")
        self.ListOptionsCombo_2.addItem("")
        self.ListOptionsCombo_2.addItem("")
        self.ListOptionsCombo_2.setObjectName(u"ListOptionsCombo_2")
        self.ListOptionsCombo_2.setGeometry(QRect(240, 516, 151, 31))
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.WNTR_show_elevations_pushButton_4 = QPushButton(self.tab_7)
        self.WNTR_show_elevations_pushButton_4.setObjectName(u"WNTR_show_elevations_pushButton_4")
        self.WNTR_show_elevations_pushButton_4.setGeometry(QRect(0, 500, 101, 41))
        self.WNTR_show_popiulation_pushButton_5 = QPushButton(self.tab_7)
        self.WNTR_show_popiulation_pushButton_5.setObjectName(u"WNTR_show_popiulation_pushButton_5")
        self.WNTR_show_popiulation_pushButton_5.setGeometry(QRect(100, 500, 101, 41))
        self.groupBox_3 = QGroupBox(self.tab_7)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 0, 621, 71))
        self.WNTR_list_WNTR_SHOW_RESULTSpushButton_7 = QPushButton(self.groupBox_3)
        self.WNTR_list_WNTR_SHOW_RESULTSpushButton_7.setObjectName(u"WNTR_list_WNTR_SHOW_RESULTSpushButton_7")
        self.WNTR_list_WNTR_SHOW_RESULTSpushButton_7.setGeometry(QRect(0, 20, 101, 41))
        self.WNTR_nodes_list_combo = QComboBox(self.groupBox_3)
        self.WNTR_nodes_list_combo.setObjectName(u"WNTR_nodes_list_combo")
        self.WNTR_nodes_list_combo.setGeometry(QRect(110, 40, 231, 22))
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 20, 49, 16))
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(360, 20, 49, 16))
        self.WNTR_links_list_combo = QComboBox(self.groupBox_3)
        self.WNTR_links_list_combo.setObjectName(u"WNTR_links_list_combo")
        self.WNTR_links_list_combo.setGeometry(QRect(360, 40, 241, 22))
        self.groupBox_4 = QGroupBox(self.tab_7)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 70, 621, 71))
        self.WNTRShowMapForTimeStamp_click = QPushButton(self.groupBox_4)
        self.WNTRShowMapForTimeStamp_click.setObjectName(u"WNTRShowMapForTimeStamp_click")
        self.WNTRShowMapForTimeStamp_click.setGeometry(QRect(0, 20, 101, 41))
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 20, 71, 16))
        self.WNTR_SimSteps_text_box_2 = QLineEdit(self.groupBox_4)
        self.WNTR_SimSteps_text_box_2.setObjectName(u"WNTR_SimSteps_text_box_2")
        self.WNTR_SimSteps_text_box_2.setGeometry(QRect(180, 20, 61, 22))
        self.Savealldatacheckbox_2 = QCheckBox(self.groupBox_4)
        self.Savealldatacheckbox_2.setObjectName(u"Savealldatacheckbox_2")
        self.Savealldatacheckbox_2.setGeometry(QRect(110, 40, 71, 20))
        self.Savealldatacheckbox_3 = QCheckBox(self.groupBox_4)
        self.Savealldatacheckbox_3.setObjectName(u"Savealldatacheckbox_3")
        self.Savealldatacheckbox_3.setGeometry(QRect(180, 40, 71, 20))
        self.groupBox_5 = QGroupBox(self.tab_7)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(0, 430, 621, 71))
        self.WNTR_simulate_pushButton_3 = QPushButton(self.groupBox_5)
        self.WNTR_simulate_pushButton_3.setObjectName(u"WNTR_simulate_pushButton_3")
        self.WNTR_simulate_pushButton_3.setGeometry(QRect(0, 20, 91, 41))
        self.groupBox_6 = QGroupBox(self.tab_7)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(0, 360, 621, 71))
        self.WNTR_waterintakeflag = QCheckBox(self.groupBox_6)
        self.WNTR_waterintakeflag.setObjectName(u"WNTR_waterintakeflag")
        self.WNTR_waterintakeflag.setGeometry(QRect(10, 20, 121, 20))
        self.label_7 = QLabel(self.groupBox_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 45, 49, 16))
        self.comboBox = QComboBox(self.groupBox_6)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(60, 40, 151, 22))
        self.label_8 = QLabel(self.groupBox_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(220, 20, 49, 16))
        self.comboBox_2 = QComboBox(self.groupBox_6)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(220, 40, 61, 22))
        self.label_9 = QLabel(self.groupBox_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(300, 20, 191, 16))
        self.WNTR_SimSave_text_box_3 = QLineEdit(self.groupBox_6)
        self.WNTR_SimSave_text_box_3.setObjectName(u"WNTR_SimSave_text_box_3")
        self.WNTR_SimSave_text_box_3.setGeometry(QRect(300, 40, 301, 21))
        self.groupBox_7 = QGroupBox(self.tab_7)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(0, 290, 621, 71))
        self.Savealldatacheckbox = QCheckBox(self.groupBox_7)
        self.Savealldatacheckbox.setObjectName(u"Savealldatacheckbox")
        self.Savealldatacheckbox.setGeometry(QRect(10, 20, 121, 20))
        self.WNTR_SimSave_text_box_2 = QLineEdit(self.groupBox_7)
        self.WNTR_SimSave_text_box_2.setObjectName(u"WNTR_SimSave_text_box_2")
        self.WNTR_SimSave_text_box_2.setGeometry(QRect(10, 41, 521, 21))
        self.WNTR_save_path_browse_pushButton_6 = QPushButton(self.groupBox_7)
        self.WNTR_save_path_browse_pushButton_6.setObjectName(u"WNTR_save_path_browse_pushButton_6")
        self.WNTR_save_path_browse_pushButton_6.setGeometry(QRect(540, 30, 71, 31))
        self.WNTR_list_WNTR_NODES_AND_PIPES_pushButton_6 = QPushButton(self.tab_7)
        self.WNTR_list_WNTR_NODES_AND_PIPES_pushButton_6.setObjectName(u"WNTR_list_WNTR_NODES_AND_PIPES_pushButton_6")
        self.WNTR_list_WNTR_NODES_AND_PIPES_pushButton_6.setGeometry(QRect(200, 500, 101, 41))
        self.groupBox_8 = QGroupBox(self.tab_7)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(0, 220, 621, 71))
        self.WNTR_MaxRain_values_text_box_4 = QLineEdit(self.groupBox_8)
        self.WNTR_MaxRain_values_text_box_4.setObjectName(u"WNTR_MaxRain_values_text_box_4")
        self.WNTR_MaxRain_values_text_box_4.setGeometry(QRect(100, 18, 81, 21))
        self.label_10 = QLabel(self.groupBox_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 20, 101, 16))
        self.label_11 = QLabel(self.groupBox_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 50, 101, 16))
        self.WNTR_SimSave_text_box_5 = QLineEdit(self.groupBox_8)
        self.WNTR_SimSave_text_box_5.setObjectName(u"WNTR_SimSave_text_box_5")
        self.WNTR_SimSave_text_box_5.setGeometry(QRect(100, 46, 81, 20))
        self.tabWidget_2.addTab(self.tab_7, "")

        self.verticalLayout.addWidget(self.tabWidget_2)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(320, 10, 631, 91))
        self.SimSteps_text_box = QLineEdit(self.groupBox_2)
        self.SimSteps_text_box.setObjectName(u"SimSteps_text_box")
        self.SimSteps_text_box.setGeometry(QRect(53, 20, 51, 22))
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 23, 61, 16))
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 23, 101, 16))
        self.Pywr_duration_units_combo = QComboBox(self.groupBox_2)
        self.Pywr_duration_units_combo.addItem("")
        self.Pywr_duration_units_combo.addItem("")
        self.Pywr_duration_units_combo.addItem("")
        self.Pywr_duration_units_combo.setObjectName(u"Pywr_duration_units_combo")
        self.Pywr_duration_units_combo.setGeometry(QRect(180, 20, 61, 22))
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
        self.tabWidget_2.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(ui_MainWindow)
    # setupUi

    def retranslateUi(self, ui_MainWindow):
        ui_MainWindow.setWindowTitle(QCoreApplication.translate("ui_MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("ui_MainWindow", u"Element list", None))
        self.OpenInpProjectButton.setText(QCoreApplication.translate("ui_MainWindow", u"Open file", None))
        self.ListOptionsCombo.setItemText(0, QCoreApplication.translate("ui_MainWindow", u"Conduits", None))

        self.label.setText(QCoreApplication.translate("ui_MainWindow", u"Show options:", None))
        self.OpenInpProjectButton_3.setText(QCoreApplication.translate("ui_MainWindow", u"Reserved", None))
        self.OpenInpProjectButton_2.setText(QCoreApplication.translate("ui_MainWindow", u"Show graph in figure", None))
        self.Listallnodes_btnclick.setText(QCoreApplication.translate("ui_MainWindow", u"Show elements list", None))
        self.ListOptionsCombo_2.setItemText(0, QCoreApplication.translate("ui_MainWindow", u"Conduits", None))
        self.ListOptionsCombo_2.setItemText(1, QCoreApplication.translate("ui_MainWindow", u"Junctions", None))
        self.ListOptionsCombo_2.setItemText(2, QCoreApplication.translate("ui_MainWindow", u"Nodes", None))
        self.ListOptionsCombo_2.setItemText(3, QCoreApplication.translate("ui_MainWindow", u"Storages", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("ui_MainWindow", u"Graph overview", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("ui_MainWindow", u"SimulationS", None))
        self.WNTR_show_elevations_pushButton_4.setText(QCoreApplication.translate("ui_MainWindow", u"Show elevantions", None))
        self.WNTR_show_popiulation_pushButton_5.setText(QCoreApplication.translate("ui_MainWindow", u"Show population", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ui_MainWindow", u"Show results for node/link", None))
        self.WNTR_list_WNTR_SHOW_RESULTSpushButton_7.setText(QCoreApplication.translate("ui_MainWindow", u"Show", None))
        self.label_4.setText(QCoreApplication.translate("ui_MainWindow", u"Node", None))
        self.label_5.setText(QCoreApplication.translate("ui_MainWindow", u"Link", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("ui_MainWindow", u"Show map for timestamp", None))
        self.WNTRShowMapForTimeStamp_click.setText(QCoreApplication.translate("ui_MainWindow", u"Show", None))
        self.label_6.setText(QCoreApplication.translate("ui_MainWindow", u"Time stamp:", None))
        self.WNTR_SimSteps_text_box_2.setText(QCoreApplication.translate("ui_MainWindow", u"5000", None))
        self.Savealldatacheckbox_2.setText(QCoreApplication.translate("ui_MainWindow", u"Junctions", None))
        self.Savealldatacheckbox_3.setText(QCoreApplication.translate("ui_MainWindow", u"Pipes", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("ui_MainWindow", u"Show map for timestamp", None))
        self.WNTR_simulate_pushButton_3.setText(QCoreApplication.translate("ui_MainWindow", u"Simulate", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("ui_MainWindow", u"Water input for simulation", None))
        self.WNTR_waterintakeflag.setText(QCoreApplication.translate("ui_MainWindow", u"Add water intake", None))
        self.label_7.setText(QCoreApplication.translate("ui_MainWindow", u"Scenario", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("ui_MainWindow", u"Clouds", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("ui_MainWindow", u"Clouds+terrain", None))

        self.label_8.setText(QCoreApplication.translate("ui_MainWindow", u"Nodes", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("ui_MainWindow", u"All", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("ui_MainWindow", u"Specific", None))

        self.label_9.setText(QCoreApplication.translate("ui_MainWindow", u"Specific nodes (use \",\" as separator)", None))
        self.WNTR_SimSave_text_box_3.setText(QCoreApplication.translate("ui_MainWindow", u"C:\\Tmp", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("ui_MainWindow", u"Water input for simulation", None))
        self.Savealldatacheckbox.setText(QCoreApplication.translate("ui_MainWindow", u"Save all data", None))
        self.WNTR_SimSave_text_box_2.setText(QCoreApplication.translate("ui_MainWindow", u"C:\\Tmp", None))
        self.WNTR_save_path_browse_pushButton_6.setText(QCoreApplication.translate("ui_MainWindow", u"Browse", None))
        self.WNTR_list_WNTR_NODES_AND_PIPES_pushButton_6.setText(QCoreApplication.translate("ui_MainWindow", u"List wntr nodes", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("ui_MainWindow", u"Additional inputs", None))
        self.WNTR_MaxRain_values_text_box_4.setText(QCoreApplication.translate("ui_MainWindow", u"0.76", None))
        self.label_10.setText(QCoreApplication.translate("ui_MainWindow", u"Max h for clouds:", None))
        self.label_11.setText(QCoreApplication.translate("ui_MainWindow", u"Max h for terrain:", None))
        self.WNTR_SimSave_text_box_5.setText(QCoreApplication.translate("ui_MainWindow", u"0.76", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("ui_MainWindow", u"wntr", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ui_MainWindow", u"Globals", None))
        self.SimSteps_text_box.setText(QCoreApplication.translate("ui_MainWindow", u"5000", None))
        self.label_2.setText(QCoreApplication.translate("ui_MainWindow", u"Sim.steps:", None))
        self.label_3.setText(QCoreApplication.translate("ui_MainWindow", u"Sim.step units:", None))
        self.Pywr_duration_units_combo.setItemText(0, QCoreApplication.translate("ui_MainWindow", u"sec", None))
        self.Pywr_duration_units_combo.setItemText(1, QCoreApplication.translate("ui_MainWindow", u"min", None))
        self.Pywr_duration_units_combo.setItemText(2, QCoreApplication.translate("ui_MainWindow", u"hours", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("ui_MainWindow", u"\".inp\" Projects", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("ui_MainWindow", u"Tab 2", None))
        self.ExitButton.setText(QCoreApplication.translate("ui_MainWindow", u"Exit", None))
    # retranslateUi

