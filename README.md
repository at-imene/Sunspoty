# ☀️ Sunspoty — Détection et Classification Automatique des Taches Solaires par Deep Learning

> Projet de fin d'études Master — Traitement d'images & Deep Learning  
> Application web Django pour l'analyse automatique des taches solaires à partir d'images magnétogrammes

---

## 📌 Résumé

Ce projet vise à assister les astronomes dans la **détection et la classification automatique des taches solaires** à partir d'images magnétogrammes. L'analyse des taches solaires est d'une grande importance en astronomie : elle permet de mieux comprendre le comportement et l'évolution du Soleil, d'identifier des relations avec d'autres phénomènes solaires, et de prédire les éruptions solaires.

Le système repose sur deux grandes parties :

1. **Calcul du nombre de Wolf** — via des méthodes de traitement d'images et de clustering
2. **Classification des taches solaires** — via un réseau de neurones convolutif 2D (CNN) entraîné sur des images magnétogrammes (classes α, β, β-γ, β-δ, etc.)

Une **interface graphique web** (Django) a été développée pour permettre aux astronomes d'utiliser ce système de diagnostic automatique.

---

## 🗂️ Structure du Projet

```
Sunspoty/
│
├── manage.py                  # Point d'entrée Django
├── requirements.txt           # Dépendances Python
├── db.sqlite3                 # Base de données SQLite
├── Pipfile.lock
│
├── project/                   # Configuration principale Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── webApp/                    # Application web principale
│   ├── views.py               # Logique métier & appels modèle
│   ├── urls.py
│   ├── models.py
│   ├── templates/             # Templates HTML
│   └── static/                # CSS, JS, images statiques
│
├── models/                    # Modèles entraînés (.h5 / .keras)
│   └── cnn_sunspot_model.*
│
└── media/                     # Images uploadées par les utilisateurs
```

---

## ⚙️ Fonctionnalités

### Partie 1 — Calcul du Nombre de Wolf
- Prétraitement des images solaires (niveaux de gris, filtrage, seuillage)
- Détection des taches par méthodes de traitement d'images (contours, morphologie)
- Clustering pour regrouper les taches en groupes
- Calcul automatique du **nombre de Wolf** : `W = k(10g + f)` où `g` = nombre de groupes, `f` = nombre total de taches

### Partie 2 — Classification des Taches Solaires (Deep Learning)
- Dataset d'images magnétogrammes divisé en train / validation / test
- Prétraitement : conversion en niveaux de gris + redimensionnement
- **Architecture CNN 2D** entraîné sur les classes de taches solaires :
  - α (Alpha)
  - β (Beta)
  - β-γ (Beta-Gamma)
  - β-δ (Beta-Delta)
  - et autres classes de la classification de Mount Wilson
- **Précision obtenue : 99.8%** sur le jeu de test
- Intégration du modèle entraîné dans l'API Django

---

## 🖥️ Application Web (Django)

L'interface web permet aux astronomes de :
- Uploader une image magnétogramme d'une tache solaire
- Obtenir automatiquement la **classification de la tache** (α, β, β-γ…)
- Visualiser le **nombre de Wolf** calculé
- Consulter l'historique des analyses

---

## 🚀 Installation & Lancement

### Prérequis
- Python 3.8+
- pip

### 1. Cloner le dépôt
```bash
git clone https://github.com/at-imene/Sunspoty.git
cd Sunspoty
```

### 2. Créer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Appliquer les migrations
```bash
python manage.py migrate
```

### 5. Lancer le serveur de développement
```bash
python manage.py runserver
```

Accéder à l'application : [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧠 Modèle CNN

| Paramètre | Valeur |
|---|---|
| Architecture | CNN 2D |
| Entrée | Images magnétogrammes (niveaux de gris) |
| Tâche | Classification multi-classes |
| Précision (test) | **99.8%** |
| Framework | TensorFlow / Keras |

Le modèle entraîné est stocké dans le dossier `models/` et chargé automatiquement par l'API Django lors des prédictions.

---

## 📊 Dataset

- **Type d'images** : Magnétogrammes de taches solaires (source : SOHO/MDI, SDO/HMI ou similaire)
- **Prétraitement** :
  - Conversion en niveaux de gris
  - Redimensionnement uniforme
  - Normalisation des pixels
- **Split** : Entraînement / Validation / Test

---

## 🛠️ Technologies Utilisées

| Catégorie | Outils |
|---|---|
| Backend | Django, Django REST Framework |
| Deep Learning | TensorFlow, Keras |
| Traitement d'images | OpenCV, NumPy, Pillow |
| Clustering | Scikit-learn |
| Frontend | HTML5, CSS3, JavaScript |
| Base de données | SQLite |

---

## 📷 Aperçu

> *(Ajouter des captures d'écran de l'interface web ici)*

---

## 👩‍💻 Auteure

**Imene At**  
Master en Informatique — Spécialité Informatique visuelle
🔗 [GitHub](https://github.com/at-imene)<br><br>
**BOUACHAT Anfel sara** <br>
Master en Informatique — Spécialité Informatique visuelle
🔗 [GitHub](https://github.com/SararaHcn)

---

## 📄 Licence

Ce projet est développé dans le cadre d'un mémoire de Master. Tous droits réservés.

---

## 📚 Références

- Classification de Mount Wilson des taches solaires
- SOHO/MDI & SDO/HMI — NASA Solar Datasets
- LeCun et al. — Convolutional Neural Networks
- Hale, G.E. — Solar magnetic field observations
