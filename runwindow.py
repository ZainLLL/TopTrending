import sys
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow
from window import Ui_MainWindow
import info
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

freq={'wb': {}, 'zh': {}, 'bd': {}}
urllist = {'wb': [], 'zh': [], 'bd': []}

class myForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.btn1.clicked.connect(self.btn1clicked)
        self.btn2.clicked.connect(self.btn2clicked)
        self.btn3.clicked.connect(self.btn3clicked)
        # self.btn4.clicked.connect(self.btn4clicked)

        self.wblist.itemDoubleClicked.connect(self.showBrowser)
        self.zhlist.itemDoubleClicked.connect(self.showBrowser)
        self.bdlist.itemDoubleClicked.connect(self.showBrowser)
        
        self.listinit()

    def showBrowser(self):
        self.browser=Newwindow()
        i = self.wblist.currentRow()
        page=self.stackedWidget.currentWidget().objectName()
        self.browser.UiInit(urllist[page][i])
        self.browser.show()

    def listinit(self):
        self.wblist.addItems(freq['wb'].keys())
        self.zhlist.addItems(freq['zh'].keys())
        self.bdlist.addItems(freq['bd'].keys())

    def selectionchange(self,i):
        self.stackedWidget.setCurrentIndex(i)
        # print(self.stackedWidget.currentWidget().objectName())

    def btn1clicked(self):
        self.Rpage.setCurrentIndex(0)
    def btn2clicked(self):
        self.Rpage.setCurrentIndex(1)
    def btn3clicked(self):
        self.Rpage.setCurrentIndex(2)


class Newwindow(QWebEngineView):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('微博热搜')
        self.resize(800, 600)
    
    def UiInit(self,str='https://www.zhihu.com/billboard/'):
        self.load(QUrl(str))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    for site in freq.keys():
        info.grab_info(site,freq[site], urllist[site])
    
    # print(items)
    w = myForm()
    w.show()
    sys.exit(app.exec_())