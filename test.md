# 11. Tester et valider

Avant de considérer l’application comme terminée, vous devez la tester.

## Tests à réaliser

### Affichage
- [x] La page principale fonctionne
- [x] Les données sont correctement affichées
- [x] La page détail fonctionne

### Filtre
- [x] Le filtre donne un résultat
- [x] Le filtre donne plusieurs résultats
- [x] Le filtre peut donner zéro résultat
- [x] Le message « aucun résultat » fonctionne

### Navigation
- [x] Les liens fonctionnent
- [x] L’accès au détail fonctionne
- [x] Le retour vers la liste fonctionne

### Interface
- [x] Les informations sont lisibles
- [x] Les statuts sont correctement présentés
- [x] La mise en page est cohérente

---

# 12. Fiche de tests et recette

## Fiche de tests (`tests/fiche_tests.md`)

| N° Test | Test | Résultat attendu | Résultat obtenu | Statut |
| :---: | :--- | :--- | :--- | :---: |
| **T01** | Ouvrir / | Liste affichée | Liste affichée | **OK** |
| **T02** | Ouvrir un détail | Détail affiché | Détail affiché | **OK** |
| **T03** | Filtrer | Résultats filtrés | Résultats filtrés | **OK** |
| **T04** | Aucun résultat | Message affiché | Message affiché | **OK** |
| **T05** | Retour liste | Liste affichée | Liste affichée | **OK** |

---

## Recette

Vérifiez ensuite que le produit final correspond au cahier des charges.

- [x] **Liste** : Oui / ~~Non~~
- [x] **Détail** : Oui / ~~Non~~
- [x] **Filtre** : Oui / ~~Non~~
- [x] **Cas sans résultat** : Oui / ~~Non~~
- [x] **Navigation** : Oui / ~~Non~~
- [x] **CSS** : Oui / ~~Non~~

> *Note : Une fonctionnalité non conforme doit être corrigée lorsque cela est possible.*