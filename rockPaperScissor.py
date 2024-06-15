import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
# from RockPaperScissorGUI_finished import Ui_MainWindow
from PyQt5.QtGui import QPixmap, QIcon, QRegExpValidator
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer, QRegExp
from Resources.IncorrectUserGUI import Ui_Dialog
from Resources.RockPaperScissorGUI import Ui_RockPaperScissor
from Resources.UserLoginGUI import Ui_UserLogin
import random as rd
from PasswordChecker import valid_new_user_password, is_password_okay
from DatabaseFunctions import test_database_connection, table_exists, add_single_query, username_availability, search_user

class IncorrectUser(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

class MyLoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_UserLogin()
        self.ui.setupUi(self)
        # loadUi("Resources/UserLoginGUI.ui", self)

        self.database_connection = test_database_connection()
        if self.database_connection == True:
            pass    
        else:
            pass

        self.table_name = 'RockPaperScissorsUsers'
        table_exists(self.table_name)

        self.curr_state = 'register' #Login/Register
        self.change_login_state() #To make Login Window By Default


        # restriction_for_only_letters = QRegExp("[a-zA-Z\u10D0-\u10FA]+")
        validator_for_text = QRegExpValidator(QRegExp("^[a-zA-Z0-9_ა-ჰ]+$"))
        self.ui.user_firstname.setValidator(validator_for_text)
        self.ui.user_lastname.setValidator(validator_for_text)
        self.ui.user_username.setValidator(validator_for_text)
        validator_for_password = QRegExpValidator(QRegExp("^[a-zA-Z0-9_]+$"))
        self.ui.user_password.setValidator(validator_for_password)

        #Adding method to start app by 'Enter' button.
        self.ui.register_button.clicked.connect(self.change_login_state)

        self.ui.submit.setShortcut("Return")
        self.ui.submit.clicked.connect(self.start_app)
        
    
    def change_login_state(self):
        if self.curr_state == 'login':
            self.curr_state = 'register'
            #Reset If something was written
            self.ui.user_firstname.setText('')
            self.ui.user_lastname.setText('')
            self.ui.user_password.setText('')
            self.ui.user_username.setText('')

            self.ui.user_firstname_frame.setHidden(False)
            self.ui.user_lastname_frame.setHidden(False)
            self.ui.user_password.setPlaceholderText('Create Password')
            self.ui.register_question.setText('Have an account?')
            self.ui.register_question.setFixedWidth(250)
            self.ui.register_button.setText('Login')

        elif self.curr_state == 'register': #initial state
            self.curr_state = 'login'
            #Reset If something was written
            self.ui.user_firstname.setText('')
            self.ui.user_lastname.setText('')
            self.ui.user_password.setText('')
            self.ui.user_username.setText('')

            self.ui.register_question.setText('Do not have an account? ')
            self.ui.register_question.setFixedWidth(265)
            self.ui.register_button.setText('Register')
            self.ui.user_password.setPlaceholderText('Password')
            self.ui.user_firstname_frame.setHidden(True)
            self.ui.user_lastname_frame.setHidden(True)
            

    def start_app(self):
        # TO DO connection to database and searching for user + saving it's stats.
        # TO DO Connection is Done !
        # TO DO Login is Done !
        # TO DO Register need to be Done ! (Usernmae availability check + GUI s)

        if self.curr_state == 'login':
            user_username = self.ui.user_username.text()
            user_password = self.ui.user_password.text()
            user = search_user(self.table_name, (user_username, user_password))
            
            if user != None: #Means that user exists
                print("Logged In Succesfully!")
                self.close()
                MyMainWindow(user_obj=user,
                             database_connected=self.database_connection,
                             table_name=self.table_name).show()
            else:
                #popup for not available profile
                # self.close()
                incorrect_user = IncorrectUser()
                incorrect_user.exec_()
                print("User Not Found")

        elif self.curr_state == 'register':
            user_username = self.ui.user_username.text()
            user_password = self.ui.user_password.text()
            password_policy = valid_new_user_password(user_password)
            password_validity = is_password_okay(password_policy)

            if username_availability(self.table_name, user_username) == True:
                #To Do - Change this so we check username availability first but
                #we add username after we check password is valid.
                if not password_validity:
                    print('Not valid password')
                    return
                else: 
                   self.add_user_to_database()
            else:
                #popup for not available username
                print('username already in use ')
                return 

            user = search_user(self.table_name, (user_username, user_password))
            if user != None: #Ensures that user added successfully
                self.close()
                MyMainWindow(user_obj=user,
                            database_connected=self.database_connection,
                            table_name=self.table_name).show()

    def add_user_to_database(self):
        add_single_query(self.table_name, (self.ui.user_firstname.text(),
                                            self.ui.user_lastname.text(),
                                            self.ui.user_username.text(),
                                            self.ui.user_password.text(),
                                            0,
                                            0))
        print(f'Table: {self.table_name}')


class MyMainWindow(QMainWindow):
    def __init__(self, user_obj, database_connected, table_name):
        super().__init__()
        self.ui = Ui_RockPaperScissor()
        self.ui.setupUi(self)

        self.user_obj = user_obj
        self.database_connected = database_connected
        self.table_name = table_name 
        # loadUi("Resources/RockPaperScissorGUI_finished.ui", self)
        
        self.import_user()
        
        self.resources = {
            'images': {
                'scissors': "Resources/scissors.png",
                'paper': "Resources/paper.png",
                'rock': "Resources/rock.png"
            },
            'finishing_texts': {
                'user_win_texts': ["Ha Ha You WON... !"],
                'pc_win_texts': ["Sorry But NO LUCK..."],
                'draw_texts': ["Nice Try But It's a draw !"]
            }
        }
        # self.images = ["Resources/scissors.png", "Resources/paper.png", "Resources/rock.png"]
        self.all_options = [self.ui.rock, self.ui.paper, self.ui.scissors, self.ui.reset]
        
        self.total_animation_cycles = 10
        self.animation_speed = 150
        self.cycle_count = 0
        self.current_pc_image = 'None'
        self.current_user_image = 'None'

        self.setWindowTitle("Rock Paper Scissor Game")
        self.setWindowIcon(QIcon("Resources/icon.png"))
        self.ui.userImg.setScaledContents(True)
        self.ui.userImg.setPixmap(QPixmap("Resources/user_icon.png").scaled(740, 1002))
        
        self.ui.computerImg.setScaledContents(True)
        self.ui.computerImg.setPixmap(QPixmap("Resources/pc_icon.png"))

        for option in self.all_options:
            option.setCursor(Qt.CursorShape.PointingHandCursor)

        self.ui.rock.clicked.connect(lambda: self.user_option_choose(self.ui.rock))
        self.ui.paper.clicked.connect(lambda: self.user_option_choose(self.ui.paper))
        self.ui.scissors.clicked.connect(lambda: self.user_option_choose(self.ui.scissors))
        self.ui.reset.clicked.connect(self.reset_results)

    def closeEvent(self, event):
        #To Do - Make Custom Dialog Window - Import - Change To "Saving..."
        reply = QMessageBox.question(
            self,
            'Message',
            "Do you want to save your progress?",
            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
            QMessageBox.Cancel
        )

        if reply == QMessageBox.Yes:
            self.save_progress()
            event.accept()
        elif reply == QMessageBox.No:
            event.accept()
        else:
            event.ignore()

    # def save_progress(self):
    #     # Implement your save functionality here
    #     print("Progress saved")

    def user_option_choose(self, option):
        self.ui.userImg.setScaledContents(True)
        self.ui.userImg.setPixmap(QPixmap(f"Resources/{option.text()}.png").scaled(740, 1002))
        self.current_user_image = f"Resources/{option.text().lower()}.png"

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
        self.ui.resultText.setText("Who Will WIN !!!")

        self.ui.userImg.setScaledContents(True)
        self.ui.userImg.setPixmap(QPixmap("Resources/user_icon.png").scaled(740, 1002))
        self.ui.computerImg.setScaledContents(True)
        self.ui.computerImg.setPixmap(QPixmap("Resources/pc_icon.png"))

        self.ui.PC_Score.setText('0')
        self.ui.userScore.setText('0')

    def animation_end_results(self):
        if self.current_pc_image == self.current_user_image:
            self.ui.resultText.setText(rd.choice(self.resources['finishing_texts']['draw_texts']))
        elif self.current_user_image == "Resources/rock.png":
            if self.current_pc_image == "Resources/paper.png":
                self.ui.PC_Score.setText(str(int(self.ui.PC_Score.text())+1))
                self.ui.resultText.setText(rd.choice(self.resources['finishing_texts']['pc_win_texts']))
            elif self.current_pc_image == "Resources/scissors.png":
                self.ui.userScore.setText(str(int(self.ui.userScore.text())+1))
                self.ui.resultText.setText(rd.choice(self.resources['finishing_texts']['user_win_texts']))
        elif self.current_user_image == "Resources/paper.png":
            if self.current_pc_image == "Resources/rock.png":
                self.ui.userScore.setText(str(int(self.ui.userScore.text())+1))
                self.ui.resultText.setText(rd.choice(self.resources['finishing_texts']['user_win_texts']))
            elif self.current_pc_image == "Resources/scissors.png":
                self.ui.PC_Score.setText(str(int(self.ui.PC_Score.text())+1))
                self.ui.resultText.setText(rd.choice(self.resources['finishing_texts']['pc_win_texts']))
        elif self.current_user_image == "Resources/scissors.png":
            if self.current_pc_image == "Resources/rock.png":
                self.ui.PC_Score.setText(str(int(self.ui.PC_Score.text())+1))
                self.ui.resultText.setText(rd.choice(self.resources['finishing_texts']['pc_win_texts']))
            elif self.current_pc_image == "Resources/paper.png":
                self.ui.userScore.setText(str(int(self.ui.userScore.text())+1))
                self.ui.resultText.setText(rd.choice(self.resources['finishing_texts']['user_win_texts']))

    def animation_end_check(self):
        if self.cycle_count == self.total_animation_cycles+1:
            self.ui.computerImg.setScaledContents(True)
            self.ui.computerImg.setPixmap(QPixmap(self.current_pc_image).scaled(740, 1002))
            self.timer.stop()
            self.animation_end_results()
            self.enable_buttons()

    def choosing_animation(self):
        self.disable_buttons()
        self.ui.resultText.setText("Who Will WIN !!!")
        self.timer = QTimer()
        self.timer.timeout.connect(self.change_image)
        self.change_image()
        self.timer.start(self.animation_speed)

    def change_image(self):
        self.set_image()
        self.cycle_count += 1
        self.animation_end_check()

    def set_image(self):
        image = rd.choice(list(self.resources['images'].values()))
        while True:
            if self.current_pc_image != image:
                pixmap = QPixmap(image)
                self.ui.computerImg.setPixmap(pixmap.scaled(self.size(), aspectRatioMode=Qt.KeepAspectRatio))
                self.current_pc_image = image;
                break
            else:
                image = rd.choice(list(self.resources['images'].values()))

    def import_user(self):
        self.ui.user_firstname = self.user_obj.firstname
        self.ui.user_lastname = self.user_obj.lastname
        self.username = self.user_obj.username
        self.ui.user_password = self.user_obj.password
        self.ui.userScore.setText(str(self.user_obj.user_score))
        self.ui.PC_Score.setText(str(self.user_obj.PC_score))

        print(self.user_obj)


if __name__ == "__main__":
    # Create the application instance
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MyLoginWindow()
    window.show()
    # user = search_user('RockPaperScissorsUsers', ('1', '1'))
    # window = MyMainWindow(user_obj=user,
    #                     database_connected=True,
    #                     table_name='RockPaperScissorsUsers')
    # window.show()

    # Run the application event loop
    sys.exit(app.exec_())
    