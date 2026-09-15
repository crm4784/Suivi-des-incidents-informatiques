# Mini-projet Flask — Gestion de Tickets Helpdesk

## Présentation
Cette application web développée avec **Flask** et **pyhton** permet de centraliser, visualiser et gérer la liste des tickets d'incidents informatiques (Helpdesk). Elle offre une vue d'ensemble du parc d'incidents et facilite le suivi de leur résolution pour les équipes support.

---

## Fonctionnalités
- **Compteur et statistiques :** Calcul dynamique du nombre total de tickets, répartition par statut et taux de résolution global.
- **Tri automatique par gravité :** Affichage prioritaire des tickets du plus grave au moins grave (`Critique` ➔ `Majeure` ➔ `Mineure`).
- **Filtrage multicritères :** Possibilité de filtrer la liste en direct selon la **Gravité**, le **Traitement** et l'**Origine**.
- **Vue détaillée :** Page dédiée pour chaque ticket affichant toutes ses caractéristiques (symptôme, demandeur, origine, etc.).

---

## Installation
Assurez-vous d'avoir Python installé sur votre machine, puis installez les dépendances :


pip install -r requirements.txt
**Github** installation du depot github avec les isues et les tache a venir en cour a faire terminer par clement, 
Ainsi que un gant effectuer par alban  et un gant sur github par alban 

## Lancement Pour démarrer l'application en mode développement :
**python app.py**
## utilisation des commande git 
- git init 
- git status 
-etc 
## creation branch 
- git switch main
- git pull origin main
- git switch -c feature-filtres-incidents


**Incident de fusion et retard de rendu : L'intégralité du développement ayant été réalisée sur la branche feature-page-liste, une tentative de synchronisation avec la branche main accompagnée d'un crash système a provoqué des conflits Git majeurs ainsi que des erreurs de commandes. Apres plusieur tentaive j'ai finalement reussi pour corriger l'historique et résoudre les conflits de fusion a nécessité des manipulations complexes, ce qui explique le décalage d'une heure sur le rendu final du projet.**

## Fusion des branches

**J'ai travaillé sur la branche feature-filtres-incidents afin d'ajouter les filtres et les modifications de mon projet Flask. J'ai ensuite enregistré mes modifications avec un commit et envoyé la branche sur GitHub avec git push. J'ai ensuite basculé sur la branche main et lancé une fusion avec git merge feature-filtres-incidents. Un conflit est apparu dans le fichier static/style.css, que j'ai résolu en conservant la version de ma branche feature-filtres-incidents. La fusion a ensuite été validée avec un commit**

Accédez ensuite à l'application dans votre navigateur à l'adresse : http://127.0.0.1:5000/

##  organisation du projet 
```bash
.
├── app.py              # Application principale Flask (routes, logique de tri et filtrage)
├── data/
│   └── data.json       # Base de données au format JSON
├── templates/
│   ├── base.html       # Template de base (header, navigation, footer)
│   ├── index.html      # Page d'accueil (stats, filtres et liste des tickets)
│   └── detail.html     # Page de détail d'un ticket
├── static/
│   └── style.css       # Feuillets de style CSS
└── README.md           # Documentation du projet$

``` 

# Membres
Alban : Développeur Back-end (logique Flask, manipulation des données JSON, tri ).
 - afficher un compteur du nombre total d’incidents par statut (ex : "En cours : 2", "Résolu : 1") en haut de la page liste ;
 - appliquer un code couleur aux incidents en fonction de leur gravite:
"Critique" → rouge foncé
"Haute" → orange
"Moyenne" → jaune
"Faible" → vert
Affichez cette couleur dans la liste et dans la page de détail.
- mettre visuellement en évidence les incidents prioritaires.

Clément : Développeur Front-end et et filtres (création des templates Jinja, mise en page CSS et intégration des formulaires). 
- creation du depot git hub, projet, issues, commande git pour envoyer vers le depot. 
- afficher les incidents ; 
- afficher le détail d'un incide identifier clairement la priorité ;
- identifier clairement la priorité ;

## Commun
 - css realise par alban en fonction des tache de chacun donc css mis en commun ( un plus travailler par alban pour le commun )
 - issues 
- pull Requests : Validation croisée du code avant fusion sur la branche principale (feature-filtres-incidents), garantissant un code stable.

Gestion du projet
Issues : Création et suivi des tickets de tâches (ex: Création des routes, Mise en place du CSS, Implémentation des filtres).

GitHub Project & Kanban : Organisation du travail sous forme de colonnes (To Do, In Progress, Done) pour suivre l'avancement en temps réel.

Planning : fais sur le gaant



## Bilan

Difficultés rencontrées
Probleme avec la fusion des branch qui on créer plusieur conflit au sein du projet

Solutions trouvées
La solution consiste à fusionner la branche feature-filtres-incidents dans main et à résoudre le conflit et le push sur la branch main et feature-filtres-incidents

Écarts entre prévision et réalisation
Prévu : Simple liste statique avec page de détail.

Réalisé : Ajout de la fonctionnalité de filtrage multicritères dynamique et tri automatique par gravité.

Améliorations possibles
Ajouter un système d'authentification pour les techniciens.

Permettre la création, la modification et la suppression de tickets directement depuis l'interface (CRUD complet)..