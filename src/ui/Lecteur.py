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


    def __init__(self, params):
        super(QtGui.QMainWindow,self).__init()
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory(), self)
        self.mediaObject = Phonon.MediaObject(self)
        self.setupUi()
        self.setupAction()
        
    def setupUi(self):
        self.volumeSlider = Phonon.VolumeSlider(self)
        self.volumeSlider.setAudioOutput(self.audioOutput)
        self.volumeSlider.setMaximumSize(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        
    def setupActions(self):
        
    
    
        