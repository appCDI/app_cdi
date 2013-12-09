'''
Created on 18 nov. 2013

@author: niho
'''

import sqlite3

basededonnee = "lecteuraudio.db"
conn = sqlite3.connect(basededonnee)
cur = conn.cursor()

class Bdd_poeme():
    '''
    classdocs
    '''

    def del_poeme(self,poeme):
        id_poeme = poeme.id
        req = "DELETE FROM POEME WHERE idPoeme = ".id_poeme
        cur.execute(req)
        
        
    def save_poeme(self,poeme):
        req = ""
        
    def load_all_poeme(self):
        req = "SELECT * FROM POEME"
        cur.execute(req)
        return list(cur)
    
    def load_poeme_by_theme(self, theme):
        id_theme = theme.id_theme
        req = "SELECT DISTINCT * FROM POEME WHERE idTheme = ",id_theme
        cur.execute(req)
        
        return list(cur)
    
    def load_one_poeme(self, poeme):
        id_poeme = poeme.id_poeme
        req = "SELECT * FROM POEME WHERE idPoeme = ".id_theme
        resultat = cur.execute(req)
        return resultat
    
    def load_poeme_by_auteur(self, auteur):
        id_artiste = auteur.id_auteur
        req = "SELECT * FROM poeme WHERE idArtiste = ".id_artiste
        cur.execute(req)
        
        return list(cur)
    
    def load_poeme_by_eleve(self, eleve):
        id_Eleve = eleve.id
        req = "SELECT * FROM poeme WHERE idEleve = ".id_Eleve
        cur.execute(req)        
        
        return list(cur)
        
        
    