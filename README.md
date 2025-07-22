# Password Control App

Une application Flask simple pour gérer l'inscription, l'authentification, le changement de mot de passe avec vérification de complexité, et une interface administrateur.

## 🔧 Fonctionnalités

- Inscription et connexion sécurisée
- Changement de mot de passe avec vérification :
  - Au moins 8 caractères
  - 1 majuscule, 1 minuscule
  - 1 chiffre
  - 1 caractère spécial
- Empêche la réutilisation de l'ancien mot de passe
- Interface Admin (accessible aux comptes `is_admin=True`)
- Conteneurisé avec Docker et Docker Compose

## 🚀 Lancement rapide

### 1. Cloner et décompresser

```bash
unzip password_control_app_with_admin.zip
cd password_control_app
```

### 2. Lancer avec Docker Compose

```bash
docker-compose up --build
```

Accédez à [http://localhost:5000](http://localhost:5000)

## 👤 Accès administrateur

Par défaut, aucun compte n'est administrateur.

Pour activer l'interface admin :

```python
# Dans un shell Python du conteneur (docker exec -it <container> python)
from app import db
from app.models import User

user = User.query.filter_by(username='votre_nom').first()
user.is_admin = True
db.session.commit()
```

## 📂 Structure

```
password_control_app/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   └── templates/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── run.py
└── README.md
```

## ✅ À venir (suggestions)

- Supprimer des comptes via l’admin
- Historique des anciens mots de passe
- Envoi de mail à chaque modification
