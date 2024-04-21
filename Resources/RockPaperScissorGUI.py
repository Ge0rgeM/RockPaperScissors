# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RockPaperScissorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RockPaperScissor(object):
    def setupUi(self, RockPaperScissor):
        RockPaperScissor.setObjectName("RockPaperScissor")
        RockPaperScissor.setEnabled(True)
        RockPaperScissor.resize(550, 600)
        RockPaperScissor.setMinimumSize(QtCore.QSize(550, 600))
        RockPaperScissor.setAutoFillBackground(False)
        RockPaperScissor.setStyleSheet("#appName{\n"
"    color: rgb(66, 165, 116);\n"
"}\n"
"#centralwidget, #MainWindow{\n"
"    background-color: rgb(28,37,65);\n"
"}\n"
"#optionsBox{\n"
"        cursor: pointer;\n"
"}\n"
"#rock, #paper, #scissors{\n"
"    border: 1px green;\n"
"    border-style: solid;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"    background-color: rgba(66, 165, 116, 0.7);\n"
"}\n"
"#rock:hover, #paper:hover, #scissors:hover{\n"
"    background-color: rgba(66, 165, 116, 1);\n"
"}\n"
"#resultText{\n"
"    border: 1px rgb(66, 165, 116);\n"
"    border-style: solid;\n"
"    border-radius: 3px;\n"
"    color: white;\n"
"}\n"
"#vsText{\n"
"    color: rgb(96, 123, 125);\n"
"}\n"
"#PC_Score, #userScore{\n"
"    color: white;\n"
"}\n"
"#reset{\n"
"    color:  rgb(28,37,65);\n"
"    border-radius: 3px;\n"
"    background-color: rgba(255,0,0,0.7);\n"
"}\n"
"#reset:hover{\n"
"    background-color: rgba(255,0,0,1);\n"
"    color: white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(RockPaperScissor)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.appNameBox = QtWidgets.QFrame(self.centralwidget)
        self.appNameBox.setMinimumSize(QtCore.QSize(0, 70))
        self.appNameBox.setMaximumSize(QtCore.QSize(50000, 50))
        self.appNameBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.appNameBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.appNameBox.setObjectName("appNameBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.appNameBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.appName = QtWidgets.QLabel(self.appNameBox)
        self.appName.setMinimumSize(QtCore.QSize(0, 0))
        self.appName.setMaximumSize(QtCore.QSize(50000, 70))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.appName.setFont(font)
        self.appName.setScaledContents(False)
        self.appName.setAlignment(QtCore.Qt.AlignCenter)
        self.appName.setIndent(0)
        self.appName.setObjectName("appName")
        self.verticalLayout.addWidget(self.appName)
        self.gridLayout.addWidget(self.appNameBox, 0, 0, 1, 1)
        self.resultBox = QtWidgets.QFrame(self.centralwidget)
        self.resultBox.setMinimumSize(QtCore.QSize(0, 50))
        self.resultBox.setMaximumSize(QtCore.QSize(1350, 70))
        self.resultBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resultBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resultBox.setObjectName("resultBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.resultBox)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.resultText = QtWidgets.QLabel(self.resultBox)
        self.resultText.setMinimumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.resultText.setFont(font)
        self.resultText.setStyleSheet("#label_3{\n"
"    /*background-color: black;*/\n"
"    border-width: 1px;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"}")
        self.resultText.setAlignment(QtCore.Qt.AlignCenter)
        self.resultText.setObjectName("resultText")
        self.horizontalLayout_2.addWidget(self.resultText)
        self.gridLayout.addWidget(self.resultBox, 3, 0, 1, 1)
        self.resetBox = QtWidgets.QFrame(self.centralwidget)
        self.resetBox.setMinimumSize(QtCore.QSize(0, 60))
        self.resetBox.setMaximumSize(QtCore.QSize(16777215, 60))
        self.resetBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resetBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resetBox.setObjectName("resetBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.resetBox)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.reset = QtWidgets.QPushButton(self.resetBox)
        self.reset.setMinimumSize(QtCore.QSize(0, 50))
        self.reset.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.reset.setFont(font)
        self.reset.setObjectName("reset")
        self.horizontalLayout_4.addWidget(self.reset)
        self.gridLayout.addWidget(self.resetBox, 5, 0, 1, 1)
        self.youVsComputerBox = QtWidgets.QFrame(self.centralwidget)
        self.youVsComputerBox.setMinimumSize(QtCore.QSize(0, 150))
        self.youVsComputerBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.youVsComputerBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.youVsComputerBox.setObjectName("youVsComputerBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.youVsComputerBox)
        self.horizontalLayout.setContentsMargins(0, 10, 0, 10)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.userBox = QtWidgets.QFrame(self.youVsComputerBox)
        self.userBox.setMinimumSize(QtCore.QSize(0, 60))
        self.userBox.setMaximumSize(QtCore.QSize(150, 150))
        self.userBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userBox.setObjectName("userBox")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.userBox)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.userImg = QtWidgets.QLabel(self.userBox)
        self.userImg.setMinimumSize(QtCore.QSize(100, 60))
        self.userImg.setMaximumSize(QtCore.QSize(150, 150))
        self.userImg.setAutoFillBackground(False)
        self.userImg.setStyleSheet("#UserBox{\n"
"    background-color: green;\n"
"    border-radius: 15px;\n"
"}")
        self.userImg.setText("")
        self.userImg.setAlignment(QtCore.Qt.AlignCenter)
        self.userImg.setObjectName("userImg")
        self.horizontalLayout_8.addWidget(self.userImg)
        self.horizontalLayout.addWidget(self.userBox)
        self.vsBox = QtWidgets.QFrame(self.youVsComputerBox)
        self.vsBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.vsBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.vsBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.vsBox.setObjectName("vsBox")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.vsBox)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.vsText = QtWidgets.QLabel(self.vsBox)
        self.vsText.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.vsText.setFont(font)
        self.vsText.setAlignment(QtCore.Qt.AlignCenter)
        self.vsText.setObjectName("vsText")
        self.horizontalLayout_10.addWidget(self.vsText)
        self.horizontalLayout.addWidget(self.vsBox)
        self.computerBox = QtWidgets.QFrame(self.youVsComputerBox)
        self.computerBox.setMaximumSize(QtCore.QSize(150, 150))
        self.computerBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.computerBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.computerBox.setObjectName("computerBox")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.computerBox)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.computerImg = QtWidgets.QLabel(self.computerBox)
        self.computerImg.setMinimumSize(QtCore.QSize(60, 60))
        self.computerImg.setMaximumSize(QtCore.QSize(150, 150))
        self.computerImg.setStyleSheet("")
        self.computerImg.setText("")
        self.computerImg.setAlignment(QtCore.Qt.AlignCenter)
        self.computerImg.setObjectName("computerImg")
        self.horizontalLayout_9.addWidget(self.computerImg)
        self.horizontalLayout.addWidget(self.computerBox)
        self.gridLayout.addWidget(self.youVsComputerBox, 2, 0, 1, 1)
        self.scoreBox = QtWidgets.QFrame(self.centralwidget)
        self.scoreBox.setMaximumSize(QtCore.QSize(16777215, 150))
        self.scoreBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scoreBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scoreBox.setObjectName("scoreBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.scoreBox)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.userScoreBox = QtWidgets.QFrame(self.scoreBox)
        self.userScoreBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userScoreBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userScoreBox.setObjectName("userScoreBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.userScoreBox)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.userScore = QtWidgets.QLabel(self.userScoreBox)
        self.userScore.setMinimumSize(QtCore.QSize(50, 50))
        self.userScore.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.userScore.setFont(font)
        self.userScore.setAlignment(QtCore.Qt.AlignCenter)
        self.userScore.setObjectName("userScore")
        self.horizontalLayout_7.addWidget(self.userScore)
        self.horizontalLayout_5.addWidget(self.userScoreBox)
        self.PCScoreBox = QtWidgets.QFrame(self.scoreBox)
        self.PCScoreBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PCScoreBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PCScoreBox.setObjectName("PCScoreBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.PCScoreBox)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.PC_Score = QtWidgets.QLabel(self.PCScoreBox)
        self.PC_Score.setMinimumSize(QtCore.QSize(50, 50))
        self.PC_Score.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(38)
        self.PC_Score.setFont(font)
        self.PC_Score.setAlignment(QtCore.Qt.AlignCenter)
        self.PC_Score.setObjectName("PC_Score")
        self.horizontalLayout_6.addWidget(self.PC_Score)
        self.horizontalLayout_5.addWidget(self.PCScoreBox)
        self.gridLayout.addWidget(self.scoreBox, 1, 0, 1, 1)
        self.optionsBox = QtWidgets.QFrame(self.centralwidget)
        self.optionsBox.setMinimumSize(QtCore.QSize(0, 0))
        self.optionsBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.optionsBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.optionsBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.optionsBox.setObjectName("optionsBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.optionsBox)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rockBox = QtWidgets.QFrame(self.optionsBox)
        self.rockBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rockBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rockBox.setObjectName("rockBox")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.rockBox)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.rock = QtWidgets.QPushButton(self.rockBox)
        self.rock.setMinimumSize(QtCore.QSize(0, 50))
        self.rock.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.rock.setFont(font)
        self.rock.setObjectName("rock")
        self.horizontalLayout_13.addWidget(self.rock)
        self.horizontalLayout_3.addWidget(self.rockBox)
        self.paperBox = QtWidgets.QFrame(self.optionsBox)
        self.paperBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.paperBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.paperBox.setObjectName("paperBox")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.paperBox)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.paper = QtWidgets.QPushButton(self.paperBox)
        self.paper.setMinimumSize(QtCore.QSize(0, 50))
        self.paper.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.paper.setFont(font)
        self.paper.setObjectName("paper")
        self.horizontalLayout_12.addWidget(self.paper)
        self.horizontalLayout_3.addWidget(self.paperBox)
        self.scissorsBox = QtWidgets.QFrame(self.optionsBox)
        self.scissorsBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scissorsBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scissorsBox.setObjectName("scissorsBox")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.scissorsBox)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.scissors = QtWidgets.QPushButton(self.scissorsBox)
        self.scissors.setMinimumSize(QtCore.QSize(0, 50))
        self.scissors.setMaximumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.scissors.setFont(font)
        self.scissors.setObjectName("scissors")
        self.horizontalLayout_11.addWidget(self.scissors)
        self.horizontalLayout_3.addWidget(self.scissorsBox)
        self.gridLayout.addWidget(self.optionsBox, 4, 0, 1, 1)
        RockPaperScissor.setCentralWidget(self.centralwidget)

        self.retranslateUi(RockPaperScissor)
        QtCore.QMetaObject.connectSlotsByName(RockPaperScissor)

    def retranslateUi(self, RockPaperScissor):
        _translate = QtCore.QCoreApplication.translate
        RockPaperScissor.setWindowTitle(_translate("RockPaperScissor", "MainWindow"))
        self.appName.setText(_translate("RockPaperScissor", "Rock Paper Scissor"))
        self.resultText.setText(_translate("RockPaperScissor", "Who Will WIN !!!"))
        self.reset.setText(_translate("RockPaperScissor", "Reset"))
        self.vsText.setText(_translate("RockPaperScissor", "VS"))
        self.userScore.setText(_translate("RockPaperScissor", "0"))
        self.PC_Score.setText(_translate("RockPaperScissor", "0"))
        self.rock.setText(_translate("RockPaperScissor", "Rock"))
        self.paper.setText(_translate("RockPaperScissor", "Paper"))
        self.scissors.setText(_translate("RockPaperScissor", "Scissors"))
