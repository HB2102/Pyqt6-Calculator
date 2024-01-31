# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(250, 300)
        Form.setMinimumSize(QtCore.QSize(250, 300))
        Form.setMaximumSize(QtCore.QSize(500, 300))
        Form.setStyleSheet("background-color:#1B262C;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input1 = QtWidgets.QLineEdit(parent=Form)
        self.input1.setMinimumSize(QtCore.QSize(0, 30))
        self.input1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input1.setStyleSheet("color:black;\n"
                                  "background-color:#EEEEEE;\n"
                                  "border-radius: 5px;\n"
                                  "padding-left:10px;")
        self.intvalid = QtGui.QIntValidator()
        self.input1.setText("")
        self.input1.setObjectName("input1")
        self.input1.setValidator(self.intvalid)
        self.verticalLayout.addWidget(self.input1)
        self.input2 = QtWidgets.QLineEdit(parent=Form)
        self.input2.setMinimumSize(QtCore.QSize(0, 30))
        self.input2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.input2.setStyleSheet("color:black;\n"
                                  "background-color:#EEEEEE;\n"
                                  "border-radius: 5px;\n"
                                  "padding-left:10px;")
        self.input2.setObjectName("input2")
        self.input2.setValidator(self.intvalid)
        self.verticalLayout.addWidget(self.input2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.add = QtWidgets.QPushButton(parent=Form)
        self.add.setMinimumSize(QtCore.QSize(0, 30))
        self.add.setStyleSheet("background-color:#0F4C75;\n"
                               "")
        self.add.setObjectName("add")
        self.horizontalLayout_7.addWidget(self.add)
        self.sub = QtWidgets.QPushButton(parent=Form)
        self.sub.setMinimumSize(QtCore.QSize(0, 30))
        self.sub.setStyleSheet("background-color:#0F4C75;")
        self.sub.setObjectName("sub")
        self.horizontalLayout_7.addWidget(self.sub)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.mul = QtWidgets.QPushButton(parent=Form)
        self.mul.setMinimumSize(QtCore.QSize(0, 30))
        self.mul.setStyleSheet("background-color:#0F4C75;")
        self.mul.setObjectName("mul")
        self.horizontalLayout_8.addWidget(self.mul)
        self.dev = QtWidgets.QPushButton(parent=Form)
        self.dev.setMinimumSize(QtCore.QSize(0, 30))
        self.dev.setStyleSheet("background-color:#0F4C75;")
        self.dev.setObjectName("dev")
        self.horizontalLayout_8.addWidget(self.dev)
        self.mod = QtWidgets.QPushButton(parent=Form)
        self.mod.setMinimumSize(QtCore.QSize(0, 30))
        self.mod.setStyleSheet("background-color:#0F4C75;")
        self.mod.setObjectName("mod")
        self.horizontalLayout_8.addWidget(self.mod)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.min = QtWidgets.QPushButton(parent=Form)
        self.min.setMinimumSize(QtCore.QSize(0, 30))
        self.min.setStyleSheet("background-color:#0F4C75;")
        self.min.setObjectName("min")
        self.horizontalLayout_9.addWidget(self.min)
        self.max = QtWidgets.QPushButton(parent=Form)
        self.max.setMinimumSize(QtCore.QSize(0, 30))
        self.max.setStyleSheet("background-color:#0F4C75;")
        self.max.setObjectName("max")
        self.horizontalLayout_9.addWidget(self.max)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.ave = QtWidgets.QPushButton(parent=Form)
        self.ave.setMinimumSize(QtCore.QSize(0, 30))
        self.ave.setStyleSheet("background-color:#0F4C75;")
        self.ave.setObjectName("ave")
        self.horizontalLayout_10.addWidget(self.ave)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.output = QtWidgets.QLineEdit(parent=Form)
        self.output.setMinimumSize(QtCore.QSize(0, 30))
        self.output.setMaximumSize(QtCore.QSize(16777215, 30))
        self.output.setStyleSheet("color:black;\n"
                                  "background-color:#EEEEEE;\n"
                                  "border-radius: 5px;\n"
                                  "padding-left:10px;")
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.output)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "My Calculator"))
        self.input1.setPlaceholderText(_translate("Form", "Input 1"))
        self.input2.setPlaceholderText(_translate("Form", "Input 2"))
        self.add.setText(_translate("Form", "+"))
        self.sub.setText(_translate("Form", "-"))
        self.mul.setText(_translate("Form", "*"))
        self.dev.setText(_translate("Form", "/"))
        self.mod.setText(_translate("Form", "%"))
        self.min.setText(_translate("Form", "min"))
        self.max.setText(_translate("Form", "max"))
        self.ave.setText(_translate("Form", "average"))
        self.output.setPlaceholderText(_translate("Form", "OUTPUT"))








if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec())
