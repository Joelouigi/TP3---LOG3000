# Backend
### But
Ce module se charge de la logique d'opérations du programme. Pour ce cas-ci, c'est ce dernier qui s'occupe de faire les opérations arithmétiques et qui reçoit les requêtes GET et POST.

### Arborescence
```
.
├── backend/
│   ├── README.md
│   ├── app.py # Lance le programme, s'occupe de recevoir les requêtes GET et POST, et implémente l'algorithme d'analyse syntaxique de l'opération mathématique donnée par l'utilisateur
│   └── operators.py # Ensembles de fonctions pour les opérations arithmétiques de base
```
### Dépendances ou Hypothèses
Le programme a besoin d'une connection internet fonctionnelle ainsi que la librairie flask installée avec l'utilitaire pip de python
