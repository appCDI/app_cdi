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
        
        self.mediaObject.setTickInterval(1000)
        
        self.mediaObject.stateChanged.connect(self.stateChanged)
        self.mediaObject.currentSourceChanged.connect(self.sourceChanged)
        self.mediaObject.aboutToFinish.connect(self.aboutToFinish)
        
        Phonon.createPath(self.mediaObject, self.audioOutput)
        
        self.setupActions()
        self.setupMenus()
        self.setupUi()
        
        self.sources = []
        
    def about(self):
        QtGui.QMessageBox.information(self, "A propos de l'application",
                "Cette Application a été conçu pour le Lycée Paul Louis Courrier"
                "par les étudiants en BTS SIO à l'occasion du printemps des "
                "poetes.")

    def stateChanged(self, newState, oldState):
        if newState == Phonon.ErrorState:
            if self.mediaObject.errorType() == Phonon.FatalError:
                QtGui.QMessageBox.warning(self, "Fatal Error",
                        self.mediaObject.errorString())
            else:
                QtGui.QMessageBox.warning(self, "Error",
                        self.mediaObject.errorString())

        elif newState == Phonon.PlayingState:
            self.playAction.setEnabled(False)
            self.pauseAction.setEnabled(True)
            self.stopAction.setEnabled(True)

        elif newState == Phonon.StoppedState:
            self.stopAction.setEnabled(False)
            self.playAction.setEnabled(True)
            self.pauseAction.setEnabled(False)

        elif newState == Phonon.PausedState:
            self.pauseAction.setEnabled(False)
            self.stopAction.setEnabled(True)
            self.playAction.setEnabled(True)
    
    def tableClicked(self, row, column):
        wasPlaying = (self.mediaObject.state() == Phonon.PlayingState)

        self.mediaObject.stop()
        self.mediaObject.clearQueue()

        self.mediaObject.setCurrentSource(self.sources[row])

        if wasPlaying:
            self.mediaObject.play()
        else:
            self.mediaObject.stop()
            
    def sourceChanged(self, source):
        self.musicTable.selectRow(self.sources.index(source))

    def aboutToFinish(self):
        index = self.sources.index(self.mediaObject.currentSource()) + 1
        if len(self.sources) > index:
            self.mediaObject.enqueue(self.sources[index])
    
    def setupActions(self):
        self.playAction = QtGui.QAction(
                self.style().standardIcon(QtGui.QStyle.SP_MediaPlay),"Play",
                self,shortcut="Ctrl+P", enabled=False,
                triggered=self.mediaObject.play)
        
        self.pauseAction = QtGui.QAction(
                self.style().standardIcon(QtGui.QStyle.SP_MediaPause),
                "Pause",self,shortcut="Ctrl+A", enabled=False,
                triggered=self.mediaObject.pause)
        
        self.stopAction = QtGui.QAction(
                self.style().standardIcon(QtGui.QStyle.SP_MediaStop), "Stop",
                self, shortcut="Ctrl+S", enabled=False,
                triggered=self.mediaObject.stop)
        
        self.nextAction = QtGui.QAction(
                self.style().standardIcon(QtGui.QStyle.SP_MediaSkipForward),
                "Next", self, shortcut="Ctrl+N")
        
        self.previousAction = QtGui.QAction(
                self.style().standardIcon(QtGui.QStyle.SP_MediaSkipBackward),
                "Previous", self, shortcut="Ctrl+R")
        
        #self.searchAction = QtGui.QAction("Search", self, triggered=self.search)
        
        self.exitAction = QtGui.QAction("Quitter", self, shortcut="Ctrl+Q",
                                        triggered=self.close)
        self.aboutAction = QtGui.QAction("A Propos", self, triggered=self.about)
    
    def setupMenus(self):
        fileMenu = self.menuBar().addMenu("&Fichier")
        fileMenu.addAction(self.exitAction)
        
        aboutMenu = self.menuBar().addMenu("&Aide")
        aboutMenu.addAction(self.aboutAction)
            
    def setupUi(self):
        searchLabel = QtGui.QLabel("Rechercher : ")
        searchLine = QtGui.QLineEdit()
        searchButton = QtGui.QPushButton("Go")
        
        searchList = ("Titre","Auteur", "Thème", "Siècle", "Genre", 
                   "Langue","Elève")
        searchBox = QtGui.QComboBox()
        searchBox.addItems(searchList)
        
        
        bar = QtGui.QToolBar()
        bar.addAction(self.playAction)
        bar.addAction(self.pauseAction)
        bar.addAction(self.stopAction)
        
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
        self.poemeTab.setHorizontalHeaderLabels(headers)
        self.poemeTab.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.poemeTab.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.poemeTab.cellPressed.connect(self.tableClicked)
        
        searchLayout = QtGui.QHBoxLayout()
        searchLayout.addWidget(searchLabel)
        searchLayout.addWidget(searchLine)
        searchLayout.addWidget(searchBox)
        searchLayout.addWidget(searchButton)
        
        seekerLayout = QtGui.QHBoxLayout()
        seekerLayout.addWidget(self.seekSlider)
        
        playbackLayout = QtGui.QHBoxLayout()
        playbackLayout.addWidget(bar)
        playbackLayout.addStretch()
        playbackLayout.addWidget(volumeLabel)
        playbackLayout.addWidget(self.volumeSlider)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addLayout(searchLayout)
        mainLayout.addWidget(self.poemeTab)
        mainLayout.addLayout(seekerLayout)
        mainLayout.addLayout(playbackLayout)
        
        widget = QtGui.QWidget()
        widget.setLayout(mainLayout)

        self.setCentralWidget(widget)
        self.setWindowTitle("Printemps des poetes - Lecteur")
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Lecteur de poeme")
    app.setQuitOnLastWindowClosed(True)
    
    window = Lecteur()
    window.show()
    
    sys.exit(app.exec_())    
    
        
    
    
        