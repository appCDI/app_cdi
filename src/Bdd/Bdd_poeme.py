'''
Created on 18 nov. 2013

@author: niho
'''

from PyQt4 import QtSql, QtCore

class Bdd_poeme():
    '''
    classdocs
    '''

    def del_poeme(self,poeme):
        req = ""
        
        
    def save_poeme(self,poeme):
        req = ""
        
    def load_all_poeme(self):
        req = "SELECT * FROM POEME"
        return poemes
    
    def load_poeme_by_theme(self, theme):
        req = "SELECT DISTINCT * FROM POEME WHERE idTheme = ",theme.id_theme
        return poemes
    
    def load_one_poeme(self, poeme):
        req = "SELECT * FROM POEME WHERE idPoeme = ".poeme.id_theme
        return poeme
    
    def load_poeme_by_auteur(self, auteur):
        req = ""
        return poemes
    
    def load_poeme_by_eleve(self, eleve):
        req = ""
        return poemes
        
        
    