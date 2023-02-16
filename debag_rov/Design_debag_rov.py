# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debag_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class DebagRovMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Debag_ROV")
        MainWindow.resize(622, 724)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(622, 724))
        MainWindow.setMaximumSize(QtCore.QSize(622, 724))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)

        self.lcdNumber_11 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_11.setMinimumSize(QtCore.QSize(0, 50))
        self.lcdNumber_11.setObjectName("lcdNumber_11")
        self.horizontalLayout_3.addWidget(self.lcdNumber_11)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)

        self.lcdNumber_10 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_10.setMinimumSize(QtCore.QSize(0, 50))
        self.lcdNumber_10.setObjectName("lcdNumber_10")
        self.horizontalLayout_3.addWidget(self.lcdNumber_10)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")

        self.horizontalLayout_3.addWidget(self.label_6)
        self.lcdNumber_12 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_12.setMinimumSize(QtCore.QSize(0, 50))
        self.lcdNumber_12.setObjectName("lcdNumber_12")
        self.horizontalLayout_3.addWidget(self.lcdNumber_12)

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)

        self.lcdNumber_13 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_13.setMinimumSize(QtCore.QSize(0, 50))
        self.lcdNumber_13.setObjectName("lcdNumber_13")
        self.horizontalLayout_3.addWidget(self.lcdNumber_13)

        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.checkBox_11 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_11.setChecked(True)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_2.addWidget(self.checkBox_11, 0, 4, 1, 1)

        self.checkBox_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_10.setEnabled(True)
        self.checkBox_10.setChecked(True)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_2.addWidget(self.checkBox_10, 0, 1, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(147, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)

        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setMinimumSize(QtCore.QSize(25, 100))
        self.verticalSlider_2.setMaximum(100)
        self.verticalSlider_2.setProperty("value", 50)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.gridLayout_2.addWidget(self.verticalSlider_2, 0, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(4, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 6, 1, 1)

        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setMinimumSize(QtCore.QSize(25, 100))
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setProperty("value", 50)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)

        self.checkBox_12 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_12.setChecked(True)
        self.checkBox_12.setObjectName("checkBox_12")
        self.horizontalLayout_2.addWidget(self.checkBox_12)

        self.horizontalSlider_10 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_10.setMinimumSize(QtCore.QSize(100, 30))
        self.horizontalSlider_10.setMaximum(100)
        self.horizontalSlider_10.setProperty("value", 50)
        self.horizontalSlider_10.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_10.setObjectName("horizontalSlider_10")
        self.horizontalLayout_2.addWidget(self.horizontalSlider_10)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)

        self.checkBox_13 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_13.setChecked(True)
        self.checkBox_13.setObjectName("checkBox_13")
        self.horizontalLayout_2.addWidget(self.checkBox_13)

        self.horizontalSlider_11 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_11.setMinimumSize(QtCore.QSize(100, 30))
        self.horizontalSlider_11.setMaximum(100)
        self.horizontalSlider_11.setProperty("value", 50)
        self.horizontalSlider_11.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_11.setObjectName("horizontalSlider_11")
        self.horizontalLayout_2.addWidget(self.horizontalSlider_11)

        spacerItem5 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)

        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_4.addWidget(self.pushButton_10)

        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_4.addWidget(self.pushButton_11)

        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_4.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_4.addWidget(self.pushButton_13)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 30))
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setChecked(True)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 7, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 3, 0, 1, 1)
        self.lcdNumber_8 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_8.setMinimumSize(QtCore.QSize(0, 30))
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.gridLayout.addWidget(self.lcdNumber_8, 8, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 6, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 5, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 7, 5, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 3, 1, 1)
        self.horizontalSlider_8 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_8.setMinimumSize(QtCore.QSize(150, 30))
        self.horizontalSlider_8.setMaximum(180)
        self.horizontalSlider_8.setProperty("value", 0)
        self.horizontalSlider_8.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_8.setObjectName("horizontalSlider_8")
        self.gridLayout.addWidget(self.horizontalSlider_8, 8, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 8, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 3, 5, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(150, 30))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setProperty("value", 50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 1, 4, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)
        self.horizontalSlider_6 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_6.setMinimumSize(QtCore.QSize(150, 30))
        self.horizontalSlider_6.setMaximum(100)
        self.horizontalSlider_6.setProperty("value", 50)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.gridLayout.addWidget(self.horizontalSlider_6, 6, 4, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 5, 2, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_9.setChecked(True)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 9, 0, 1, 1)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setEnabled(True)
        self.horizontalSlider_2.setMinimumSize(QtCore.QSize(150, 30))
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setProperty("value", 50)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout.addWidget(self.horizontalSlider_2, 2, 4, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 9, 2, 1, 1)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setMinimumSize(QtCore.QSize(0, 30))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout.addWidget(self.lcdNumber_3, 3, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 9, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 3, 1, 1)
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_7.setMinimumSize(QtCore.QSize(0, 30))
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.gridLayout.addWidget(self.lcdNumber_7, 7, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 6, 5, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setChecked(True)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout.addWidget(self.checkBox_8, 8, 0, 1, 1)
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setMinimumSize(QtCore.QSize(0, 30))
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.gridLayout.addWidget(self.lcdNumber_4, 4, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 8, 5, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.horizontalSlider_7 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_7.setMinimumSize(QtCore.QSize(150, 30))
        self.horizontalSlider_7.setMaximum(180)
        self.horizontalSlider_7.setProperty("value", 90)
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")
        self.gridLayout.addWidget(self.horizontalSlider_7, 7, 4, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 9, 5, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 4, 5, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 7, 2, 1, 1)
        self.horizontalSlider_5 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_5.setMinimumSize(QtCore.QSize(150, 30))
        self.horizontalSlider_5.setMaximum(100)
        self.horizontalSlider_5.setProperty("value", 50)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.gridLayout.addWidget(self.horizontalSlider_5, 5, 4, 1, 1)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_3.setMinimumSize(QtCore.QSize(150, 30))
        self.horizontalSlider_3.setMaximum(100)
        self.horizontalSlider_3.setProperty("value", 50)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.gridLayout.addWidget(self.horizontalSlider_3, 3, 4, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 8, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 7, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 3, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout.addWidget(self.lcdNumber_2, 2, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 5, 5, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setChecked(True)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 6, 0, 1, 1)
        self.horizontalSlider_9 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_9.setMinimumSize(QtCore.QSize(150, 30))
        self.horizontalSlider_9.setMaximum(100)
        self.horizontalSlider_9.setProperty("value", 0)
        self.horizontalSlider_9.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_9.setObjectName("horizontalSlider_9")
        self.gridLayout.addWidget(self.horizontalSlider_9, 9, 4, 1, 1)
        self.lcdNumber_9 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_9.setMinimumSize(QtCore.QSize(0, 30))
        self.lcdNumber_9.setObjectName("lcdNumber_9")
        self.gridLayout.addWidget(self.lcdNumber_9, 9, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 3, 1, 1)
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_6.setMinimumSize(QtCore.QSize(0, 30))
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.gridLayout.addWidget(self.lcdNumber_6, 6, 1, 1, 1)
        self.horizontalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_4.setMinimumSize(QtCore.QSize(150, 30))
        self.horizontalSlider_4.setMaximum(100)
        self.horizontalSlider_4.setProperty("value", 50)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.gridLayout.addWidget(self.horizontalSlider_4, 4, 4, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 5, 0, 1, 1)
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_5.setMinimumSize(QtCore.QSize(0, 30))
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.gridLayout.addWidget(self.lcdNumber_5, 5, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 2, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 4, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 1, 5, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 4, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 50))
        self.textBrowser.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_4.addWidget(self.textBrowser, 5, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label_4.setText(_translate("MainWindow", "Volt:"))
        self.label_5.setText(_translate("MainWindow", "Amper:"))
        self.label_6.setText(_translate("MainWindow", "Dept:"))
        self.label_7.setText(_translate("MainWindow", "Angle:"))

        self.checkBox_11.setText(_translate("MainWindow", "j2_val_y"))
        self.checkBox_10.setText(_translate("MainWindow", "j1_val_y"))
        self.checkBox_12.setText(_translate("MainWindow", "j1_val_x"))
        self.checkBox_13.setText(_translate("MainWindow", "j2_val_x"))

        self.pushButton_10.setText(_translate("MainWindow", "Home_j1_val_x"))
        self.pushButton_11.setText(_translate("MainWindow", "Home_j1_val_y"))
        self.pushButton_12.setText(_translate("MainWindow", "Home_j2_val_x"))
        self.pushButton_13.setText(_translate("MainWindow", "Home_j2_val_y"))

        self.pushButton.setText(_translate("MainWindow", "Home"))

        self.checkBox_7.setText(_translate("MainWindow", "Ser_cam"))

        self.label_8.setText(_translate("MainWindow", "0"))

        self.checkBox_3.setText(_translate("MainWindow", "Motor_2"))

        self.pushButton_6.setText(_translate("MainWindow", "Home"))

        self.label_18.setText(_translate("MainWindow", "100"))

        self.label_23.setText(_translate("MainWindow", "180"))

        self.pushButton_4.setText(_translate("MainWindow", "Home"))

        self.label.setText(_translate("MainWindow", "Amper"))

        self.label_12.setText(_translate("MainWindow", "0"))

        self.label_13.setText(_translate("MainWindow", "0"))

        self.label_15.setText(_translate("MainWindow", "0"))

        self.label_19.setText(_translate("MainWindow", "100"))

        self.checkBox.setText(_translate("MainWindow", "Motor_0"))

        self.pushButton_5.setText(_translate("MainWindow", "Home"))

        self.checkBox_9.setText(_translate("MainWindow", "Led       "))

        self.pushButton_9.setText(_translate("MainWindow", "Home"))

        self.label_16.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Power"))
        self.label_22.setText(_translate("MainWindow", "100"))
        self.checkBox_8.setText(_translate("MainWindow", "Arm        "))
        self.label_24.setText(_translate("MainWindow", "180"))
        self.pushButton_3.setText(_translate("MainWindow", "Home"))
        self.label_25.setText(_translate("MainWindow", "100"))
        self.label_20.setText(_translate("MainWindow", "100"))
        self.pushButton_7.setText(_translate("MainWindow", "Home"))
        self.pushButton_8.setText(_translate("MainWindow", "Home"))
        self.label_14.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_9.setText(_translate("MainWindow", "0"))
        self.label_21.setText(_translate("MainWindow", "100"))
        self.checkBox_6.setText(_translate("MainWindow", "Motor_5"))
        self.label_10.setText(_translate("MainWindow", "0"))
        self.checkBox_5.setText(_translate("MainWindow", "Motor_4"))
        self.pushButton_2.setText(_translate("MainWindow", "Home"))
        self.checkBox_2.setText(_translate("MainWindow", "Motor_1"))
        self.checkBox_4.setText(_translate("MainWindow", "Motor_3"))
        self.label_17.setText(_translate("MainWindow", "100"))



