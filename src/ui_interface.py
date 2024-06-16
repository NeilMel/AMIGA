# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLCDNumber, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(986, 653)
        MainWindow.setMinimumSize(QSize(974, 492))
        MainWindow.setStyleSheet(u"*{\n"
"margin: 0px;\n"
"padding: 0px;\n"
"background-color: #EBEBEB;\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: #EBEBEB;\n"
"}\n"
"\n"
"#header, #widget_2, #adminLoginPage{\n"
"background-color: #DB6262;\n"
"border-bottom-left-radius: 15px;\n"
"border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"#adminFrame, #adminBtn, #resetBtn, #continueBtn{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"#widget {\n"
"    background-color: transparent;\n"
"    background-position: center;\n"
"}\n"
"\n"
"#img_icon{\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#idleTimer{\n"
"color: black;\n"
"background-color: green;\n"
"}\n"
"\n"
"#msg_label, #msg_label2, #msg_label3, #msg_label4{\n"
"font-size: 50px;\n"
"color: black;\n"
"}\n"
"\n"
"#adminBtn, #resetBtn, #continueBtn{\n"
"color: white;\n"
"}\n"
"\n"
".QPushButton{\n"
"color: #DB6262;\n"
"}\n"
"\n"
"#inputPrompt, #inputPrompt_2, #userInputTableWidget{\n"
"color: black;\n"
"}\n"
"\n"
"#response_label, #label, #label_2, #fileListLbl{\n"
"color: black; \n"
"}\n"
"\n"
"#frame"
                        ", #frame_2 {\n"
"margin: 2px;\n"
"}\n"
"\n"
"#label_4, #usernamefield, #passwordfield, #label_5 {\n"
"color: black; \n"
"}\n"
"\n"
"#label_3{\n"
"color:black;\n"
"}\n"
"\n"
"#loginBtn {\n"
"font-size: 20px;\n"
"color: white;\n"
"border-radius: 10px;\n"
"background-color: pink;\n"
"padding: 5px 20px;\n"
"}\n"
"\n"
"#embedBtn, #browseOrdeleteBtn, #deleteDataBtn{\n"
"background-color: pink;\n"
"color: black;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"#adminLoginPage{\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.widget_2 = QWidget(self.header)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_17 = QVBoxLayout(self.widget_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.idleTimer = QLCDNumber(self.widget_2)
        self.idleTimer.setObjectName(u"idleTimer")
        self.idleTimer.setLayoutDirection(Qt.LeftToRight)
        self.idleTimer.setFrameShadow(QFrame.Raised)
        self.idleTimer.setSegmentStyle(QLCDNumber.Filled)

        self.verticalLayout_17.addWidget(self.idleTimer)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(9)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_4)


        self.horizontalLayout.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.widget = QWidget(self.header)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.img_icon = QLabel(self.widget)
        self.img_icon.setObjectName(u"img_icon")
        self.img_icon.setMinimumSize(QSize(0, 0))
        self.img_icon.setMaximumSize(QSize(230, 230))
        self.img_icon.setFrameShadow(QFrame.Plain)
        self.img_icon.setPixmap(QPixmap(u":/imgs/img/3d_character_58 1.png"))
        self.img_icon.setScaledContents(True)
        self.img_icon.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.img_icon.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.img_icon)


        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignHCenter)

        self.adminFrame = QFrame(self.header)
        self.adminFrame.setObjectName(u"adminFrame")
        self.adminFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.adminFrame.setFrameShape(QFrame.StyledPanel)
        self.adminFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.adminFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.adminBtn = QPushButton(self.adminFrame)
        self.adminBtn.setObjectName(u"adminBtn")
        font1 = QFont()
        font1.setFamilies([u"Simplex_IV50"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        self.adminBtn.setFont(font1)
        self.adminBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/security.png", QSize(), QIcon.Normal, QIcon.Off)
        self.adminBtn.setIcon(icon)

        self.verticalLayout_2.addWidget(self.adminBtn)

        self.resetBtn = QPushButton(self.adminFrame)
        self.resetBtn.setObjectName(u"resetBtn")
        font2 = QFont()
        font2.setFamilies([u"Simplex_IV50"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.resetBtn.setFont(font2)
        self.resetBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/reset_tv.png", QSize(), QIcon.Normal, QIcon.Off)
        self.resetBtn.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.resetBtn)

        self.continueBtn = QPushButton(self.adminFrame)
        self.continueBtn.setObjectName(u"continueBtn")
        self.continueBtn.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/arrow-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.continueBtn.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.continueBtn)


        self.horizontalLayout.addWidget(self.adminFrame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        font3 = QFont()
        font3.setBold(True)
        self.mainBody.setFont(font3)
        self.verticalLayout_18 = QVBoxLayout(self.mainBody)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.stackedWidget = QCustomQStackedWidget(self.mainBody)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.homeWidgetPage = QWidget()
        self.homeWidgetPage.setObjectName(u"homeWidgetPage")
        self.verticalLayout_5 = QVBoxLayout(self.homeWidgetPage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.msg_label = QLabel(self.homeWidgetPage)
        self.msg_label.setObjectName(u"msg_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg_label.sizePolicy().hasHeightForWidth())
        self.msg_label.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Simplex_IV25"])
        font4.setBold(True)
        self.msg_label.setFont(font4)

        self.verticalLayout_5.addWidget(self.msg_label, 0, Qt.AlignHCenter)

        self.widget_12 = QWidget(self.homeWidgetPage)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.wakeUpBtn = QPushButton(self.widget_12)
        self.wakeUpBtn.setObjectName(u"wakeUpBtn")
        self.wakeUpBtn.setEnabled(True)
        self.wakeUpBtn.setIconSize(QSize(0, 0))

        self.horizontalLayout_7.addWidget(self.wakeUpBtn)


        self.verticalLayout_5.addWidget(self.widget_12, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.stackedWidget.addWidget(self.homeWidgetPage)
        self.adminLoginPage = QWidget()
        self.adminLoginPage.setObjectName(u"adminLoginPage")
        self.verticalLayout_16 = QVBoxLayout(self.adminLoginPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame = QFrame(self.adminLoginPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font5 = QFont()
        font5.setFamilies([u"Montserrat Medium"])
        font5.setPointSize(10)
        self.label.setFont(font5)

        self.horizontalLayout_5.addWidget(self.label)

        self.usernamefield = QLineEdit(self.frame)
        self.usernamefield.setObjectName(u"usernamefield")

        self.horizontalLayout_5.addWidget(self.usernamefield)


        self.verticalLayout_16.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.adminLoginPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font5)

        self.horizontalLayout_6.addWidget(self.label_2)

        self.passwordfield = QLineEdit(self.frame_2)
        self.passwordfield.setObjectName(u"passwordfield")
        self.passwordfield.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.passwordfield)


        self.verticalLayout_16.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.loginBtn = QPushButton(self.adminLoginPage)
        self.loginBtn.setObjectName(u"loginBtn")
        font6 = QFont()
        font6.setFamilies([u"Montserrat ExtraBold"])
        font6.setBold(True)
        self.loginBtn.setFont(font6)
        self.loginBtn.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.loginBtn, 0, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.adminLoginPage)
        self.dashboardPage = QWidget()
        self.dashboardPage.setObjectName(u"dashboardPage")
        self.horizontalLayout_3 = QHBoxLayout(self.dashboardPage)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_3 = QFrame(self.dashboardPage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 11, 0, 0)
        self.widget_14 = QWidget(self.frame_3)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_19 = QVBoxLayout(self.widget_14)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.widget_14)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_21 = QVBoxLayout(self.widget_17)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 9)
        self.label_5 = QLabel(self.widget_17)
        self.label_5.setObjectName(u"label_5")
        font7 = QFont()
        font7.setPointSize(11)
        font7.setBold(True)
        self.label_5.setFont(font7)

        self.verticalLayout_21.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.scrollArea_2 = QScrollArea(self.widget_17)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 77, 43))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.fileListLbl = QLabel(self.scrollAreaWidgetContents_2)
        self.fileListLbl.setObjectName(u"fileListLbl")
        font8 = QFont()
        font8.setPointSize(10)
        font8.setBold(True)
        self.fileListLbl.setFont(font8)

        self.verticalLayout_22.addWidget(self.fileListLbl, 0, Qt.AlignTop)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_21.addWidget(self.scrollArea_2)


        self.verticalLayout_19.addWidget(self.widget_17)

        self.widget_16 = QWidget(self.widget_14)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(7, 7, 7, 7)
        self.widget_19 = QWidget(self.widget_16)
        self.widget_19.setObjectName(u"widget_19")
        self.verticalLayout_24 = QVBoxLayout(self.widget_19)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 4, 0)
        self.embedBtn = QPushButton(self.widget_19)
        self.embedBtn.setObjectName(u"embedBtn")
        sizePolicy.setHeightForWidth(self.embedBtn.sizePolicy().hasHeightForWidth())
        self.embedBtn.setSizePolicy(sizePolicy)
        self.embedBtn.setMinimumSize(QSize(0, 0))
        self.embedBtn.setFont(font8)
        self.embedBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/material_design/icons/material_design/input.png", QSize(), QIcon.Normal, QIcon.Off)
        self.embedBtn.setIcon(icon3)

        self.verticalLayout_24.addWidget(self.embedBtn)


        self.horizontalLayout_10.addWidget(self.widget_19)

        self.widget_18 = QWidget(self.widget_16)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_23 = QVBoxLayout(self.widget_18)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 4, 0)
        self.browseOrdeleteBtn = QPushButton(self.widget_18)
        self.browseOrdeleteBtn.setObjectName(u"browseOrdeleteBtn")
        sizePolicy.setHeightForWidth(self.browseOrdeleteBtn.sizePolicy().hasHeightForWidth())
        self.browseOrdeleteBtn.setSizePolicy(sizePolicy)
        self.browseOrdeleteBtn.setFont(font8)
        self.browseOrdeleteBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.browseOrdeleteBtn.setIcon(icon4)

        self.verticalLayout_23.addWidget(self.browseOrdeleteBtn)


        self.horizontalLayout_10.addWidget(self.widget_18)


        self.verticalLayout_19.addWidget(self.widget_16, 0, Qt.AlignBottom)


        self.horizontalLayout_9.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.frame_3)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_20 = QVBoxLayout(self.widget_15)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(4, 0, 0, 0)
        self.label_3 = QLabel(self.widget_15)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font7)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_3)

        self.userInputTableWidget = QTableWidget(self.widget_15)
        if (self.userInputTableWidget.columnCount() < 2):
            self.userInputTableWidget.setColumnCount(2)
        font9 = QFont()
        font9.setBold(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font9);
        self.userInputTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font3);
        self.userInputTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.userInputTableWidget.setObjectName(u"userInputTableWidget")
        self.userInputTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.userInputTableWidget.setShowGrid(True)
        self.userInputTableWidget.setGridStyle(Qt.SolidLine)
        self.userInputTableWidget.setSortingEnabled(False)
        self.userInputTableWidget.setWordWrap(True)
        self.userInputTableWidget.setCornerButtonEnabled(True)
        self.userInputTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.userInputTableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.userInputTableWidget.horizontalHeader().setStretchLastSection(True)
        self.userInputTableWidget.verticalHeader().setVisible(False)
        self.userInputTableWidget.verticalHeader().setHighlightSections(True)
        self.userInputTableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_20.addWidget(self.userInputTableWidget)

        self.widget_20 = QWidget(self.widget_15)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(7, 7, 7, 7)
        self.deleteDataBtn = QPushButton(self.widget_20)
        self.deleteDataBtn.setObjectName(u"deleteDataBtn")
        self.deleteDataBtn.setFont(font8)
        self.deleteDataBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/font_awesome_solid/icons/font_awesome/solid/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteDataBtn.setIcon(icon5)

        self.horizontalLayout_11.addWidget(self.deleteDataBtn)


        self.verticalLayout_20.addWidget(self.widget_20)


        self.horizontalLayout_9.addWidget(self.widget_15)


        self.horizontalLayout_3.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.dashboardPage)
        self.inputWidgetPage = QWidget()
        self.inputWidgetPage.setObjectName(u"inputWidgetPage")
        self.verticalLayout_8 = QVBoxLayout(self.inputWidgetPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_7 = QWidget(self.inputWidgetPage)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_9 = QVBoxLayout(self.widget_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.msg_label3 = QLabel(self.widget_7)
        self.msg_label3.setObjectName(u"msg_label3")
        self.msg_label3.setFont(font4)

        self.verticalLayout_9.addWidget(self.msg_label3, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.widget_7, 0, Qt.AlignTop)

        self.widget_8 = QWidget(self.inputWidgetPage)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy1)
        self.verticalLayout_10 = QVBoxLayout(self.widget_8)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.inputPrompt = QLineEdit(self.widget_8)
        self.inputPrompt.setObjectName(u"inputPrompt")
        sizePolicy.setHeightForWidth(self.inputPrompt.sizePolicy().hasHeightForWidth())
        self.inputPrompt.setSizePolicy(sizePolicy)
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setPointSize(11)
        self.inputPrompt.setFont(font10)
        self.inputPrompt.setFocusPolicy(Qt.StrongFocus)
        self.inputPrompt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.inputPrompt)

        self.widget_13 = QWidget(self.widget_8)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.process_user_input = QPushButton(self.widget_13)
        self.process_user_input.setObjectName(u"process_user_input")
        self.process_user_input.setIconSize(QSize(0, 0))

        self.horizontalLayout_8.addWidget(self.process_user_input)


        self.verticalLayout_10.addWidget(self.widget_13, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.verticalLayout_8.addWidget(self.widget_8)

        self.stackedWidget.addWidget(self.inputWidgetPage)
        self.askWidgetPage = QWidget()
        self.askWidgetPage.setObjectName(u"askWidgetPage")
        self.verticalLayout_6 = QVBoxLayout(self.askWidgetPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_3 = QWidget(self.askWidgetPage)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.msg_label2 = QLabel(self.widget_3)
        self.msg_label2.setObjectName(u"msg_label2")
        self.msg_label2.setFont(font4)

        self.horizontalLayout_4.addWidget(self.msg_label2, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.askWidgetPage)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_4 = QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.speakBtn = QPushButton(self.widget_6)
        self.speakBtn.setObjectName(u"speakBtn")
        self.speakBtn.setEnabled(True)
        font11 = QFont()
        font11.setFamilies([u"Simplex"])
        font11.setPointSize(14)
        font11.setBold(True)
        self.speakBtn.setFont(font11)
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/mic.png", QSize(), QIcon.Normal, QIcon.Off)
        self.speakBtn.setIcon(icon6)
        self.speakBtn.setIconSize(QSize(30, 47))

        self.verticalLayout_4.addWidget(self.speakBtn)


        self.horizontalLayout_2.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.inputBtn = QPushButton(self.widget_5)
        self.inputBtn.setObjectName(u"inputBtn")
        self.inputBtn.setEnabled(True)
        font12 = QFont()
        font12.setFamilies([u"Simplex_IV25"])
        font12.setPointSize(14)
        font12.setBold(True)
        self.inputBtn.setFont(font12)
        icon7 = QIcon()
        icon7.addFile(u":/font_awesome_solid/icons/font_awesome/solid/display.png", QSize(), QIcon.Normal, QIcon.Off)
        self.inputBtn.setIcon(icon7)
        self.inputBtn.setIconSize(QSize(30, 47))

        self.verticalLayout_7.addWidget(self.inputBtn)


        self.horizontalLayout_2.addWidget(self.widget_5)


        self.verticalLayout_6.addWidget(self.widget_4)

        self.stackedWidget.addWidget(self.askWidgetPage)
        self.speakWidgetPage = QWidget()
        self.speakWidgetPage.setObjectName(u"speakWidgetPage")
        self.verticalLayout_13 = QVBoxLayout(self.speakWidgetPage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_10 = QWidget(self.speakWidgetPage)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_12 = QVBoxLayout(self.widget_10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.msg_label4 = QLabel(self.widget_10)
        self.msg_label4.setObjectName(u"msg_label4")
        self.msg_label4.setFont(font4)

        self.verticalLayout_12.addWidget(self.msg_label4, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.widget_10)

        self.widget_9 = QWidget(self.speakWidgetPage)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy1.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy1)
        self.verticalLayout_11 = QVBoxLayout(self.widget_9)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.inputPrompt_2 = QLineEdit(self.widget_9)
        self.inputPrompt_2.setObjectName(u"inputPrompt_2")
        self.inputPrompt_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.inputPrompt_2.sizePolicy().hasHeightForWidth())
        self.inputPrompt_2.setSizePolicy(sizePolicy)
        font13 = QFont()
        font13.setFamilies([u"Segoe UI"])
        font13.setPointSize(11)
        font13.setBold(False)
        font13.setKerning(True)
        self.inputPrompt_2.setFont(font13)
        self.inputPrompt_2.setFocusPolicy(Qt.StrongFocus)
        self.inputPrompt_2.setLayoutDirection(Qt.LeftToRight)
        self.inputPrompt_2.setAutoFillBackground(False)
        self.inputPrompt_2.setAlignment(Qt.AlignCenter)
        self.inputPrompt_2.setDragEnabled(False)
        self.inputPrompt_2.setReadOnly(True)
        self.inputPrompt_2.setClearButtonEnabled(False)

        self.verticalLayout_11.addWidget(self.inputPrompt_2)

        self.process_speak_input = QPushButton(self.widget_9)
        self.process_speak_input.setObjectName(u"process_speak_input")

        self.verticalLayout_11.addWidget(self.process_speak_input, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.widget_9)

        self.stackedWidget.addWidget(self.speakWidgetPage)
        self.response_Page = QWidget()
        self.response_Page.setObjectName(u"response_Page")
        self.verticalLayout_14 = QVBoxLayout(self.response_Page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_11 = QWidget(self.response_Page)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy)
        self.verticalLayout_15 = QVBoxLayout(self.widget_11)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.response_label = QLabel(self.widget_11)
        self.response_label.setObjectName(u"response_label")
        sizePolicy.setHeightForWidth(self.response_label.sizePolicy().hasHeightForWidth())
        self.response_label.setSizePolicy(sizePolicy)
        font14 = QFont()
        font14.setFamilies([u"Segoe UI"])
        font14.setPointSize(15)
        self.response_label.setFont(font14)
        self.response_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.response_label.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.response_label)


        self.verticalLayout_14.addWidget(self.widget_11)

        self.stackedWidget.addWidget(self.response_Page)

        self.verticalLayout_18.addWidget(self.stackedWidget)

        self.logInPageBtn = QPushButton(self.mainBody)
        self.logInPageBtn.setObjectName(u"logInPageBtn")

        self.verticalLayout_18.addWidget(self.logInPageBtn)

        self.resetBtn_2 = QPushButton(self.mainBody)
        self.resetBtn_2.setObjectName(u"resetBtn_2")
        self.resetBtn_2.setIconSize(QSize(0, 0))

        self.verticalLayout_18.addWidget(self.resetBtn_2, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Idle Timer", None))
        self.img_icon.setText("")
        self.adminBtn.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.resetBtn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.continueBtn.setText(QCoreApplication.translate("MainWindow", u"Continue", None))
        self.msg_label.setText(QCoreApplication.translate("MainWindow", u"Press \"W\" to wake AMIGA", None))
        self.wakeUpBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.usernamefield.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input username", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.passwordfield.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Input password", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Log in", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Files present", None))
        self.fileListLbl.setText("")
        self.embedBtn.setText(QCoreApplication.translate("MainWindow", u"Embed", None))
        self.browseOrdeleteBtn.setText(QCoreApplication.translate("MainWindow", u"Browse and Delete", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Prompt Lists", None))
        ___qtablewidgetitem = self.userInputTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Prompt Num", None));
        ___qtablewidgetitem1 = self.userInputTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Prompt", None));
        self.deleteDataBtn.setText(QCoreApplication.translate("MainWindow", u"Erase Data", None))
        self.msg_label3.setText(QCoreApplication.translate("MainWindow", u"Please Input Prompt", None))
        self.inputPrompt.setInputMask("")
        self.inputPrompt.setText("")
        self.inputPrompt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please Enter your prompt here........", None))
        self.process_user_input.setText("")
        self.msg_label2.setText(QCoreApplication.translate("MainWindow", u"How May I help You?", None))
        self.speakBtn.setText(QCoreApplication.translate("MainWindow", u"Press S to Speak", None))
        self.inputBtn.setText(QCoreApplication.translate("MainWindow", u"Press I to Type", None))
        self.msg_label4.setText(QCoreApplication.translate("MainWindow", u"Press \"Enter if you're done\"", None))
        self.inputPrompt_2.setInputMask("")
        self.inputPrompt_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"[PLEASE NOTE: This will only stop and the idle timer is less than '0' or the user would click 'ENTER']", None))
        self.process_speak_input.setText("")
        self.response_label.setText(QCoreApplication.translate("MainWindow", u"Gpt Response Here ......", None))
        self.logInPageBtn.setText("")
        self.resetBtn_2.setText("")
    # retranslateUi

