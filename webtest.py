from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)

browser = QWebEngineView()
browser.load(QUrl("https://blog.csdn.net/s_daqing"))
browser.show()
sys.exit(app.exec_())