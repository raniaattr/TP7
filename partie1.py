import sqlite3

# PARTIE 1 :

def main():
    try:
        # connexion a la BDD (création si elle n'existe pas)
        connexion = sqlite3.connect("alesc.db")
        curseur = connexion.cursor()

        # script de creation de la table logement
        requete_type = f'''CREATE TABLE IF NOT EXISTS `type` (
                      `id_type` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                      'nom' TEXT NOT NULL)'''

        requete_logeur = f'''CREATE TABLE IF NOT EXISTS `logeur` (
              `id_logeur` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
              'nom' TEXT NOT NULL,
              `prenom` TEXT NOT NULL,
              `numero_rue` TEXT  NOT NULL,
              `nom_rue` TEXT  NOT NULL,
              `code_postal` TEXT  NOT NULL,
              `ville` TEXT  NOT NULL)'''

        requete_logement = f'''CREATE TABLE IF NOT EXISTS `logement` (
                      `id_logement` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                      `numero_rue` TEXT  NOT NULL,
                      `nom_rue` TEXT  NOT NULL,
                      `code_postal` TEXT  NOT NULL,
                      `ville` TEXT  NOT NULL,
                      `label` INTEGER  NOT NULL,
                      `id_logeur` INTEGER NOT NULL,
                      'id_type' INTEGER NOT NULL,
                      CONSTRAINT `fk_logement_logeur`
                        FOREIGN KEY (`id_logeur`)  
                        REFERENCES `logeur` (`id_logeur`)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION,
                      CONSTRAINT 'fk_logement_type'
                        FOREIGN KEY ('id_type')
                        REFERENCES 'type' ('id_type')
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION)'''

        requete_etudiant = f'''CREATE TABLE IF NOT EXISTS `etudiant` (
              `id_etudiant` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
              `nom` TEXT  NOT NULL,
              `prenom` INTEGER  NOT NULL,
              `semestre` TEXT  NOT NULL,
              `id_logement` INTEGER NOT NULL,
              CONSTRAINT `fk_etudiant_logement`
                FOREIGN KEY (`id_logement`)  
                REFERENCES `logement` (`id_logement`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION)'''

        curseur.execute(requete_type)
        curseur.execute(requete_logeur)
        curseur.execute(requete_logement)  # execution de la requete
        curseur.execute(requete_etudiant)

        # CREATION DES AUTRES TABLES A FAIRE

        connexion.commit()

    except FileNotFoundError:
        print("fichier inexistant")
    finally:
        if connexion:
            curseur.close()
            connexion.close()


if __name__ == '__main__':
    main()
