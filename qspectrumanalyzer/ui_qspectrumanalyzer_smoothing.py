# Form implementation generated from reading ui file 'qspectrumanalyzer_smoothing.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_QSpectrumAnalyzerSmoothing(object):
    def setupUi(self, QSpectrumAnalyzerSmoothing):
        QSpectrumAnalyzerSmoothing.setObjectName("QSpectrumAnalyzerSmoothing")
        QSpectrumAnalyzerSmoothing.resize(250, 130)
        self.verticalLayout = QtWidgets.QVBoxLayout(QSpectrumAnalyzerSmoothing)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(QSpectrumAnalyzerSmoothing)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.windowFunctionComboBox = QtWidgets.QComboBox(QSpectrumAnalyzerSmoothing)
        self.windowFunctionComboBox.setObjectName("windowFunctionComboBox")
        self.windowFunctionComboBox.addItem("")
        self.windowFunctionComboBox.addItem("")
        self.windowFunctionComboBox.addItem("")
        self.windowFunctionComboBox.addItem("")
        self.windowFunctionComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.windowFunctionComboBox)
        self.label_2 = QtWidgets.QLabel(QSpectrumAnalyzerSmoothing)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.windowLengthSpinBox = QtWidgets.QSpinBox(QSpectrumAnalyzerSmoothing)
        self.windowLengthSpinBox.setMinimum(3)
        self.windowLengthSpinBox.setMaximum(1001)
        self.windowLengthSpinBox.setProperty("value", 11)
        self.windowLengthSpinBox.setObjectName("windowLengthSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.windowLengthSpinBox)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(QSpectrumAnalyzerSmoothing)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.windowFunctionComboBox)
        self.label_2.setBuddy(self.windowLengthSpinBox)

        self.retranslateUi(QSpectrumAnalyzerSmoothing)
        self.windowFunctionComboBox.setCurrentIndex(1)
        self.buttonBox.accepted.connect(QSpectrumAnalyzerSmoothing.accept) # type: ignore
        self.buttonBox.rejected.connect(QSpectrumAnalyzerSmoothing.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(QSpectrumAnalyzerSmoothing)
        QSpectrumAnalyzerSmoothing.setTabOrder(self.windowFunctionComboBox, self.windowLengthSpinBox)
        QSpectrumAnalyzerSmoothing.setTabOrder(self.windowLengthSpinBox, self.buttonBox)

    def retranslateUi(self, QSpectrumAnalyzerSmoothing):
        _translate = QtCore.QCoreApplication.translate
        QSpectrumAnalyzerSmoothing.setWindowTitle(_translate("QSpectrumAnalyzerSmoothing", "Smoothing - QSpectrumAnalyzer"))
        self.label.setText(_translate("QSpectrumAnalyzerSmoothing", "&Window function:"))
        self.windowFunctionComboBox.setItemText(0, _translate("QSpectrumAnalyzerSmoothing", "rectangular"))
        self.windowFunctionComboBox.setItemText(1, _translate("QSpectrumAnalyzerSmoothing", "hanning"))
        self.windowFunctionComboBox.setItemText(2, _translate("QSpectrumAnalyzerSmoothing", "hamming"))
        self.windowFunctionComboBox.setItemText(3, _translate("QSpectrumAnalyzerSmoothing", "bartlett"))
        self.windowFunctionComboBox.setItemText(4, _translate("QSpectrumAnalyzerSmoothing", "blackman"))
        self.label_2.setText(_translate("QSpectrumAnalyzerSmoothing", "Window len&gth:"))
