# Form implementation generated from reading ui file 'qspectrumanalyzer_baseline.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_QSpectrumAnalyzerBaseline(object):
    def setupUi(self, QSpectrumAnalyzerBaseline):
        QSpectrumAnalyzerBaseline.setObjectName("QSpectrumAnalyzerBaseline")
        QSpectrumAnalyzerBaseline.resize(500, 100)
        self.verticalLayout = QtWidgets.QVBoxLayout(QSpectrumAnalyzerBaseline)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(QSpectrumAnalyzerBaseline)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.baselineFileEdit = QtWidgets.QLineEdit(QSpectrumAnalyzerBaseline)
        self.baselineFileEdit.setObjectName("baselineFileEdit")
        self.horizontalLayout.addWidget(self.baselineFileEdit)
        self.baselineFileButton = QtWidgets.QToolButton(QSpectrumAnalyzerBaseline)
        self.baselineFileButton.setMinimumSize(QtCore.QSize(50, 0))
        self.baselineFileButton.setObjectName("baselineFileButton")
        self.horizontalLayout.addWidget(self.baselineFileButton)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalLayout)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(QSpectrumAnalyzerBaseline)
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.baselineFileEdit)

        self.retranslateUi(QSpectrumAnalyzerBaseline)
        self.buttonBox.accepted.connect(QSpectrumAnalyzerBaseline.accept) # type: ignore
        self.buttonBox.rejected.connect(QSpectrumAnalyzerBaseline.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(QSpectrumAnalyzerBaseline)
        QSpectrumAnalyzerBaseline.setTabOrder(self.baselineFileEdit, self.baselineFileButton)

    def retranslateUi(self, QSpectrumAnalyzerBaseline):
        _translate = QtCore.QCoreApplication.translate
        QSpectrumAnalyzerBaseline.setWindowTitle(_translate("QSpectrumAnalyzerBaseline", "Baseline - QSpectrumAnalyzer"))
        self.label.setText(_translate("QSpectrumAnalyzerBaseline", "Baseline &file:"))
        self.baselineFileButton.setText(_translate("QSpectrumAnalyzerBaseline", "..."))
