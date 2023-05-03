#By Eucador
#UnderBrowser is a safe Browser with bare essentials for minimum tracking.
#It was coded by the programmer who calls himself Eucador (Yoo-ca-door).
#It was programmed in Python, using PyQt.
print("Launching UnderBrowser...")
print("Please Wait...")
#Import stuff
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        #Set the Browser Window Title
        self.setWindowTitle("UnderBrowser")
        self.setWindowIcon(QIcon('icons/icon.png'))
        self.setGeometry(000,000, 900,600)

        #create the toolbar for the buttons and URL search bar
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        

        #Create the Back button    
        self.backButton = QPushButton("<")
        self.backButton.setIcon(QIcon('icons/back.png'))
        self.backButton.clicked.connect(self.backBtn)
        toolbar.addWidget(self.backButton)
        
        #Create the Refresh Button
        self.reloadButton = QPushButton("%")
        self.reloadButton.clicked.connect(self.reloadBtn)
        toolbar.addWidget(self.reloadButton)

        #Create the Forward Button   
        self.forwardButton = QPushButton(">")
        self.forwardButton.setIcon(QIcon('icons/forward.png'))
        self.forwardButton.clicked.connect(self.forwardBtn)
        toolbar.addWidget(self.forwardButton)

        #Create the Home button
        self.homeButton = QPushButton("Home")
        self.homeButton.clicked.connect(self.homeBtn)
        toolbar.addWidget(self.homeButton)

        #Create the url search bar    
        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.setFont(QFont("Helvatica", 18))
        toolbar.addWidget(self.addressLineEdit)

        #Create the search button for url search bar
        self.searchButton = QPushButton("Search")
        self.searchButton.clicked.connect(self.searchBtn)
        toolbar.addWidget(self.searchButton)
        

        #Create the webengine view below the toolbar        
        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl = "https://www.duckduckgo.com"
        self.addressLineEdit.setText(initialUrl)
        self.webEngineView.load(QUrl(initialUrl))

    #what the search button does    
    def searchBtn(self):
        myurl = self.addressLineEdit.text()
        self.webEngineView.load(QUrl(myurl))

    #what the back button does    
    def backBtn(self):
        self.webEngineView.back()

    #what the forward button does    
    def forwardBtn(self):
        self.webEngineView.forward()

    #what the refresh button does    
    def reloadBtn(self):
        self.webEngineView.reload()

    #what the home button does    
    def homeBtn(self):
        self.webEngineView.load(QUrl('https://duckduckgo.com'))

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())