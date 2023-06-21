import sqlite3
import pandas as pd

# PARTIE 2 :

connexion = sqlite3.connect("alesc.db")  # reconnexion à la base de donnée
curseur = connexion.cursor()

# remplissage de la table type
logement = pd.read_excel('logements.xlsx')
type = logement['type_logement']
requete_type = f'INSERT INTO type(nom) values (?)'
for ligne in type:
    requete_verif = f'SELECT nom FROM type'
    curseur.execute(requete_verif)
    res_verif = curseur.fetchall()
    if ligne not in res_verif:
        curseur.execute(requete_type, [ligne])
        result = curseur.fetchall()

# remplissage table logeur

logeur = pd.read_excel('logeurs.xlsx')
requete_logeur = f'INSERT INTO logeur(nom,prenom,numero_rue,nom_rue,code_postal,ville) values (?, ?, ?, ?, ?, ?)'
for ligne in logeur.iterrows():
    (nom_logeur, prenom_logeur) = (ligne[1][0], ligne[1][1])
    requete_verif = f'SELECT nom,prenom FROM logeur'
    curseur.execute(requete_verif)
    res_verif = curseur.fetchall()
    if (nom_logeur, prenom_logeur) not in res_verif:
        curseur.execute(requete_logeur, [ligne[1][0], ligne[1][1], ligne[1][2], ligne[1][3], ligne[1][4], ligne[1][5]])

# remplissage table logement

logement = pd.read_excel('logements.xlsx')
requete_logement = f'INSERT INTO logement (numero_rue,nom_rue,code_postal,ville,label,id_logeur,id_type) values (?, ?, ?, ?, ?, ?,?)'
for ligne in logement.iterrows():
    (numero_rue, nom_rue, label, nom_logeur, prenom_logeur, type) = (
    ligne[1][0], ligne[1][1], ligne[1][4], ligne[1][5], ligne[1][6], ligne[1][7])
    requete1_verif = f'SELECT numero_rue,nom_rue,label FROM logement '
    curseur.execute(requete1_verif)
    res_verif1 = curseur.fetchall()

    if (numero_rue, nom_rue, label) not in res_verif1:
        req_log = f'SELECT id_logeur FROM logeur AS l WHERE l.nom= ? AND l.prenom= ? '
        curseur.execute(req_log, [nom_logeur, prenom_logeur])
        log = curseur.fetchall()
        log_id = log[0][0]
        req_type = f'SELECT id_type FROM type AS t WHERE t.nom= ?'
        curseur.execute(req_type, [type])
        typ = curseur.fetchall()
        type_id = typ[0][0]
        curseur.execute(requete_logement, [numero_rue, nom_rue, ligne[1][2], ligne[1][3], label, log_id, type_id])

# remplissage table etudiant

etu = pd.read_excel('etudiants.xlsx')
requete_etudiant = f'INSERT INTO etudiant (nom,prenom,semestre,id_logement) values (?, ?, ?, ?)'
for ligne in etu.iterrows():
    (nom, prenom, semestre, numero_rue, nom_rue, code_postal, ville) = (
    ligne[1][0], ligne[1][1], ligne[1][2], ligne[1][3], ligne[1][4], ligne[1][5], ligne[1][6])
    requete1_verif = f'SELECT nom,prenom,semestre FROM Etudiant '
    curseur.execute(requete1_verif)
    res_verif1 = curseur.fetchall()
    if (nom, prenom, semestre) not in res_verif1:
        req_logem = f'SELECT id_logement FROM Logement AS log WHERE log.numero_rue= ? AND log.nom_rue= ? AND log.code_postal= ? AND log.ville= ? '
        curseur.execute(req_logem, [numero_rue, nom_rue, code_postal, ville])
        logem = curseur.fetchall()
        id_logement = logem[0][0]
        curseur.execute(requete_etudiant, [nom, prenom, semestre, id_logement])


curseur.close()
connexion.commit()
connexion.close()