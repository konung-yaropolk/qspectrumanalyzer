# Form implementation generated from reading ui file 'qspectrumanalyzer.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_QSpectrumAnalyzerMainWindow(object):
    def setupUi(self, QSpectrumAnalyzerMainWindow):
        QSpectrumAnalyzerMainWindow.setObjectName("QSpectrumAnalyzerMainWindow")
        QSpectrumAnalyzerMainWindow.resize(1200, 899)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(220, 217, 214))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 3, 3))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 247, 247))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 142, 147))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 200, 204))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 217, 214))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 217, 214))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 15, 14))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 181, 179))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(61, 174, 233))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 128, 185))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 8, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 8, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 217, 214))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 217, 214))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 3, 3))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 247, 247))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 142, 147))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 200, 204))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 217, 214))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 217, 214))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 15, 14))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 181, 179))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(39, 112, 149))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 128, 185))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 8, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 8, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 217, 214))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 142, 147))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(3, 3, 3))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 247, 247))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 142, 147))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 200, 204))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 142, 147))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(136, 142, 147))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 15, 14))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 15, 14))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 181, 179))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 229, 231))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(41, 128, 185))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 8, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(8, 8, 8))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 217, 214))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 38, 41, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        QSpectrumAnalyzerMainWindow.setPalette(palette)
        QSpectrumAnalyzerMainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(QSpectrumAnalyzerMainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.plotSplitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotSplitter.sizePolicy().hasHeightForWidth())
        self.plotSplitter.setSizePolicy(sizePolicy)
        self.plotSplitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.plotSplitter.setObjectName("plotSplitter")
        self.mainPlotLayout = GraphicsLayoutWidget(self.plotSplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainPlotLayout.sizePolicy().hasHeightForWidth())
        self.mainPlotLayout.setSizePolicy(sizePolicy)
        self.mainPlotLayout.setObjectName("mainPlotLayout")
        self.waterfallPlotLayout = GraphicsLayoutWidget(self.plotSplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.waterfallPlotLayout.sizePolicy().hasHeightForWidth())
        self.waterfallPlotLayout.setSizePolicy(sizePolicy)
        self.waterfallPlotLayout.setObjectName("waterfallPlotLayout")
        self.horizontalLayout.addWidget(self.plotSplitter)
        QSpectrumAnalyzerMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QSpectrumAnalyzerMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 30))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        QSpectrumAnalyzerMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(QSpectrumAnalyzerMainWindow)
        self.statusbar.setObjectName("statusbar")
        QSpectrumAnalyzerMainWindow.setStatusBar(self.statusbar)
        self.controlsDockWidget = QtWidgets.QDockWidget(QSpectrumAnalyzerMainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controlsDockWidget.sizePolicy().hasHeightForWidth())
        self.controlsDockWidget.setSizePolicy(sizePolicy)
        self.controlsDockWidget.setMinimumSize(QtCore.QSize(190, 111))
        self.controlsDockWidget.setMaximumSize(QtCore.QSize(233, 111))
        self.controlsDockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.controlsDockWidget.setObjectName("controlsDockWidget")
        self.controlsDockWidgetContents = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controlsDockWidgetContents.sizePolicy().hasHeightForWidth())
        self.controlsDockWidgetContents.setSizePolicy(sizePolicy)
        self.controlsDockWidgetContents.setObjectName("controlsDockWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.controlsDockWidgetContents)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.singleShotButton = QtWidgets.QPushButton(self.controlsDockWidgetContents)
        self.singleShotButton.setObjectName("singleShotButton")
        self.gridLayout_2.addWidget(self.singleShotButton, 1, 0, 1, 2)
        self.stopButton = QtWidgets.QPushButton(self.controlsDockWidgetContents)
        self.stopButton.setObjectName("stopButton")
        self.gridLayout_2.addWidget(self.stopButton, 0, 1, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.controlsDockWidgetContents)
        self.startButton.setObjectName("startButton")
        self.gridLayout_2.addWidget(self.startButton, 0, 0, 1, 1)
        self.controlsDockWidget.setWidget(self.controlsDockWidgetContents)
        QSpectrumAnalyzerMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.controlsDockWidget)
        self.frequencyDockWidget = QtWidgets.QDockWidget(QSpectrumAnalyzerMainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frequencyDockWidget.sizePolicy().hasHeightForWidth())
        self.frequencyDockWidget.setSizePolicy(sizePolicy)
        self.frequencyDockWidget.setMinimumSize(QtCore.QSize(190, 142))
        self.frequencyDockWidget.setMaximumSize(QtCore.QSize(233, 142))
        self.frequencyDockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.frequencyDockWidget.setObjectName("frequencyDockWidget")
        self.frequencyDockWidgetContents = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frequencyDockWidgetContents.sizePolicy().hasHeightForWidth())
        self.frequencyDockWidgetContents.setSizePolicy(sizePolicy)
        self.frequencyDockWidgetContents.setObjectName("frequencyDockWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.frequencyDockWidgetContents)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)
        self.formLayout.setContentsMargins(3, 3, 3, 3)
        self.formLayout.setSpacing(3)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frequencyDockWidgetContents)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.startFreqSpinBox = QtWidgets.QDoubleSpinBox(self.frequencyDockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startFreqSpinBox.sizePolicy().hasHeightForWidth())
        self.startFreqSpinBox.setSizePolicy(sizePolicy)
        self.startFreqSpinBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.startFreqSpinBox.setProperty("showGroupSeparator", True)
        self.startFreqSpinBox.setDecimals(3)
        self.startFreqSpinBox.setMinimum(0.0)
        self.startFreqSpinBox.setMaximum(2200.0)
        self.startFreqSpinBox.setProperty("value", 87.0)
        self.startFreqSpinBox.setObjectName("startFreqSpinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.startFreqSpinBox)
        self.label_3 = QtWidgets.QLabel(self.frequencyDockWidgetContents)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.stopFreqSpinBox = QtWidgets.QDoubleSpinBox(self.frequencyDockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopFreqSpinBox.sizePolicy().hasHeightForWidth())
        self.stopFreqSpinBox.setSizePolicy(sizePolicy)
        self.stopFreqSpinBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.stopFreqSpinBox.setProperty("showGroupSeparator", True)
        self.stopFreqSpinBox.setDecimals(3)
        self.stopFreqSpinBox.setMinimum(0.0)
        self.stopFreqSpinBox.setMaximum(2200.0)
        self.stopFreqSpinBox.setProperty("value", 108.0)
        self.stopFreqSpinBox.setObjectName("stopFreqSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.stopFreqSpinBox)
        self.label = QtWidgets.QLabel(self.frequencyDockWidgetContents)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.binSizeSpinBox = QtWidgets.QDoubleSpinBox(self.frequencyDockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.binSizeSpinBox.sizePolicy().hasHeightForWidth())
        self.binSizeSpinBox.setSizePolicy(sizePolicy)
        self.binSizeSpinBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.binSizeSpinBox.setProperty("showGroupSeparator", True)
        self.binSizeSpinBox.setDecimals(3)
        self.binSizeSpinBox.setMinimum(0.0)
        self.binSizeSpinBox.setMaximum(10000.0)
        self.binSizeSpinBox.setProperty("value", 10.0)
        self.binSizeSpinBox.setObjectName("binSizeSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.binSizeSpinBox)
        self.frequencyDockWidget.setWidget(self.frequencyDockWidgetContents)
        QSpectrumAnalyzerMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.frequencyDockWidget)
        self.settingsDockWidget = QtWidgets.QDockWidget(QSpectrumAnalyzerMainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsDockWidget.sizePolicy().hasHeightForWidth())
        self.settingsDockWidget.setSizePolicy(sizePolicy)
        self.settingsDockWidget.setMinimumSize(QtCore.QSize(233, 348))
        self.settingsDockWidget.setMaximumSize(QtCore.QSize(233, 348))
        self.settingsDockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.settingsDockWidget.setObjectName("settingsDockWidget")
        self.settingsDockWidgetContents = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsDockWidgetContents.sizePolicy().hasHeightForWidth())
        self.settingsDockWidgetContents.setSizePolicy(sizePolicy)
        self.settingsDockWidgetContents.setObjectName("settingsDockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.settingsDockWidgetContents)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.baselineCheckBox = QtWidgets.QCheckBox(self.settingsDockWidgetContents)
        self.baselineCheckBox.setObjectName("baselineCheckBox")
        self.gridLayout.addWidget(self.baselineCheckBox, 10, 0, 1, 1)
        self.intervalSpinBox = QtWidgets.QSpinBox(self.settingsDockWidgetContents)
        self.intervalSpinBox.setMaximum(999)
        self.intervalSpinBox.setObjectName("intervalSpinBox")
        self.gridLayout.addWidget(self.intervalSpinBox, 1, 0, 1, 1)
        self.smoothButton = QtWidgets.QToolButton(self.settingsDockWidgetContents)
        self.smoothButton.setIconSize(QtCore.QSize(16, 16))
        self.smoothButton.setAutoRaise(False)
        self.smoothButton.setObjectName("smoothButton")
        self.gridLayout.addWidget(self.smoothButton, 6, 2, 2, 1)
        self.peakHoldMaxCheckBox = QtWidgets.QCheckBox(self.settingsDockWidgetContents)
        self.peakHoldMaxCheckBox.setObjectName("peakHoldMaxCheckBox")
        self.gridLayout.addWidget(self.peakHoldMaxCheckBox, 5, 0, 1, 1)
        self.mainCurveCheckBox = QtWidgets.QCheckBox(self.settingsDockWidgetContents)
        self.mainCurveCheckBox.setChecked(True)
        self.mainCurveCheckBox.setObjectName("mainCurveCheckBox")
        self.gridLayout.addWidget(self.mainCurveCheckBox, 4, 0, 1, 1)
        self.peakHoldMinCheckBox = QtWidgets.QCheckBox(self.settingsDockWidgetContents)
        self.peakHoldMinCheckBox.setObjectName("peakHoldMinCheckBox")
        self.gridLayout.addWidget(self.peakHoldMinCheckBox, 5, 1, 1, 2)
        self.colorsButton = QtWidgets.QPushButton(self.settingsDockWidgetContents)
        self.colorsButton.setObjectName("colorsButton")
        self.gridLayout.addWidget(self.colorsButton, 4, 1, 1, 2)
        self.baselineButton = QtWidgets.QToolButton(self.settingsDockWidgetContents)
        self.baselineButton.setAutoRaise(False)
        self.baselineButton.setObjectName("baselineButton")
        self.gridLayout.addWidget(self.baselineButton, 10, 2, 2, 1)
        self.subtractBaselineCheckBox = QtWidgets.QCheckBox(self.settingsDockWidgetContents)
        self.subtractBaselineCheckBox.setObjectName("subtractBaselineCheckBox")
        self.gridLayout.addWidget(self.subtractBaselineCheckBox, 11, 0, 1, 1)
        self.persistenceCheckBox = QtWidgets.QCheckBox(self.settingsDockWidgetContents)
        self.persistenceCheckBox.setObjectName("persistenceCheckBox")
        self.gridLayout.addWidget(self.persistenceCheckBox, 9, 0, 1, 1)
        self.averageCheckBox = QtWidgets.QCheckBox(self.settingsDockWidgetContents)
        self.averageCheckBox.setObjectName("averageCheckBox")
        self.gridLayout.addWidget(self.averageCheckBox, 6, 0, 1, 1)
        self.persistenceButton = QtWidgets.QToolButton(self.settingsDockWidgetContents)
        self.persistenceButton.setAutoRaise(False)
        self.persistenceButton.setObjectName("persistenceButton")
        self.gridLayout.addWidget(self.persistenceButton, 9, 2, 1, 1)
        self.ppmSpinBox = QtWidgets.QSpinBox(self.settingsDockWidgetContents)
        self.ppmSpinBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ppmSpinBox.setSuffix("")
        self.ppmSpinBox.setPrefix("Corr. [ppm]: ")
        self.ppmSpinBox.setMinimum(-999)
        self.ppmSpinBox.setMaximum(999)
        self.ppmSpinBox.setObjectName("ppmSpinBox")
        self.gridLayout.addWidget(self.ppmSpinBox, 3, 0, 1, 1)
        self.smoothCheckBox = QtWidgets.QCheckBox(self.settingsDockWidgetContents)
        self.smoothCheckBox.setObjectName("smoothCheckBox")
        self.gridLayout.addWidget(self.smoothCheckBox, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.settingsDockWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.settingsDockWidgetContents)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.cropSpinBox = QtWidgets.QSpinBox(self.settingsDockWidgetContents)
        self.cropSpinBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.cropSpinBox.setSuffix("")
        self.cropSpinBox.setPrefix("Crop [%]: ")
        self.cropSpinBox.setMaximum(49)
        self.cropSpinBox.setProperty("value", 25)
        self.cropSpinBox.setObjectName("cropSpinBox")
        self.gridLayout.addWidget(self.cropSpinBox, 3, 1, 1, 2)
        self.gainSpinBox = QtWidgets.QDoubleSpinBox(self.settingsDockWidgetContents)
        self.gainSpinBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.gainSpinBox.setPrefix("")
        self.gainSpinBox.setDecimals(1)
        self.gainSpinBox.setMinimum(-1.0)
        self.gainSpinBox.setMaximum(999.0)
        self.gainSpinBox.setSingleStep(1.0)
        self.gainSpinBox.setProperty("value", -1.0)
        self.gainSpinBox.setObjectName("gainSpinBox")
        self.gridLayout.addWidget(self.gainSpinBox, 1, 1, 1, 2)
        self.settingsDockWidget.setWidget(self.settingsDockWidgetContents)
        QSpectrumAnalyzerMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.settingsDockWidget)
        self.levelsDockWidget = QtWidgets.QDockWidget(QSpectrumAnalyzerMainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.levelsDockWidget.sizePolicy().hasHeightForWidth())
        self.levelsDockWidget.setSizePolicy(sizePolicy)
        self.levelsDockWidget.setMinimumSize(QtCore.QSize(190, 233))
        self.levelsDockWidget.setMaximumSize(QtCore.QSize(233, 524287))
        self.levelsDockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetFeature.DockWidgetMovable)
        self.levelsDockWidget.setObjectName("levelsDockWidget")
        self.levelsDockWidgetContents = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.levelsDockWidgetContents.sizePolicy().hasHeightForWidth())
        self.levelsDockWidgetContents.setSizePolicy(sizePolicy)
        self.levelsDockWidgetContents.setObjectName("levelsDockWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.levelsDockWidgetContents)
        self.verticalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.histogramPlotLayout = GraphicsLayoutWidget(self.levelsDockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.histogramPlotLayout.sizePolicy().hasHeightForWidth())
        self.histogramPlotLayout.setSizePolicy(sizePolicy)
        self.histogramPlotLayout.setObjectName("histogramPlotLayout")
        self.verticalLayout_6.addWidget(self.histogramPlotLayout)
        self.levelsDockWidget.setWidget(self.levelsDockWidgetContents)
        QSpectrumAnalyzerMainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.levelsDockWidget)
        self.action_Settings = QtGui.QAction(QSpectrumAnalyzerMainWindow)
        self.action_Settings.setObjectName("action_Settings")
        self.action_Quit = QtGui.QAction(QSpectrumAnalyzerMainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.action_About = QtGui.QAction(QSpectrumAnalyzerMainWindow)
        self.action_About.setObjectName("action_About")
        self.menu_File.addAction(self.action_Settings)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.label_2.setBuddy(self.startFreqSpinBox)
        self.label_3.setBuddy(self.stopFreqSpinBox)
        self.label.setBuddy(self.binSizeSpinBox)
        self.label_6.setBuddy(self.gainSpinBox)

        self.retranslateUi(QSpectrumAnalyzerMainWindow)
        QtCore.QMetaObject.connectSlotsByName(QSpectrumAnalyzerMainWindow)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.startButton, self.stopButton)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.stopButton, self.singleShotButton)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.singleShotButton, self.startFreqSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.startFreqSpinBox, self.stopFreqSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.stopFreqSpinBox, self.binSizeSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.binSizeSpinBox, self.gainSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.gainSpinBox, self.ppmSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.ppmSpinBox, self.cropSpinBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.cropSpinBox, self.mainCurveCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.mainCurveCheckBox, self.colorsButton)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.colorsButton, self.peakHoldMaxCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.peakHoldMaxCheckBox, self.peakHoldMinCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.peakHoldMinCheckBox, self.averageCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.averageCheckBox, self.smoothCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.smoothCheckBox, self.smoothButton)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.smoothButton, self.persistenceCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.persistenceCheckBox, self.baselineCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.baselineCheckBox, self.baselineButton)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.baselineButton, self.subtractBaselineCheckBox)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.subtractBaselineCheckBox, self.histogramPlotLayout)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.histogramPlotLayout, self.mainPlotLayout)
        QSpectrumAnalyzerMainWindow.setTabOrder(self.mainPlotLayout, self.waterfallPlotLayout)

    def retranslateUi(self, QSpectrumAnalyzerMainWindow):
        _translate = QtCore.QCoreApplication.translate
        QSpectrumAnalyzerMainWindow.setWindowTitle(_translate("QSpectrumAnalyzerMainWindow", "QSpectrumAnalyzer"))
        self.menu_File.setTitle(_translate("QSpectrumAnalyzerMainWindow", "&File"))
        self.menu_Help.setTitle(_translate("QSpectrumAnalyzerMainWindow", "&Help"))
        self.controlsDockWidget.setWindowTitle(_translate("QSpectrumAnalyzerMainWindow", "Controls"))
        self.singleShotButton.setText(_translate("QSpectrumAnalyzerMainWindow", "Si&ngle shot"))
        self.stopButton.setText(_translate("QSpectrumAnalyzerMainWindow", "S&top"))
        self.startButton.setText(_translate("QSpectrumAnalyzerMainWindow", "&Start"))
        self.frequencyDockWidget.setWindowTitle(_translate("QSpectrumAnalyzerMainWindow", "Frequency"))
        self.label_2.setText(_translate("QSpectrumAnalyzerMainWindow", "Start:"))
        self.startFreqSpinBox.setSuffix(_translate("QSpectrumAnalyzerMainWindow", " MHz"))
        self.label_3.setText(_translate("QSpectrumAnalyzerMainWindow", "Stop:"))
        self.stopFreqSpinBox.setSuffix(_translate("QSpectrumAnalyzerMainWindow", " MHz"))
        self.label.setText(_translate("QSpectrumAnalyzerMainWindow", "&Bin size:"))
        self.binSizeSpinBox.setSuffix(_translate("QSpectrumAnalyzerMainWindow", " kHz"))
        self.settingsDockWidget.setWindowTitle(_translate("QSpectrumAnalyzerMainWindow", "Settings"))
        self.baselineCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Baseline"))
        self.smoothButton.setText(_translate("QSpectrumAnalyzerMainWindow", "..."))
        self.peakHoldMaxCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Max. hold"))
        self.mainCurveCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Main curve"))
        self.peakHoldMinCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Min. hold"))
        self.colorsButton.setText(_translate("QSpectrumAnalyzerMainWindow", "Colors..."))
        self.baselineButton.setText(_translate("QSpectrumAnalyzerMainWindow", "..."))
        self.subtractBaselineCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Subtract baseline"))
        self.persistenceCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Persistence"))
        self.averageCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Average"))
        self.persistenceButton.setText(_translate("QSpectrumAnalyzerMainWindow", "..."))
        self.smoothCheckBox.setText(_translate("QSpectrumAnalyzerMainWindow", "Smoothing"))
        self.label_4.setText(_translate("QSpectrumAnalyzerMainWindow", "Interval [s]:"))
        self.label_6.setText(_translate("QSpectrumAnalyzerMainWindow", "&Gain [dB]:"))
        self.gainSpinBox.setSpecialValueText(_translate("QSpectrumAnalyzerMainWindow", "auto"))
        self.levelsDockWidget.setWindowTitle(_translate("QSpectrumAnalyzerMainWindow", "Levels"))
        self.action_Settings.setText(_translate("QSpectrumAnalyzerMainWindow", "&Settings..."))
        self.action_Quit.setText(_translate("QSpectrumAnalyzerMainWindow", "&Quit"))
        self.action_Quit.setShortcut(_translate("QSpectrumAnalyzerMainWindow", "Ctrl+Q"))
        self.action_About.setText(_translate("QSpectrumAnalyzerMainWindow", "&About"))
from pyqtgraph import GraphicsLayoutWidget
