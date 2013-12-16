'''
Created on 18 nov. 2013

@author: niho
'''

import sqlite3
from Media import Auteur
from Media import Poeme
from Media import eleve
from Media import Forme
from Media import Langue
from Media import Siecle
from Media import Theme

basededonnee = "lecteuraudio.db"
conn = sqlite3.connect(basededonnee)
cur = conn.cursor()

class Bdd_poeme():
    '''
    classdocs
    '''

    def del_poeme(self,poeme):
        id = poeme.id_poeme
        req = "DELETE FROM POEME WHERE idPoeme = ?"
        cur.execute(req, id)
        
        
    def save_poeme(self,poeme, theme):
        id = poeme.id_poeme
        titre = poeme.nom_poeme
        auteur = poeme.id_auteur
        forme = poeme.id_forme
        theme = theme.id_theme
        eleve = poeme.id_eleve
        langue = poeme.id_langue
        siecle = poeme.id_siecle
        chemin = poeme.path
        
        objPoeme = Poeme(id, titre, chemin, eleve, forme, langue, siecle, auteur)
        
        if (exist_poeme_eleve(objPoeme) == True):
            str_msg = 'Ce poeme existe déjà.'
        else:
            req = "INSERT INTO poeme VALUES(?,?,?,?,?,?,?,?)"
            cur.execute(req, id, titre, auteur, forme, eleve, siecle, langue, chemin)
            str_msg = "L'ajout s'est effectué correctement."
        
        return str_msg
                   
    def load_all_poeme(self):
        req = "SELECT * FROM POEME"
        cur.execute(req)
        return list(cur)
    
    def load_poeme_by_theme(self, theme):
        id = theme.id_theme
        req = "SELECT DISTINCT * FROM POEME WHERE idTheme = ? "
        cur.execute(req, id)
        
        return list(cur)
    
    def load_one_poeme(self, poeme):
        id = poeme.id_poeme
        req = "SELECT * FROM POEME WHERE idPoeme = ?"
        resultat = cur.execute(req, id)
        return resultat
    
    def load_poeme_by_auteur(self, auteur):
        id = auteur.id_auteur
        req = "SELECT * FROM poeme WHERE idArtiste = ?"
        cur.execute(req, id)
        
        return list(cur)
    
    def load_poeme_by_eleve(self, eleve):
        id = eleve.id_eleve
        req = "SELECT * FROM poeme WHERE idEleve = "
        cur.execute(req, id)        
        
        return list(cur)
        
    def exist_poeme(self, poeme):
        idPoeme = poeme.id_poeme
        req = "SELECT * FROM poeme WHERE idPoeme = ?"
        resultat = cur.execute(req, idPoeme)
        if (resultat == ''):
            return False
        else:
            return True
    
    
    def exist_poeme_eleve(self, poeme):
        artiste = poeme.artiste
        titre = poeme.titre
        eleve = poeme.eleve
        req = "SELECT * FROM poeme INNER JOIN artiste ON poeme.idArtiste = artiste.id INNER JOIN eleve ON poeme.idEleve = eleve.id WHERE artiste.nom = ? AND poeme.titrePoeme = ? AND eleve.nom = ?" 
                
        cur.execute(req, artiste, titre, eleve)
        list(cur)
        if (len(list) == 0):
            return False
        else:
            return True
        
    
    def exist_artiste(self, artiste):
        idArtiste = artiste.id_artiste
        req = "SELECT * FROM artiste WHERE id = ?"
        resultat = cur.execute(req, idArtiste)
        if (resultat == ''):
            return False
        else:
            return True
        
    def exist_forme(self, forme):
        idForme = forme.id_forme
        req = "SELECT * FROM forme WHERE id = ?"
        resultat = cur.execute(req, idForme)
        if (resultat == ''):
            return False
        else:
            return True
    
    def exist_theme(self, theme):
        idTheme = theme.id_theme
        req = "SELECT * FROM theme WHERE id = ?"
        resultat = cur.execute(req, idTheme)
        if (resultat == ''):
            return False
        else:
            return True
    
    def exist_eleve(self, eleve):
        idEleve = eleve.id_poeme
        req = "SELECT * FROM eleve WHERE id = ?"
        resultat = cur.execute(req, idEleve)
        if (resultat == ''):
            return False
        else:
            return True
      
    def load_poeme_by_Id(self, idPoeme):
        req= "SELECT * FROM poeme WHERE idPoeme=?"
        cur.execute(req, idPoeme)
        list(cur)
        artistePoeme = list['idArtiste']
        titrePoeme = list['titrePoeme']
        sieclePoeme = list['idSiecle']
        formePoeme = list['idForme']
        languePoeme = list['idLangue']
        cheminPoeme = list['idChemin']
        elevePoeme = list['idEleve']
        
        objetPoeme = Poeme(idPoeme, titrePoeme, cheminPoeme, elevePoeme, formePoeme, languePoeme, sieclePoeme, artistePoeme)
        return objetPoeme
        
    def load_auteur_by_Id(self, idAuteur):
        req = "SELECT * FROM artiste WHERE id=?"
        cur.execute(req, idAuteur)
        list(cur)
        nomAuteur = list[1]
        prenomAuteur = list[2]       
        objetAuteur = Auteur(idAuteur, nomAuteur, prenomAuteur)
        return objetAuteur
    
    def load_forme_by_Id(self, idForme):
        req = "SELECT * FROM forme WHERE id=?"
        cur.execute(req, idForme)
        list(cur)
        libForme = list[1]
        objetForme = Forme(idForme, libForme)
        return objetForme
    
    def load_theme_by_Id(self, idTheme):
        req = "SELECT * FROM theme WHERE id=?"
        cur.execute(req, idTheme)
        list(cur)
        libTheme = list[1]
        objetTheme = Theme(idTheme, libTheme)
        return objetTheme
    
    def load_eleve_by_Id(self, idEleve):
        req = "SELECT * FROM eleve WHERE id=?"
        cur.execute(req, idEleve)
        list(cur)
        nomEleve = list[1]
        prenomEleve = list[2]
        objetEleve = eleve(idEleve, nomEleve, prenomEleve)
        return objetEleve
        
    def load_langue_by_Id (self, idLangue):
        req = "SELECT * FROM langue WHERE id=?"
        cur.execute(req, idLangue)
        list(cur)
        libLangue = list[1]
        objetLangue = Langue(idLangue, libLangue)
        return objetLangue
    
    def load_siecle_by_Id (self, idSiecle):
        req = "SELECT * FROM siecle WHERE id=?"
        cur.execute(req, idSiecle)
        list(cur)
        libSiecle = list[1]
        objetSiecle = Siecle(idSiecle, libSiecle)
        return objetSiecle
    
    
    
    