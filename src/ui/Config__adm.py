'''
Created on 2 déc. 2013

@author: niho
'''
from PyQt4 import QtGui

class Config_adm(QtGui.QDialog):
    '''
    classdocs
    '''
    

    def __init__(self, params):
        super.setupAction()
        super.setupUi()
        
    def setupAction(self):
        super.save = QAction()
        super.modify = QAction()
        super.delete = QAction()
    
    def setupUi(self):
        
        
        
        