import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
import test
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(self.run)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')    
        self.show()

    def run(self):
        self.browser = Newwindow()
        self.load(QUrl("https://blog.csdn.net/s_daqing"))

        self.browser.show()

class Newwindow(QWebEngineView):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('新窗口')
        self.resize(280, 230)
        # self.load(QUrl("https://blog.csdn.net/s_daqing"))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())