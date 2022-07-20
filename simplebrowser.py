# first pip install PyQt5 and pip install PyQtWebEngine
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

# creating class
class MyWebBrowser():
    # constructor
    def __init__(self):
        #setting the max height
        maxHeight = 30

        #setting default url
        defUrl = "https://www.google.com"

        # setting gui
        self.window = QWidget()
        self.window.setWindowTitle("Browser Test")

        # setting the layout of the window
        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        # create btns
        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(maxHeight)
        self.go_btn = QPushButton("Go")
        self.go_btn.setMaximumHeight(maxHeight)
        self.back_btn = QPushButton("<")
        self.back_btn.setMaximumHeight(maxHeight)
        self.for_btn = QPushButton(">")
        self.for_btn.setMaximumHeight(maxHeight)

        # add btns to horizontal layout
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.for_btn)

        # create browser
        self.browser = QWebEngineView()

        # when buttons clicked
        # go btn clicked it takes whats in navbar, lambda makes it so it doesnt execute unless called
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.for_btn.clicked.connect(self.browser.forward)

        # add browser to layout
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        # set default URL
        self.browser.setUrl(QUrl(defUrl))

        # create and display window
        self.window.setLayout(self.layout)
        self.window.show()

    # funtion for the nav bar
    def navigate(self, url):
        # in case it doesnt have http
        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))


# application functionality
app = QApplication([])
window = MyWebBrowser()

app.exec()
