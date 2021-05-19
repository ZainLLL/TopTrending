from datetime import datetime
from sys import argv,exit
from shutil import copy
from qdarkstyle import load_stylesheet_pyqt5
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QListWidgetItem, QMainWindow, QWidget ,QMessageBox

from info import grab_info, generat_img
from MyItem import Ui_Form
from window import Ui_MainWindow


wb = 'sina'
zh = 'zhihu'
bd = 'baidu'
t = 'title'
v = 'val'
l = 'link'

sites = [wb,zh,bd]
infos = {i:{x:[] for x in [t,v,l]} for i in sites}  # t:titles v:vals l:links
times = {'wb':str, 'zh':str, 'bd':str}

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.currentIndexChanged.connect(self.sitechange)
        self.btn1.clicked.connect(self.btn1clicked)
        self.btn2.clicked.connect(self.btn2clicked)
        self.btn3.clicked.connect(self.btn3clicked)

        self.lists = {wb: self.wblist, zh: self.zhlist, bd: self.bdlist}
        for site in sites:
            self.lists[site].itemDoubleClicked.connect(self.showBrowser)
            grab_info(site, infos[site])
            time = datetime.now()
            times[site]=time.strftime("%Y-%m-%d %H:%M")
            self.listshow(site)

        self.RefreshButton.clicked.connect(self.refresh)
        
        # TODO:add the button function
        self.geneButton.clicked.connect(self.PicGen)
        self.saveButton.clicked.connect(self.PicSave)

    def PicGen(self):
        site = sites[self.comboBox2.currentIndex()]
        if site != zh:
            vals = [int(x) if x.isdigit() else 3000000 for x in infos[site][v]]
        else:
            vals = [x[:-1] for x in infos[site][v]]
            vals = [int(x) if x.isdigit() else 10 for x in infos[site][v]]
        freq=dict(zip(infos[site][t],vals))
        if generat_img(freq):
            self.img_label.setPixmap(QPixmap("./img/wordcloud.jpg").scaled(self.img_label.sizeHint()))
        else:
            self.img_label.setText("生成失败，请重试")
    
    def PicSave(self):
        site = sites[self.comboBox2.currentIndex()]
        src_f = "./img/wordcloud.jpg"
        name = times[site][5:]
        name = name.replace(' ', '-')
        name=site+name.replace(':','')
        dst_f = "./output/" + name + ".jpg"
        copy(src_f, dst_f)
        QMessageBox.about(self,"TopTrending","图片\n保存成功")
        # self.box.setWindowIcon(self.icon)

        
    def showBrowser(self):
            self.browser=Newwindow(self.comboBox.currentText())
            site = self.stackedWidget.currentWidget().objectName()
            i = self.lists[site].currentRow()
            self.browser.UiInit(infos[site][l][i])
            self.browser.show()

    def listshow(self, site):
        self.time_label.setText(times[site])
        qlist = self.lists[site]
        # texts = sorted(freq[site].items(), key=lambda x: x[1] if isinstance(x[1], int) else int(x[1][:-1]), reverse=True)
        titles = list(infos[site][t])
        vals = list(infos[site][v])
        for i in range(len(titles)):
            item = QListWidgetItem()
            qlist.addItem(item)
            if site == wb:
                if i != 0:
                    wid = Form(str(i), titles[i], vals[i])
                else:
                    wid = Form("↑", titles[i], "")
            else:
                wid = Form(str(i+1),titles[i], vals[i])
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
        grab_info(site, infos[site])
        time = datetime.now()
        times[site]=time.strftime("%Y-%m-%d %H:%M")
        self.lists[site].clear()
        self.listshow(site)
        # print("refresh success!")


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
    app = QApplication(argv)
    w = MainWindow()
    app.setStyleSheet(load_stylesheet_pyqt5())
    w.show()
    # print(w.size().height())
    exit(app.exec_())
