# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayitekrani.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(666, 621)
        font = QtGui.QFont()
        font.setPointSize(8)
        Form.setFont(font)
        self.label_soyad = QtWidgets.QLabel(Form)
        self.label_soyad.setGeometry(QtCore.QRect(50, 180, 55, 16))
        self.label_soyad.setObjectName("label_soyad")
        self.label_ad = QtWidgets.QLabel(Form)
        self.label_ad.setGeometry(QtCore.QRect(50, 140, 55, 16))
        self.label_ad.setObjectName("label_ad")
        self.label_kAd = QtWidgets.QLabel(Form)
        self.label_kAd.setGeometry(QtCore.QRect(50, 220, 71, 16))
        self.label_kAd.setObjectName("label_kAd")
        self.label_telefon = QtWidgets.QLabel(Form)
        self.label_telefon.setGeometry(QtCore.QRect(50, 340, 55, 16))
        self.label_telefon.setObjectName("label_telefon")
        self.label_TC = QtWidgets.QLabel(Form)
        self.label_TC.setGeometry(QtCore.QRect(50, 300, 81, 16))
        self.label_TC.setObjectName("label_TC")
        self.label_email = QtWidgets.QLabel(Form)
        self.label_email.setGeometry(QtCore.QRect(50, 420, 55, 16))
        self.label_email.setObjectName("label_email")
        self.label_adres = QtWidgets.QLabel(Form)
        self.label_adres.setGeometry(QtCore.QRect(50, 380, 55, 16))
        self.label_adres.setObjectName("label_adres")
        self.label_parola = QtWidgets.QLabel(Form)
        self.label_parola.setGeometry(QtCore.QRect(50, 260, 55, 16))
        self.label_parola.setObjectName("label_parola")
        self.lineEdit_ad = QtWidgets.QLineEdit(Form)
        self.lineEdit_ad.setGeometry(QtCore.QRect(170, 140, 113, 22))
        self.lineEdit_ad.setObjectName("lineEdit_ad")
        self.lineEdit_soyad = QtWidgets.QLineEdit(Form)
        self.lineEdit_soyad.setGeometry(QtCore.QRect(170, 180, 113, 22))
        self.lineEdit_soyad.setObjectName("lineEdit_soyad")
        self.lineEdit_kAd = QtWidgets.QLineEdit(Form)
        self.lineEdit_kAd.setGeometry(QtCore.QRect(170, 220, 113, 22))
        self.lineEdit_kAd.setObjectName("lineEdit_kAd")
        self.lineEdit_parola = QtWidgets.QLineEdit(Form)
        self.lineEdit_parola.setGeometry(QtCore.QRect(170, 260, 113, 22))
        self.lineEdit_parola.setObjectName("lineEdit_parola")
        self.lineEdit_TC = QtWidgets.QLineEdit(Form)
        self.lineEdit_TC.setGeometry(QtCore.QRect(170, 300, 113, 22))
        self.lineEdit_TC.setObjectName("lineEdit_TC")
        self.lineEdit_telefon = QtWidgets.QLineEdit(Form)
        self.lineEdit_telefon.setGeometry(QtCore.QRect(170, 340, 113, 22))
        self.lineEdit_telefon.setObjectName("lineEdit_telefon")
        self.lineEdit_adres = QtWidgets.QLineEdit(Form)
        self.lineEdit_adres.setGeometry(QtCore.QRect(170, 380, 113, 22))
        self.lineEdit_adres.setObjectName("lineEdit_adres")
        self.lineEdit_email = QtWidgets.QLineEdit(Form)
        self.lineEdit_email.setGeometry(QtCore.QRect(170, 420, 113, 22))
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.pushButton_kaydol = QtWidgets.QPushButton(Form)
        self.pushButton_kaydol.setGeometry(QtCore.QRect(270, 510, 111, 41))
        self.pushButton_kaydol.setObjectName("pushButton_kaydol")
        self.label_baslik = QtWidgets.QLabel(Form)
        self.label_baslik.setGeometry(QtCore.QRect(270, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_baslik.setFont(font)
        self.label_baslik.setObjectName("label_baslik")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_soyad.setText(_translate("Form", "Soyad:"))
        self.label_ad.setText(_translate("Form", "Ad:"))
        self.label_kAd.setText(_translate("Form", "Kullanıcı Adı:"))
        self.label_telefon.setText(_translate("Form", "Telefon:"))
        self.label_TC.setText(_translate("Form", "TC Kimlik No:"))
        self.label_email.setText(_translate("Form", "E-mail:"))
        self.label_adres.setText(_translate("Form", "Adres:"))
        self.label_parola.setText(_translate("Form", "Parola:"))
        self.pushButton_kaydol.setText(_translate("Form", "KAYDOL"))
        self.label_baslik.setText(_translate("Form", " Kayıt Ekranı"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
