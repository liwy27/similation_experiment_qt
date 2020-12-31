from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsPixmapItem, QGraphicsScene, QFileDialog
from main_window import Ui_MainWindow
from first_childwin import Ui_Form
from second_childwin import Ui_Form_2
from PyQt5.QtGui import QImage, QPixmap
import cv2 as cv
import os
from pandas import read_csv
import numpy as np
import math


class Mainwin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mainwin, self).__init__()
        self.setupUi(self)


class First_child(QMainWindow, Ui_Form):
    def __init__(self):
        super(First_child, self).__init__()
        self.setupUi(self)
        self.img_rgb = np.zeros((400, 400, 3), dtype=np.uint8)
        self.img_rgb2 = np.zeros((400, 400, 3), dtype=np.uint8)
        self.img_cmy = np.zeros((400, 400, 3), dtype=np.uint8)
        self.img_hsv = np.zeros((400, 400, 3), dtype=np.uint8)

        self.r = 1
        self.g = 1
        self.b = 1
        self.r2 = 1
        self.g2 = 1
        self.b2 = 1
        self.c = 0
        self.m = 0
        self.y = 0
        self.h = 0
        self.s = 0
        self.v = 0

        frame_rgb = QImage(self.img_rgb, 400, 400, QImage.Format_RGB888)
        frame_rgb2 = QImage(self.img_rgb2, 400, 400, QImage.Format_RGB888)
        frame_cmy = QImage(self.img_cmy, 400, 400, QImage.Format_RGB888)
        frame_hsv = QImage(self.img_hsv, 400, 400, QImage.Format_RGB888)

        pix_rgb = QPixmap.fromImage(frame_rgb)
        pix_rgb2 = QPixmap.fromImage(frame_rgb2)
        pix_cmy = QPixmap.fromImage(frame_cmy)
        pix_hsv = QPixmap.fromImage(frame_hsv)

        self.item_rgb = QGraphicsPixmapItem(pix_rgb)  # 创建像素图元
        self.item_rgb2 = QGraphicsPixmapItem(pix_rgb2)
        self.item_cmy = QGraphicsPixmapItem(pix_cmy)
        self.item_hsv = QGraphicsPixmapItem(pix_hsv)

        self.scene_rgb = QGraphicsScene()  # 创建场景
        self.scene_rgb2 = QGraphicsScene()
        self.scene_cmy = QGraphicsScene()  # 创建场景
        self.scene_hsv = QGraphicsScene()

        self.scene_rgb.addItem(self.item_rgb)
        self.scene_rgb2.addItem(self.item_rgb2)
        self.scene_cmy.addItem(self.item_cmy)
        self.scene_hsv.addItem(self.item_hsv)

        self.graphicsView.setScene(self.scene_rgb)
        self.graphicsView_3.setScene(self.scene_rgb2)
        self.graphicsView_2.setScene(self.scene_cmy)
        self.graphicsView_4.setScene(self.scene_hsv)

        self.spinBox.valueChanged.connect(self.run)
        self.spinBox_2.valueChanged.connect(self.run)
        self.spinBox_3.valueChanged.connect(self.run)

        self.R2.valueChanged.connect(self.run)
        self.G2.valueChanged.connect(self.run)
        self.B2.valueChanged.connect(self.run)

        self.Hue.valueChanged.connect(self.run)
        self.Sat.valueChanged.connect(self.run)
        self.Val.valueChanged.connect(self.run)

        # run 为要触发的函数
        self.doubleSpinBox.valueChanged.connect(self.run)
        self.doubleSpinBox_2.valueChanged.connect(self.run)
        self.doubleSpinBox_3.valueChanged.connect(self.run)

    def run(self):
        self.r = self.spinBox.value()
        self.g = self.spinBox_2.value()
        self.b = self.spinBox_3.value()
        self.r2 = self.R2.value()
        self.g2 = self.G2.value()
        self.b2 = self.B2.value()
        self.c = self.doubleSpinBox.value()
        self.m = self.doubleSpinBox_2.value()
        self.y = self.doubleSpinBox_3.value()
        self.h = self.Hue.value()
        self.s = self.Sat.value()
        self.v = self.Val.value()

        self.img_rgb[:, :, 0] = self.r
        self.img_rgb[:, :, 1] = self.g
        self.img_rgb[:, :, 2] = self.b

        self.img_rgb2[:, :, 0] = self.r2
        self.img_rgb2[:, :, 1] = self.g2
        self.img_rgb2[:, :, 2] = self.b2

        self.img_cmy[:, :, 0] = (1 - self.c) * 255
        self.img_cmy[:, :, 1] = (1 - self.m) * 255
        self.img_cmy[:, :, 2] = (1 - self.y) * 255

        hsv_r, hsv_g, hsv_b = self.hsv2rbg(self.h, self.s, self.v)

        self.img_hsv[:, :, 0] = hsv_r * 255
        self.img_hsv[:, :, 1] = hsv_g * 255
        self.img_hsv[:, :, 2] = hsv_b * 255

        # 计算色坐标
        x1, y1, _ = self.convert(self.r, self.g, self.b)
        x2, y2, _ = self.convert(self.r2, self.g2, self.b2)

        x3, y3, _ = self.convert((1 - self.c), (1 - self.m), (1 - self.y))
        x4, y4, _ = self.convert(hsv_r, hsv_g, hsv_b)

        d = math.sqrt(math.pow((x1-x2), 2)+math.pow((y1-y2), 2))
        d = round(d, 4)

        self.delta.setText(str(d))

        self.LineEdit_X1.setText(str(x1))
        self.LineEdit_Y1.setText(str(y1))
        self.LineEdit_X2.setText(str(x2))
        self.LineEdit_Y2.setText(str(y2))
        self.LineEdit_X3.setText(str(x3))
        self.LineEdit_Y3.setText(str(y3))
        self.LineEdit_X4.setText(str(x4))
        self.LineEdit_Y4.setText(str(y4))

        cv.putText(self.img_rgb2, "Chromatic aberration:", (10, 40),
                   cv.FONT_HERSHEY_COMPLEX_SMALL,
                   1.3,
                   (255, 255, 255),
                   2)

        cv.putText(self.img_rgb2, str(d), (10, 90),
                   cv.FONT_HERSHEY_COMPLEX_SMALL,
                   1.3,
                   (255, 255, 255),
                   2)

        frame_rgb = QImage(self.img_rgb, 400, 400, QImage.Format_RGB888)
        frame_rgb2 = QImage(self.img_rgb2, 400, 400, QImage.Format_RGB888)
        frame_cmy = QImage(self.img_cmy, 400, 400, QImage.Format_RGB888)
        frame_hsv = QImage(self.img_hsv, 400, 400, QImage.Format_RGB888)

        pix_rgb = QPixmap.fromImage(frame_rgb)
        pix_rgb2 = QPixmap.fromImage(frame_rgb2)
        pix_cmy = QPixmap.fromImage(frame_cmy)
        pix_hsv = QPixmap.fromImage(frame_hsv)

        self.item_rgb = QGraphicsPixmapItem(pix_rgb)  # 创建像素图元
        self.item_rgb2 = QGraphicsPixmapItem(pix_rgb2)
        self.item_cmy = QGraphicsPixmapItem(pix_cmy)
        self.item_hsv = QGraphicsPixmapItem(pix_hsv)

        self.scene_rgb.addItem(self.item_rgb)
        self.scene_rgb2.addItem(self.item_rgb2)
        self.scene_cmy.addItem(self.item_cmy)
        self.scene_hsv.addItem(self.item_hsv)

    def convert(self, r, g, b):
        x_0 = 0.490 * r + 0.310 * g + 0.200 * b
        y_0 = 0.117 * r + 0.812 * g + 0.010 * b
        z_0 = 0.010 * g + 0.990 * b
        x = x_0 / (x_0 + y_0 + z_0 + 0.0000000001)
        y = y_0 / (x_0 + y_0 + z_0 + 0.0000000001)
        z = z_0 / (x_0 + y_0 + z_0 + 0.0000000001)
        x = round(x, 4)
        y = round(y, 4)
        z = round(z, 4)
        return x, y, z

    def hsv2rbg(self, h, s, v):
        h_i = h // 60
        f = h / 60 - h_i
        p = v * (1 - s)
        q = v * (1 - f * s)
        t = v * (1 - (1 - f) * s)
        if h_i == 0:
            return v, t, p
        elif h_i == 1:
            return q, v, p
        elif h_i == 2:
            return p, v, t
        elif h_i == 3:
            return p, q, v
        elif h_i == 4:
            return t, p, v
        elif h_i == 5:
            return v, p, q


