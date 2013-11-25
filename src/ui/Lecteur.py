from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon
import sys

'''
Created on 25 nov. 2013
@author: niho
'''

class Lecteur(QtGui.QMainWindow):
    '''
    classdocs
    '''

    def __init__(self):
        super(QtGui.QMainWindow,self).__init__()
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.mediaObject = Phonon.MediaObject(self)
        self.setupActions()
        self.setupUi()
        
    def about(self):
        QtGui.QMessageBox.Information(self, "A propos de l'application",
                "Cette Application a été conçu pour le Lycée Paul Louis Courrier"
                "par les étudiants en BTS SIO à l'occasion du printemps des "
                "poetes.")
    
    def setupActions(self):
        self.playAction = QtGui.QAction(
                self.style().standardIcon(QtGui.QStyle.SP_MediaPlay),"Play",
                self,shortcut="Ctrl+P", enabled=False,
                triggered=self.mediaObject.play)
        #self.search = QtGui.QAction("Search", self, triggered=self.search)
        
        self.exitAction = QtGui.QAction("Quitter", self, shortcut="Ctrl+Q",
                                        triggered=self.close)
        self.aboutAction = QtGui.QAction("A Propos", self, triggered=self.about)
    
    def setupMenus(self):
        fileMenu = self.menuBar().addMenu("&Fichier")
        fileMenu.addAction(self.exitAction)
        
        aboutMenu = self.menuBar().addMenu("&Aide")
        aboutMenu.addAction(self.AboutAction)
            
    def setupUi(self):
        searchLabel = QtGui.QLabel("Rechercher : ")
        searchLine = QtGui.QLineEdit()
        searchButton = QtGui.QPushButton("Go")
        
        listeOptSearch = ("Titre","<<Auteur", "Thème", "Siècle", "Genre", 
                   "Langue","Elève")
        searchBox = QtGui.QComboBox()
        searchBox.addItems(listeOptSearch)
        
        
        bar = QtGui.QToolBar()
        bar.addAction(self.playAction)
        #bar.addAction(self.pauseAction)
        #bar.addAction(self.stopAction)
        
        self.seekSlider = Phonon.SeekSlider(self)
        self.seekSlider.setMediaObject(self.mediaObject)
        
        
        self.volumeSlider = Phonon.VolumeSlider(self)
        self.volumeSlider.setAudioOutput(self.audioOutput)
        self.volumeSlider.setMaximumSize(QtGui.QSizePolicy.Maximum, 
                                         QtGui.QSizePolicy.Maximum)
        
        volumeLabel = QtGui.QLabel()
        volumeLabel.setPixmap(QtGui.QPixmap('images/volume.png'))
        
        headers = ("Id","Titre","Auteur", "Thème", "Siècle", "Genre", 
                   "Langue","Elève")
        self.poemeTab = QtGui.QTableWidget(0,8)
        self.poemeTab.setHorizontalHeader(headers)
        
        self.setWindowTitle("Printemps des poetes - Lecteur")
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Lecteur de poeme")
    app.setQuitOnLastWindowClosed(True)
    
    window = Lecteur()
    window.show()
    
    sys.exit(app.exec_())    
    
        
    
    
        