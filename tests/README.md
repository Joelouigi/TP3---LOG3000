# Tests
### But
Ce module se charge de tester les diverses fonctions des fichiers dans le sous dossier [backend](../backend)
Les tests couvrent les opérations de bases arithmétiques d'[operators](../backend/operators.py) ainsi que l'intégration avec des exemples d'entrées utilisateur dans la fonction calculate(expr) d'[app](../backend/app.py)

### Arborescence
```
.
├── tests/
│   ├── README.md
│   └── test_calculator.py # Contient les tests pour la logique de l'application
```
### Dépendances ou Hypothèses
Dépend de la librairie pytest ainsi que des fonctions de logiques ([app](../backend/app.py) et [operators](../backend/operators.py)) de l'application pour comparer les résultats attendus à ceux obtenus 

### Lancement des tests
```
# À la racine du projet
python -m pytest
```
