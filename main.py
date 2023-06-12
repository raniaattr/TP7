import sqlite3

def main():
    try:
        # connexion a la BDD (création si elle n'existe pas)
        connexion = sqlite3.connect("alesc.sqlite")
        curseur = connexion.cursor()

        # script de creation de la table logement
        requete_logements = f'''CREATE TABLE IF NOT EXISTS `logements` (
              `id_logement` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
              `numero_rue` TEXT  NOT NULL,
              `label` INTEGER  NULL,
              `nom_rue` TEXT  NOT NULL,
              `code_postal` TEXT  NOT NULL,
              `ville` TEXT  NOT NULL,
              `type` TEXT  NOT NULL,
              `id_logeur` INTEGER NOT NULL, 
              CONSTRAINT `fk_logements_logeurs`
                FOREIGN KEY (`id_logeur`)  
                REFERENCES `logeurs` (`id_logeur`)
                ON DELETE NO ACTION
                ON UPDATE NO ACTION)'''

        curseur.execute(requete_logements)  # execution de la requete


        # script de creation de la table logement
        requete_logeurs = f'''CREATE TABLE IF NOT EXISTS `logeurs` (
                     `id_logeur` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                     `nom` TEXT  NOT NULL,
                     `prenom` TEXT  NOT NULL,
                     `numero_rue` TEXT  NULL,
                     `nom_rue` TEXT  NULL,
                     `code_postal` TEXT  NULL,
                     `ville` TEXT  NULL)'''

        curseur.execute(requete_logeurs)  # execution de la requete

        # script de creation de la table logement
        requete_etudiants = f'''CREATE TABLE IF NOT EXISTS `etudiants` (
                      `id_etudiant` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                      `nom` TEXT  NOT NULL,
                      `prenom` TEXT  NOT NULL,
                      `semestre` INTEGER  NULL,
                      `numero_rue` TEXT  NULL,
                      `nom_rue` TEXT  NULL,
                      `code_postal` TEXT  NULL,
                      `ville` TEXT  NULL,
                      `id_logement` INTEGER NULL,
                      CONSTRAINT `fk_etudiants_logements`
                        FOREIGN KEY (`id_logements`)  
                        REFERENCES `logements` (`id_logement`)
                        ON DELETE NO ACTION
                        ON UPDATE NO ACTION)'''


        curseur.execute(requete_logeurs)  # execution de la requete

        connexion.commit()

    except FileNotFoundError:
        print("fichier inexistant")
    finally:
        if connexion:
            curseur.close()
            connexion.close()



if __name__ == '__main__':
    main()

