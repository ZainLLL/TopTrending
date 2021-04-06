import datetime
import sys

import qdarkstyle
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QListWidgetItem, QMainWindow, QWidget

import img_rc
import info
from MyItem import Ui_Form
from window import Ui_MainWindow

sites = ['wb', 'zh', 'bd']
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
        
        # TODO:add the button function
        self.geneButton.clicked.connect(self.PicGen)

    def PicGen(self):
        site = sites[self.comboBox2.currentIndex()]
        if info.generat_img(freq[site]):
            self.img_label.setPixmap(QPixmap("./img/wordcloud.jpg"))
        else:
            self.img_label.setText("生成失败，请重试")

        
    def showBrowser(self):
        self.browser=Newwindow(self.comboBox.currentText())
        site = self.stackedWidget.currentWidget().objectName()
        i = self.lists[site].currentRow()
        self.browser.UiInit(urllist[site][i])
        self.browser.show()

    def listshow(self, site):
        self.time_label.setText(times[site])
        qlist = self.lists[site]
        texts = sorted(freq[site].items(), key=lambda x: x[1] if isinstance(x[1], int) else int(x[1][:-1]), reverse=True)
        for i in range(len(texts)):
            item = QListWidgetItem()
            qlist.addItem(item)
            if site == "wb":
                if i != 0:
                    wid = Form(str(i), texts[i][0], texts[i][1])
                else:
                    wid = Form("↑", texts[i][0], "")
            else:
                wid = Form(str(i+1), texts[i][0], texts[i][1])
            item.setSizeHint(wid.sizeHint())
            # print(item.sizeHint().height())
            qlist.setItemWidget(item,wid)

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
        times[site]=time.strftime("%Y-%m-%d %H:%M")
        self.lists[site].clear()
        self.listshow(site)
        print("refresh success!")


class Newwindow(QWebEngineView):
    def __init__(self,text):
        super().__init__()
        self.setWindowTitle(text)
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap(":/img/img/logo.ico"))
        self.setWindowIcon(self.icon)
        self.resize(900, 600)
    
    def UiInit(self,str='https://www.zhihu.com/billboard/'):
        self.load(QUrl(str))
    

class Form(QWidget, Ui_Form):
    def __init__(self,num,title,val):
        super().__init__()
        self.setupUi(self)
        self.num.setText(num)
        self.title.setText(title)
        self.value.setText(str(val))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    w.show()
    sys.exit(app.exec_())
