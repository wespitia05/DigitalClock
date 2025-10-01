# python pyqt5 digital clock

# provides modules used and maintained by the python interpreter
import sys
# provides gui components
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
# provides functionality
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    # within this method we will be constructing all of the different entities for the program
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self) # displays the time
        self.timer = QTimer(self) # adds timer to the clock
        self.initUI()
    
    # within this method we will design the layout for the program
    def initUI(self):
        self.setWindowTitle("Digital Clock") # sets title of the window
        self.setGeometry(600, 400, 300, 100) # x, y, width, height

        vbox = QVBoxLayout() # arranges all of our widgets vertically
        vbox.addWidget(self.time_label) # adds time label widget
        self.setLayout(vbox) # sets layout that applies to our clock

        self.time_label.setAlignment(Qt.AlignCenter) # center aligns our time

        # css properties for the time label
        self.time_label.setStyleSheet("font-size: 125px;"
                                      "color: #26ff00;")
        # css properties for the window
        self.setStyleSheet("background: black;")

        font_id = QFontDatabase.addApplicationFont("/Users/william/Documents/Bro Code Digital Clock/BroCodeDigitalClock/DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0] # retrieves first element of the family
        my_font = QFont(font_family, 150) # font family, font size
        self.time_label.setFont(my_font) # sets font for the time label

        self.timer.timeout.connect(self.update_time) # will connect to the update time function
        self.timer.start(1000) # updates after every 1000 ms

        self.update_time() # calls update time function to display current time

    # this method will update the time
    def update_time(self):
        # get current time, change it to a string with 12:00:00 format AM/PM
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time) # sets current time to time label text

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show() # appears for a brief second
    sys.exit(app.exec_()) # allows window to stay in place until we exit