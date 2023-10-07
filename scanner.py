# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
import datetime

from scan import assign_and_scan
from scan import iptoint
from PySide2 import QtWidgets
from PySide2.QtCore import *
from PySide2.QtWidgets import *


class Ui_Form(object):

    def __init__(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1050, 755)
        self.result = ""
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(190, 90, 601, 531))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 51, 16))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(330, 50, 16, 21))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 50, 16, 20))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(210, 50, 16, 20))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 50, 16, 20))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(510, 50, 16, 20))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(390, 50, 16, 20))
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(450, 50, 16, 20))
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 110, 61, 16))
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(190, 110, 16, 16))
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(420, 110, 51, 16))
        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(480, 110, 70, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10000)
        self.spinBox.setValue(100)
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(270, 150, 71, 28))
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(280, 470, 51, 28))
        self.textBrowser = QTextBrowser(self.groupBox)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 181, 561, 281))
        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(100, 50, 46, 22))
        self.spinBox_2.setMaximum(255)
        self.spinBox_2.setValue(127)
        self.spinBox_3 = QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(160, 50, 46, 22))
        self.spinBox_3.setMaximum(255)
        self.spinBox_4 = QSpinBox(self.groupBox)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setGeometry(QRect(220, 50, 46, 22))
        self.spinBox_4.setMaximum(255)
        self.spinBox_5 = QSpinBox(self.groupBox)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setGeometry(QRect(280, 50, 46, 22))
        self.spinBox_5.setMaximum(255)
        self.spinBox_5.setValue(1)
        self.spinBox_6 = QSpinBox(self.groupBox)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setGeometry(QRect(340, 50, 46, 22))
        self.spinBox_6.setMaximum(255)
        self.spinBox_6.setValue(127)
        self.spinBox_7 = QSpinBox(self.groupBox)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setGeometry(QRect(400, 50, 46, 22))
        self.spinBox_7.setMaximum(255)
        self.spinBox_8 = QSpinBox(self.groupBox)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setGeometry(QRect(460, 50, 46, 22))
        self.spinBox_8.setMaximum(255)
        self.spinBox_9 = QSpinBox(self.groupBox)
        self.spinBox_9.setObjectName(u"spinBox_9")
        self.spinBox_9.setGeometry(QRect(520, 50, 46, 22))
        self.spinBox_9.setMaximum(255)
        self.spinBox_9.setValue(1)
        self.spinBox_10 = QSpinBox(self.groupBox)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setGeometry(QRect(120, 110, 61, 22))
        self.spinBox_10.setMinimum(1)
        self.spinBox_10.setMaximum(65535)
        self.spinBox_11 = QSpinBox(self.groupBox)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setGeometry(QRect(210, 110, 61, 22))
        self.spinBox_11.setMinimum(1)
        self.spinBox_11.setMaximum(65535)
        self.spinBox_11.setValue(1000)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.start)
        self.pushButton.show()
        self.pushButton_2.clicked.connect(self.save)
        self.pushButton_2.setEnabled(False)
        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u7aef\u53e3\u626b\u63cf", None))
        self.label.setText(QCoreApplication.translate("Form", u"ip\u8303\u56f4", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_3.setText(QCoreApplication.translate("Form", u".", None))
        self.label_4.setText(QCoreApplication.translate("Form", u".", None))
        self.label_5.setText(QCoreApplication.translate("Form", u".", None))
        self.label_6.setText(QCoreApplication.translate("Form", u".", None))
        self.label_7.setText(QCoreApplication.translate("Form", u".", None))
        self.label_8.setText(QCoreApplication.translate("Form", u".", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u7aef\u53e3\u8303\u56f4", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u7ebf\u7a0b\u6570", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u626b\u63cf", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
    # retranslateUi

    def start(self):
        start_ip = "%d.%d.%d.%d"%(self.spinBox_2.value(), self.spinBox_3.value(), self.spinBox_4.value(), self.spinBox_5.value())
        end_ip = "%d.%d.%d.%d"%(self.spinBox_6.value(), self.spinBox_7.value(), self.spinBox_8.value(), self.spinBox_9.value())
        start_port = self.spinBox_10.value()
        end_port = self.spinBox_11.value()
        num_thread = self.spinBox.value()
        if iptoint(start_ip) > iptoint(end_ip) or start_port > end_port:
            self.textBrowser.setText("输入不符合要求。\n")
        else:
            self.pushButton.setEnabled(False)
            self.result = assign_and_scan(start_ip, end_ip, start_port, end_port, num_thread)
            self.textBrowser.setText("扫描完成，打开的端口如下所示：\n" + self.result)
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
    # def start(self):
    #     start_ip = "%d.%d.%d.%d"%(self.spinBox_2.value(), self.spinBox_3.value(), self.spinBox_4.value(), self.spinBox_5.value())
    #     end_ip = "%d.%d.%d.%d"%(self.spinBox_6.value(), self.spinBox_7.value(), self.spinBox_8.value(), self.spinBox_9.value())
    #     start_port = self.spinBox_10.value()
    #     end_port = self.spinBox_11.value()
    #     num_thread = self.spinBox.value()
    #     self.result = assign_and_scan(start_ip, end_ip, start_port, end_port, num_thread, self.textBrowser)
    #     # self.textBrowser.setText("扫描完成，打开的端口如下所示：\n" + self.result)
    #     self.pushButton_2.setEnabled(True)

    def save(self):
        with open("scan_result/result" + datetime.datetime.now().strftime("%Y-%m-%d#%H#%M#%S"), "wb") as f:
            f.write(self.result.encode())
            self.textBrowser.setText("保存成功。")
            self.pushButton_2.setEnabled(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
