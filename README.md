## Calculatrice

- Équipe 35

Ce projet présente une plateforme pour une calculatrice. Cette dernière permet d'effectuer des calculs de plusieurs nombres avec comme opérations arithmétiques de bases : l'addition, la multiplication, la division et la soustraction.

### Prérequis
- python (###mettre la version###)
- pip
- flask

### Installation
1. Cloner le repo
```
git clone https://github.com/Joelouigi/TP3---LOG3000.git
```
2. Installer la version stable la plus récente de python: `https://www.python.org/downloads/`
3. Créer l'environnement virtuel
```
python -m venv .venv
```
4. Activer l'environnement virtuel

**Macos/linux**
```
source .venv/bin/activate
```
**Windows**
```
# Cmd
.venv\Scripts\activate

# Powershell
.\.venv\Scripts\Activate.ps1
```

### Utilisation
**Installation des dépendances**
```
pip install flask pytest
```
**Lancer l'application**
```
# Sous le répertoire /backend
python app.py
```
Vous pouvez ensuite entrer cette adresse dans votre moteur de recherche pour accéder à l'application http://127.0.0.1:5000

### Tests
**Lancer les tests**
```
# Sous le répertoire /tests
python -m pytest
```

### Contribution

**Syntaxe Commits**
```
feat(module): description de la modification apportée # Pour une nouvelle fonctionalité
fix(module): description de la modification apportée # Pour une résolution de bug
hotfix(module): description de la modification apportée # Pour une résolution urgente de bug
style(module): description de la modification apportée # Pour une modification qui touche purement à l'aspect visuel de l'application
chore(module): description de la modification apportée # Pour une modification qui ne touche ni aux fonctionalités, ni au style de l'application, ni aux corrections de bugs 
test(module): description de la modification apportée # Pour un ou plusieurs nouveaux tests
```

**Syntaxe PR**
```
feature/objectif # Pour une nouvelle fonctionalité
fix/objectif # Pour une résolution de bug
style/objectif # Pour une modification qui touche purement à l'aspect visuel de l'application
chore/objectif # Pour une modification qui ne touche ni aux fonctionalités, ni au style de l'application, ni aux corrections de bugs 
test/objectif # Pour un ou plusieurs nouveaux tests
```

**Syntaxe Issues**

Titre : Titre de la problématique  
Description : Explication de la problématique (fichier et fonction où se trouve le bug)
Photos (pour un bug visuel seulement)