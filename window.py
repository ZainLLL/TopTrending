# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("等距更纱黑体 SC")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/img/img/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap(":/img/img/logo.ico"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/img/img/logo.ico"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/img/img/logo.ico"), QtGui.QIcon.Active, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(25, 25))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(-1, 12, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMouseTracking(False)
        self.frame.setFocusPolicy(QtCore.Qt.NoFocus)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setMaximumSize(QtCore.QSize(165000, 30000))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setPixmap(QtGui.QPixmap(":/img/img/title_black.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn1 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy)
        self.btn1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("等距更纱黑体 SC")
        font.setPointSize(12)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.verticalLayout_4.addWidget(self.btn1)
        self.btn2 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等距更纱黑体 SC")
        font.setPointSize(12)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.verticalLayout_4.addWidget(self.btn2)
        self.btn3 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等距更纱黑体 SC")
        font.setPointSize(12)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.verticalLayout_4.addWidget(self.btn3)
        self.btn4 = QtWidgets.QPushButton(self.frame_4)
        self.btn4.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy)
        self.btn4.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("等距更纱黑体 SC")
        font.setPointSize(12)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.verticalLayout_4.addWidget(self.btn4)
        self.horizontalLayout_8.addWidget(self.frame_4)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addWidget(self.frame)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.Rpage = QtWidgets.QStackedWidget(self.centralwidget)
        self.Rpage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Rpage.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Rpage.setObjectName("Rpage")
        self.IntroPage = QtWidgets.QWidget()
        self.IntroPage.setObjectName("IntroPage")
        self.gridLayout = QtWidgets.QGridLayout(self.IntroPage)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.IntroPage)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.IntroPage)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.Rpage.addWidget(self.IntroPage)
        self.TrendPage = QtWidgets.QWidget()
        self.TrendPage.setObjectName("TrendPage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.TrendPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.TrendPage)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(130, 16))
        self.comboBox.setObjectName("comboBox")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/img/weibo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon1, "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/img/zhihu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon2, "")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/img/baidu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.comboBox.addItem(icon3, "")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem7 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setStyleSheet("border: 1px solid #455364;border-radius: 4px;")
        self.label_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.time_label = QtWidgets.QLabel(self.frame_3)
        self.time_label.setStyleSheet("border: 1px solid #455364;border-radius: 4px;")
        self.time_label.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.time_label.setObjectName("time_label")
        self.horizontalLayout_2.addWidget(self.time_label)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.RefreshButton = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RefreshButton.sizePolicy().hasHeightForWidth())
        self.RefreshButton.setSizePolicy(sizePolicy)
        self.RefreshButton.setMinimumSize(QtCore.QSize(60, 20))
        self.RefreshButton.setStyleSheet("background: #19232D;\n"
"border: 1px solid #455364;border-radius: 4px;")
        self.RefreshButton.setObjectName("RefreshButton")
        self.horizontalLayout_2.addWidget(self.RefreshButton)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.stackedWidget = QtWidgets.QStackedWidget(self.TrendPage)
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setObjectName("stackedWidget")
        self.wb = QtWidgets.QWidget()
        self.wb.setObjectName("wb")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.wb)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.wblist = QtWidgets.QListWidget(self.wb)
        self.wblist.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wblist.sizePolicy().hasHeightForWidth())
        self.wblist.setSizePolicy(sizePolicy)
        self.wblist.setMinimumSize(QtCore.QSize(300, 0))
        self.wblist.setObjectName("wblist")
        self.horizontalLayout_5.addWidget(self.wblist)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.stackedWidget.addWidget(self.wb)
        self.zh = QtWidgets.QWidget()
        self.zh.setObjectName("zh")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.zh)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.zhlist = QtWidgets.QListWidget(self.zh)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zhlist.sizePolicy().hasHeightForWidth())
        self.zhlist.setSizePolicy(sizePolicy)
        self.zhlist.setMinimumSize(QtCore.QSize(240, 0))
        self.zhlist.setStyleSheet("QListWidget::item:{padding-top:-2px; padding-bottom:1px;border: 1px solid red;}")
        self.zhlist.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.zhlist.setLineWidth(1)
        self.zhlist.setProperty("isWrapping", False)
        self.zhlist.setResizeMode(QtWidgets.QListView.Adjust)
        self.zhlist.setWordWrap(True)
        self.zhlist.setObjectName("zhlist")
        self.horizontalLayout_7.addWidget(self.zhlist)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.stackedWidget.addWidget(self.zh)
        self.bd = QtWidgets.QWidget()
        self.bd.setObjectName("bd")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.bd)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem14)
        self.bdlist = QtWidgets.QListWidget(self.bd)
        self.bdlist.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bdlist.sizePolicy().hasHeightForWidth())
        self.bdlist.setSizePolicy(sizePolicy)
        self.bdlist.setMinimumSize(QtCore.QSize(300, 0))
        self.bdlist.setObjectName("bdlist")
        self.horizontalLayout_6.addWidget(self.bdlist)
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem15)
        self.stackedWidget.addWidget(self.bd)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.Rpage.addWidget(self.TrendPage)
        self.WCPage = QtWidgets.QWidget()
        self.WCPage.setObjectName("WCPage")
        self.pushButton_2 = QtWidgets.QPushButton(self.WCPage)
        self.pushButton_2.setGeometry(QtCore.QRect(6, 278, 56, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.WCPage)
        self.label_5.setGeometry(QtCore.QRect(466, 6, 16, 16))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.comboBox_2 = QtWidgets.QComboBox(self.WCPage)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 150, 130, 19))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setMinimumSize(QtCore.QSize(130, 16))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem(icon1, "")
        self.comboBox_2.addItem(icon2, "")
        self.comboBox_2.addItem(icon3, "")
        self.Rpage.addWidget(self.WCPage)
        self.window4 = QtWidgets.QWidget()
        self.window4.setObjectName("window4")
        self.label_4 = QtWidgets.QLabel(self.window4)
        self.label_4.setGeometry(QtCore.QRect(40, 50, 121, 51))
        self.label_4.setObjectName("label_4")
        self.Rpage.addWidget(self.window4)
        self.horizontalLayout.addWidget(self.Rpage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Rpage.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn1.setText(_translate("MainWindow", "HomePage"))
        self.btn2.setText(_translate("MainWindow", "Trending"))
        self.btn3.setText(_translate("MainWindow", "WordCloud"))
        self.btn4.setText(_translate("MainWindow", "Page4"))
        self.label_3.setText(_translate("MainWindow", "Top Trending"))
        self.label_2.setText(_translate("MainWindow", "What\'s happening in the world?"))
        self.comboBox.setItemText(0, _translate("MainWindow", "微博热搜 "))
        self.comboBox.setItemText(1, _translate("MainWindow", "知乎热榜 "))
        self.comboBox.setItemText(2, _translate("MainWindow", "百度热搜 "))
        self.label_6.setText(_translate("MainWindow", "更新时间"))
        self.time_label.setText(_translate("MainWindow", "TextLabel"))
        self.RefreshButton.setText(_translate("MainWindow", "刷新"))
        self.pushButton_2.setText(_translate("MainWindow", "generate \n"
" WordCloud"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "微博热搜 "))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "知乎热榜 "))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "百度热搜 "))
        self.label_4.setText(_translate("MainWindow", "wait for adding"))
import img
