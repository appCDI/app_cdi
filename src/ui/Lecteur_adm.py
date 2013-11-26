'''
Created on 26 nov. 2013

@author: niho
'''
from PyQt4 import QtGui
import Lecteur
import sys

class Lecteur_adm(Lecteur.Lecteur):
    '''
    classdocs
    '''

    def __init__(self):
        super().__init__()
        self.setupActionsAdm()
        self.setupMenusAdm()
        
    def gestion(self):
        QtGui.QMessageBox.Information(self, "Yeah", "interface admin gestion poeme")
        
    def setupActionsAdm(self):
        self.gestionAction = QtGui.QAction("&Gestion",self, triggered=self.gestion)
        
    def setupMenusAdm(self):
        editMenu = self.menuBar().addMenu("&Edition")
        editMenu.addAction(self.gestionAction)
        

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Lecteur de poeme")
    app.setQuitOnLastWindowClosed(True)
    
    window = Lecteur_adm()
    window.show()
    
    sys.exit(app.exec_())    
    
        
