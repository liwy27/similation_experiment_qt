# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_childwin.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1179, 888)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(1070, 840, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(170, 30, 400, 400))
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView_2 = QtWidgets.QGraphicsView(Form)
        self.graphicsView_2.setGeometry(QtCore.QRect(170, 460, 400, 400))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(90, 105, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spinBox.setFont(font)
        self.spinBox.setMaximum(255)
        self.spinBox.setSingleStep(10)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(Form)
        self.spinBox_2.setGeometry(QtCore.QRect(90, 145, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setMaximum(255)
        self.spinBox_2.setSingleStep(10)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(Form)
        self.spinBox_3.setGeometry(QtCore.QRect(90, 185, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spinBox_3.setFont(font)
        self.spinBox_3.setMaximum(255)
        self.spinBox_3.setSingleStep(10)
        self.spinBox_3.setObjectName("spinBox_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 105, 51, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 145, 51, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 51, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox.setGeometry(QtCore.QRect(80, 525, 85, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setMaximum(1.0)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(80, 565, 85, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.doubleSpinBox_2.setFont(font)
        self.doubleSpinBox_2.setMaximum(1.0)
        self.doubleSpinBox_2.setSingleStep(0.1)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(Form)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(80, 605, 85, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.doubleSpinBox_3.setFont(font)
        self.doubleSpinBox_3.setMaximum(1.0)
        self.doubleSpinBox_3.setSingleStep(0.1)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 530, 61, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 570, 61, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 610, 61, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(30, 440, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.graphicsView_3 = QtWidgets.QGraphicsView(Form)
        self.graphicsView_3.setGeometry(QtCore.QRect(580, 30, 400, 400))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.G2 = QtWidgets.QSpinBox(Form)
        self.G2.setGeometry(QtCore.QRect(1060, 140, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.G2.setFont(font)
        self.G2.setMaximum(255)
        self.G2.setSingleStep(10)
        self.G2.setObjectName("G2")
        self.R2 = QtWidgets.QSpinBox(Form)
        self.R2.setGeometry(QtCore.QRect(1060, 100, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.R2.setFont(font)
        self.R2.setMaximum(255)
        self.R2.setSingleStep(10)
        self.R2.setObjectName("R2")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(1000, 10, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.B2 = QtWidgets.QSpinBox(Form)
        self.B2.setGeometry(QtCore.QRect(1060, 180, 70, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B2.setFont(font)
        self.B2.setMaximum(255)
        self.B2.setSingleStep(10)
        self.B2.setObjectName("B2")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(1000, 145, 51, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(1000, 105, 51, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(1000, 190, 51, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.LineEdit_X2 = QtWidgets.QLineEdit(Form)
        self.LineEdit_X2.setGeometry(QtCore.QRect(1050, 280, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LineEdit_X2.setFont(font)
        self.LineEdit_X2.setMouseTracking(False)
        self.LineEdit_X2.setReadOnly(True)
        self.LineEdit_X2.setObjectName("LineEdit_X2")
        self.LineEdit_Y1 = QtWidgets.QLineEdit(Form)
        self.LineEdit_Y1.setGeometry(QtCore.QRect(60, 330, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LineEdit_Y1.setFont(font)
        self.LineEdit_Y1.setMouseTracking(False)
        self.LineEdit_Y1.setReadOnly(True)
        self.LineEdit_Y1.setObjectName("LineEdit_Y1")
        self.LineEdit_Y2 = QtWidgets.QLineEdit(Form)
        self.LineEdit_Y2.setGeometry(QtCore.QRect(1050, 330, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LineEdit_Y2.setFont(font)
        self.LineEdit_Y2.setMouseTracking(False)
        self.LineEdit_Y2.setReadOnly(True)
        self.LineEdit_Y2.setObjectName("LineEdit_Y2")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(30, 240, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(1010, 240, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(30, 330, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(30, 280, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(1010, 330, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(1010, 280, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.LineEdit_X1 = QtWidgets.QLineEdit(Form)
        self.LineEdit_X1.setGeometry(QtCore.QRect(60, 280, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LineEdit_X1.setFont(font)
        self.LineEdit_X1.setMouseTracking(False)
        self.LineEdit_X1.setReadOnly(True)
        self.LineEdit_X1.setObjectName("LineEdit_X1")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(20, 60, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(1000, 60, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(10, 480, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(1000, 430, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.graphicsView_4 = QtWidgets.QGraphicsView(Form)
        self.graphicsView_4.setGeometry(QtCore.QRect(580, 460, 400, 400))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.LineEdit_X4 = QtWidgets.QLineEdit(Form)
        self.LineEdit_X4.setGeometry(QtCore.QRect(1040, 720, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LineEdit_X4.setFont(font)
        self.LineEdit_X4.setMouseTracking(False)
        self.LineEdit_X4.setReadOnly(True)
        self.LineEdit_X4.setObjectName("LineEdit_X4")
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(1000, 770, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(990, 600, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(1000, 680, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.Hue = QtWidgets.QSpinBox(Form)
        self.Hue.setGeometry(QtCore.QRect(1090, 470, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Hue.setFont(font)
        self.Hue.setMaximum(359)
        self.Hue.setSingleStep(10)
        self.Hue.setObjectName("Hue")
        self.LineEdit_Y4 = QtWidgets.QLineEdit(Form)
        self.LineEdit_Y4.setGeometry(QtCore.QRect(1040, 770, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LineEdit_Y4.setFont(font)
        self.LineEdit_Y4.setMouseTracking(False)
        self.LineEdit_Y4.setReadOnly(True)
        self.LineEdit_Y4.setObjectName("LineEdit_Y4")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(1000, 720, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setGeometry(QtCore.QRect(990, 530, 101, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(Form)
        self.label_29.setGeometry(QtCore.QRect(990, 470, 81, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(20, 720, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.LineEdit_X3 = QtWidgets.QLineEdit(Form)
        self.LineEdit_X3.setGeometry(QtCore.QRect(60, 720, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LineEdit_X3.setFont(font)
        self.LineEdit_X3.setMouseTracking(False)
        self.LineEdit_X3.setReadOnly(True)
        self.LineEdit_X3.setObjectName("LineEdit_X3")
        self.label_30 = QtWidgets.QLabel(Form)
        self.label_30.setGeometry(QtCore.QRect(20, 680, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(Form)
        self.label_31.setGeometry(QtCore.QRect(20, 760, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.LineEdit_Y3 = QtWidgets.QLineEdit(Form)
        self.LineEdit_Y3.setGeometry(QtCore.QRect(60, 770, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.LineEdit_Y3.setFont(font)
        self.LineEdit_Y3.setMouseTracking(False)
        self.LineEdit_Y3.setReadOnly(True)
        self.LineEdit_Y3.setObjectName("LineEdit_Y3")
        self.label_32 = QtWidgets.QLabel(Form)
        self.label_32.setGeometry(QtCore.QRect(1010, 490, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(Form)
        self.label_33.setGeometry(QtCore.QRect(1010, 560, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(Form)
        self.label_34.setGeometry(QtCore.QRect(1010, 630, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.Sat = QtWidgets.QDoubleSpinBox(Form)
        self.Sat.setGeometry(QtCore.QRect(1090, 530, 85, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Sat.setFont(font)
        self.Sat.setMaximum(1.0)
        self.Sat.setSingleStep(0.1)
        self.Sat.setObjectName("Sat")
        self.Val = QtWidgets.QDoubleSpinBox(Form)
        self.Val.setGeometry(QtCore.QRect(1090, 600, 85, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Val.setFont(font)
        self.Val.setMaximum(1.0)
        self.Val.setSingleStep(0.1)
        self.Val.setObjectName("Val")
        self.label_35 = QtWidgets.QLabel(Form)
        self.label_35.setGeometry(QtCore.QRect(1000, 380, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe 黑体 Std R")
        font.setPointSize(16)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.delta = QtWidgets.QLineEdit(Form)
        self.delta.setGeometry(QtCore.QRect(1050, 380, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.delta.setFont(font)
        self.delta.setMouseTracking(False)
        self.delta.setReadOnly(True)
        self.delta.setObjectName("delta")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "加光/减光混色实验"))
        Form.setStatusTip(_translate("Form", "实验"))
        self.pushButton.setText(_translate("Form", "返回"))
        self.label.setText(_translate("Form", "R(红)"))
        self.label_2.setText(_translate("Form", "G(绿)"))
        self.label_3.setText(_translate("Form", "B(蓝)"))
        self.label_4.setText(_translate("Form", "青色C"))
        self.label_5.setText(_translate("Form", "品红M"))
        self.label_6.setText(_translate("Form", "黄色Y"))
        self.label_7.setText(_translate("Form", "加光混色1"))
        self.label_8.setText(_translate("Form", "减光混色"))
        self.label_10.setText(_translate("Form", "加光混色2"))
        self.label_9.setText(_translate("Form", "G(绿)"))
        self.label_11.setText(_translate("Form", "R(红)"))
        self.label_12.setText(_translate("Form", "B(蓝)"))
        self.LineEdit_X2.setText(_translate("Form", "0.0000"))
        self.LineEdit_Y1.setText(_translate("Form", "0.0000"))
        self.LineEdit_Y2.setText(_translate("Form", "0.0000"))
        self.label_14.setText(_translate("Form", "色坐标1"))
        self.label_15.setText(_translate("Form", "色坐标2"))
        self.label_16.setText(_translate("Form", "y1"))
        self.label_17.setText(_translate("Form", "x1"))
        self.label_18.setText(_translate("Form", "y2"))
        self.label_19.setText(_translate("Form", "x2"))
        self.LineEdit_X1.setText(_translate("Form", "0.0000"))
        self.label_20.setText(_translate("Form", "值域:0~255"))
        self.label_21.setText(_translate("Form", "值域:0~255"))
        self.label_22.setText(_translate("Form", "值域:0~1"))
        self.label_13.setText(_translate("Form", "HSV混色"))
        self.LineEdit_X4.setText(_translate("Form", "0.0000"))
        self.label_24.setText(_translate("Form", "y4"))
        self.label_25.setText(_translate("Form", "V(明度)"))
        self.label_26.setText(_translate("Form", "色坐标4"))
        self.LineEdit_Y4.setText(_translate("Form", "0.0000"))
        self.label_27.setText(_translate("Form", "x4"))
        self.label_28.setText(_translate("Form", "S(饱和度)"))
        self.label_29.setText(_translate("Form", "H(色调)"))
        self.label_23.setText(_translate("Form", "x3"))
        self.LineEdit_X3.setText(_translate("Form", "0.0000"))
        self.label_30.setText(_translate("Form", "色坐标3"))
        self.label_31.setText(_translate("Form", "y3"))
        self.LineEdit_Y3.setText(_translate("Form", "0.0000"))
        self.label_32.setText(_translate("Form", "0-360"))
        self.label_33.setText(_translate("Form", "0-1"))
        self.label_34.setText(_translate("Form", "0-1"))
        self.label_35.setText(_translate("Form", "色差"))
        self.delta.setText(_translate("Form", "0.0000"))
