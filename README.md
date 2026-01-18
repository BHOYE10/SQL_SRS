# SQL Learning App - Système de Répétition Espacée

Application interactive pour apprendre et pratiquer SQL avec validation automatique et répétition espacée pour mémorisation long-terme.

## 🚀 Installation

```bash
# Cloner le projet
git clone https://github.com/BHOYE10/SQL_SRS.git
cd SQL_SRS

# Créer environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Installer dépendances
pip install -r requirements.txt

# Initialiser base de données
python init_db.py

# Lancer l'application
streamlit run app.py
```

## 📁 Structure

```
SQL_SRS/
├── app.py              # Application principale
├── init_db.py          # Initialisation base de données
├── requirements.txt    # Dépendances Python
├── answers/            # Résultats SQL attendus
└── data/               # Données générées
```

## 🛠️ Technologies

- **Python** - pandas, streamlit
- **SQLite** - Base de données
- **Git/GitHub** - Versioning

## 💡 Fonctionnalités

- Pratique interactive de requêtes SQL
- Validation automatique des résultats
- Système de répétition espacée (SRS)
- Suivi des progrès

## 👤 Auteur

**Mamadou Bhoye Cisse**
- GitHub: [@BHOYE10](https://github.com/BHOYE10)
- LinkedIn: [Mamadou-Bhoye-Cisse](https://linkedin.com/in/Mamadou-Bhoye-Cisse)