class Second_child(QMainWindow, Ui_Form_2):
    def __init__(self):
        super(Second_child, self).__init__()
        self.setupUi(self)
        self.img = cv.imread("pic.jpg")
        b, g, r = cv.split(self.img)  # 分解Opencv里的标准格式B、G、R
        self.img = cv.merge([r, g, b])  # 将BGR格式转化为常用的RGB格式
        frame_img = QImage(self.img, 560, 606, QImage.Format_RGB888)

        pix_img = QPixmap.fromImage(frame_img)

        self.item_img = QGraphicsPixmapItem(pix_img)  # 创建像素图元

        self.scene_img = QGraphicsScene()  # 创建场景

        self.scene_img.addItem(self.item_img)

        self.graphicsView.setScene(self.scene_img)

        self.get_filename_path = ""
        self.pushButton.clicked.connect(self.openFile)
        self.pushButton_2.clicked.connect(self.calculate)

    def openFile(self):
        path = os.getcwd()
        self.get_filename_path, ok = QFileDialog.getOpenFileName(self,
                                                            "选取单个文件",
                                                            path,
                                                            "All Files (*);;Text Files (*.txt)")
        if ok:
            # self.filePathlineEdit.setText(str(self.get_filename_path))
            self.lineEdit.setText(str(self.get_filename_path))  # self.get_filename_path 路径

    def calculate(self):
        # 读取CIE1931三刺激色响应数据
        csv_data = read_csv(r"CIE_1931.csv")
        data = csv_data.values.tolist()

        # 读取光源光谱数据，这里是溴钨灯，即A标准光源
        sorce = read_csv(r"LightSource_A.csv")
        s = sorce.values.tolist()

        # 读取样品反射谱或者透射谱数据
        sample_data = read_csv(self.get_filename_path)
        sample = sample_data.values.tolist()

        XYZ = [0, 0, 0]
        for i in range(3):
            for j in range(61):
                XYZ[i] += s[j][1] * data[j][i + 1] * sample[j][2] * 0.05

        # 归一化参数
        k = 100 / XYZ[1]

        for i in range(3):
            XYZ[i] = k * XYZ[i]

        # 计算色度坐标
        x = round(XYZ[0] / sum(XYZ), 4)
        y = round(XYZ[1] / sum(XYZ), 4)
        z = round(XYZ[2] / sum(XYZ), 4)
        img_line = self.img.copy()
        cv.line(img_line, (int(600 * x) + 54, 556 - int(600 * y) - 10), (int(600 * x) + 54, 556 - int(600 * y) + 10),
                (255, 0, 0))
        cv.line(img_line, (int(600 * x) + 54 - 10, 556 - int(600 * y)), (int(600 * x) + 54 + 10, 556 - int(600 * y)),
                (255, 0, 0))
        cv.line(img_line, (int(600 * x) + 54, 556 - int(600 * y)), (323, 311), (255, 0, 0), thickness=1, lineType=4)

        frame_img = QImage(img_line, 560, 606, QImage.Format_RGB888)

        pix_img = QPixmap.fromImage(frame_img)

        self.item_img = QGraphicsPixmapItem(pix_img)  # 创建像素图元

        self.scene_img.addItem(self.item_img)
        self.graphicsView.setScene(self.scene_img)

        self.lineEdit_2.setText(str(x))
        self.lineEdit_3.setText(str(y))
        self.lineEdit_4.setText(str(z))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main = Mainwin()
    main.show()

    child_1 = First_child()
    child_2 = Second_child()

    btn = main.pushButton
    btn.clicked.connect(child_1.show)

    btn_2 = main.pushButton_2
    btn_2.clicked.connect(child_2.show)

    sys.exit(app.exec_())
