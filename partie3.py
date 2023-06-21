import sqlite3

# PARTIE 3 :

connexion = sqlite3.connect("alesc.db")  # reconnexion à la base de donnée
curseur = connexion.cursor()
curseur2 = connexion.cursor()
nom_logeur = str(input("Nom du logeur : "))
prenom_logeur = str(input("Prénom du logeur : "))

requete1 = f'SELECT log.id_logement,log.nom_rue,log.numero_rue,log.ville,log.code_postal,log.id_type FROM logement AS log JOIN logeur AS l ON (l.id_logeur=log.id_logeur) WHERE nom = ? AND prenom = ?;'

curseur.execute(requete1, [nom_logeur, prenom_logeur])
les_logements = curseur.fetchall()

# on fait une deuxième requête pour compléter l'affichage

requete2 = f'SELECT nom FROM type WHERE id_type=?'

# premier affichage:

print("\nPremier affichage : ")
print(f'Nom du logeur: {nom_logeur} {prenom_logeur} ')
for i, tuple_l in enumerate(les_logements):
    type = tuple_l[5]
    curseur.execute(requete2, [type])
    logement_type = curseur.fetchall()
    print(f'Logement {i+1} : {tuple_l[2]} rue {tuple_l[1]} {tuple_l[4]} {tuple_l[3]} *** {logement_type[0][0]} ')

    # affichage des étudiants logés:

requete_complete = f'SELECT log.id_logement,log.nom_rue,log.numero_rue,log.ville,log.code_postal,log.id_type, etu.nom,etu.prenom FROM logement as log JOIN logeur as l ON (l.id_logeur=log.id_logeur) LEFT JOIN Etudiant as etu ON (etu.id_logement=log.id_logement) WHERE l.nom = ? AND l.prenom = ? ;'

curseur2.execute(requete_complete, [nom_logeur, prenom_logeur])
etudiant_loge = curseur2.fetchall()
print("\nDeuxième affichage : ")
for i, tuple_l in enumerate(les_logements):
    type = tuple_l[5]
    curseur.execute(requete2, [type])
    logement_type = curseur.fetchall()
    print(f'Logement {i+1} : ')
    print(f'{tuple_l[2]} rue {tuple_l[1]} {tuple_l[4]} {tuple_l[3]} * {logement_type[0][0]} ')
    for el in etudiant_loge:
        if el[0] == tuple_l[0]:
            if el[6] != None:
                print(f"Nom de l'étudiant : {el[6]} {el[7]}")

curseur.close()  # fermeture de la connexion
curseur2.close()

connexion.close()