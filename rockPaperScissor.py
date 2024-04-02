import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# from RockPaperScissorGUI_finished import Ui_MainWindow
from PyQt5.QtGui import QPixmap, QIcon, QRegExpValidator
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer, QRegExp
import random as rd


class MyLoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loadUi("Resources/UserLoginGUI.ui", self)

        restriction_for_only_letters = QRegExp("[a-zA-Z\u10D0-\u10FA]+")
        validator = QRegExpValidator(restriction_for_only_letters)
        self.user_firstname.setValidator(validator)
        self.user_lastname.setValidator(validator)

        self.submit.setShortcut("Return")
        self.submit.clicked.connect(self.start_app)

    def start_app(self):
        user_firstname = self.user_firstname.text()
        user_lastname = self.user_lastname.text()

        if user_firstname != '' and user_lastname != '':
            self.close()
            MyMainWindow(user_firstname, user_lastname).show()


class MyMainWindow(QMainWindow):
    def __init__(self, firstname, lastname):
        super().__init__()
        # Set up the UI
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        
        loadUi("Resources/RockPaperScissorGUI_finished.ui", self)

        self.user_firstname = firstname
        self.user_lastname = lastname
        self.images = ["Resources/scissors.png", "Resources/paper.png", "Resources/rock.png"]
        self.all_options = [self.rock, self.paper, self.scissors, self.reset]
        self.user_win_texts = ["Ha Ha You WON... !"]
        self.pc_win_texts = ["Sorry But NO LUCK..."]
        self.draw_texts = ["Nice Try But It's a draw !"]
        
        self.total_animation_cycles = 10
        self.animation_speed = 150
        self.cycle_count = 0
        self.current_pc_image = 'None'
        self.current_user_image = 'None'

        self.setWindowTitle("Rock Paper Scissor Game")
        self.setWindowIcon(QIcon("Resources/icon.png"))
        self.userImg.setScaledContents(True)
        self.userImg.setPixmap(QPixmap("Resources/user_icon.png").scaled(740, 1002))
        
        self.computerImg.setScaledContents(True)
        self.computerImg.setPixmap(QPixmap("Resources/pc_icon.png"))

        for option in self.all_options:
            option.setCursor(Qt.CursorShape.PointingHandCursor)

        self.rock.clicked.connect(lambda: self.user_option_choose(self.rock))
        self.paper.clicked.connect(lambda: self.user_option_choose(self.paper))
        self.scissors.clicked.connect(lambda: self.user_option_choose(self.scissors))
        self.reset.clicked.connect(self.reset_results)


    def user_option_choose(self, option):
        self.userImg.setScaledContents(True)
        self.userImg.setPixmap(QPixmap(f"Resources/{option.text()}.png").scaled(740, 1002))
        self.current_user_image = f"Resources/{option.text()}.png".lower()

        self.cycle_count = 0

        self.choosing_animation()

    def disable_buttons(self):
        for item in self.all_options:
            item.setEnabled(False)
            if item.text() == 'Reset':
                item.setStyleSheet("background-color: rgba(255,0,0,0.3);")
                continue
            item.setStyleSheet("background-color: rgba(66, 165, 116, 0.3);")
    
    def enable_buttons(self):
        for item in self.all_options:
            item.setEnabled(True)
            if item.text() == 'Reset':
                item.setStyleSheet("background-color: rgba(255,0,0,0.7);")
                continue
            item.setStyleSheet("background-color: rgba(66, 165, 116, 0.7);")
    
    def reset_results(self):
        self.resultText.setText("Who Will WIN !!!")

        self.userImg.setScaledContents(True)
        self.userImg.setPixmap(QPixmap("Resources/user_icon.png").scaled(740, 1002))
        self.computerImg.setScaledContents(True)
        self.computerImg.setPixmap(QPixmap("Resources/pc_icon.png"))

        self.PC_Score.setText('0')
        self.userScore.setText('0')

    def animation_end_results(self):
        if self.current_pc_image == self.current_user_image:
            self.resultText.setText(rd.choice(self.draw_texts))
        elif self.current_user_image == "rock.png":
            if self.current_pc_image == "paper.png":
                self.PC_Score.setText(str(int(self.PC_Score.text())+1))
                self.resultText.setText(rd.choice(self.pc_win_texts))
            elif self.current_pc_image == "scissors.png":
                self.userScore.setText(str(int(self.userScore.text())+1))
                self.resultText.setText(rd.choice(self.user_win_texts))
        elif self.current_user_image == "paper.png":
            if self.current_pc_image == "rock.png":
                self.userScore.setText(str(int(self.userScore.text())+1))
                self.resultText.setText(rd.choice(self.user_win_texts))
            elif self.current_pc_image == "scissors.png":
                self.PC_Score.setText(str(int(self.PC_Score.text())+1))
                self.resultText.setText(rd.choice(self.pc_win_texts))
        elif self.current_user_image == "scissors.png":
            if self.current_pc_image == "rock.png":
                self.PC_Score.setText(str(int(self.PC_Score.text())+1))
                self.resultText.setText(rd.choice(self.pc_win_texts))
            elif self.current_pc_image == "paper.png":
                self.userScore.setText(str(int(self.userScore.text())+1))
                self.resultText.setText(rd.choice(self.user_win_texts))

    def animation_end_check(self):
        if self.cycle_count == self.total_animation_cycles+1:
            self.computerImg.setScaledContents(True)
            self.computerImg.setPixmap(QPixmap(self.current_pc_image).scaled(740, 1002))
            self.timer.stop()
            self.animation_end_results()
            self.enable_buttons()

    def choosing_animation(self):
        self.disable_buttons()
        self.resultText.setText("Who Will WIN !!!")
        self.timer = QTimer()
        self.timer.timeout.connect(self.change_image)
        self.change_image()
        self.timer.start(self.animation_speed)

    def change_image(self):
        self.set_image()
        self.cycle_count += 1
        self.animation_end_check()

    def set_image(self):
        image = rd.choice(self.images)
        while True:
            if self.current_pc_image != image:
                pixmap = QPixmap(image)
                self.computerImg.setPixmap(pixmap.scaled(self.size(), aspectRatioMode=Qt.KeepAspectRatio))
                self.current_pc_image = image;
                break
            else:
                image = rd.choice(self.images)


if __name__ == "__main__":
    # Create the application instance
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MyLoginWindow()
    window.show()

    # Run the application event loop
    app.exec_()
    