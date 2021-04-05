import sys
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow
from window import Ui_MainWindow
import info
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import qdarkstyle
import datetime

sites=['wb','zh','bd']
freq={'wb': {}, 'zh': {}, 'bd': {}}
urllist = {'wb': [], 'zh': [], 'bd': []}
times = {'wb':str, 'zh':str, 'bd':str}

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.currentIndexChanged.connect(self.sitechange)
        self.btn1.clicked.connect(self.btn1clicked)
        self.btn2.clicked.connect(self.btn2clicked)
        self.btn3.clicked.connect(self.btn3clicked)

        self.lists = {'wb': self.wblist, 'zh': self.zhlist, 'bd': self.bdlist}
        for site in sites:
            self.lists[site].itemDoubleClicked.connect(self.showBrowser)
            info.grab_info(site, freq[site], urllist[site])
            time = datetime.datetime.now()
            times[site]=time.strftime("%Y-%m-%d %H:%M")
            self.listshow(site)

        self.RefreshButton.clicked.connect(self.refresh)
        
        
    def showBrowser(self):
        self.browser=Newwindow()
        i = self.wblist.currentRow()
        site=self.stackedWidget.currentWidget().objectName()
        self.browser.UiInit(urllist[site][i])
        self.browser.show()

    def listshow(self, site):
        self.time_label.setText(times[site])
        self.lists[site].addItems(freq[site].keys())

    def sitechange(self,i):
        self.stackedWidget.setCurrentIndex(i)
        site=self.stackedWidget.currentWidget().objectName()
        self.time_label.setText(times[site])

    def btn1clicked(self):
        self.Rpage.setCurrentIndex(0)
    def btn2clicked(self):
        self.Rpage.setCurrentIndex(1)
    def btn3clicked(self):
        self.Rpage.setCurrentIndex(2)
    
    def refresh(self):
        site=self.stackedWidget.currentWidget().objectName()
        info.grab_info(site, freq[site], urllist[site])
        time = datetime.datetime.now()
        times[site]=time.strftime("%Y-%m-%d %H:%M:%S")
        self.lists[site].clear()
        self.listshow(site)
        print("refresh success!")



class Newwindow(QWebEngineView):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle('微博热搜')
        self.resize(800, 600)
    
    def UiInit(self,str='https://www.zhihu.com/billboard/'):
        self.load(QUrl(str))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    w.show()
    sys.exit(app.exec_())