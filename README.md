# SQL Learning App - Spaced Repetition System

Interactive application for learning and practicing SQL with automated validation and spaced repetition for long-term retention.

🚀 **[Try it live!](#)** (Coming soon)

## What is SRS?

**Spaced Repetition System (SRS)** is a scientifically proven learning technique that optimizes long-term retention by scheduling reviews at increasing intervals (2, 7, 21 days). This method is based on the Ebbinghaus forgetting curve and is more effective than traditional studying methods.

## Features

- 📝 **Interactive SQL Practice** - Write and test queries in real-time
- ✅ **Automated Validation** - Compare results against expected outputs
- 🔄 **Spaced Repetition** - Review queries at optimal intervals (2/7/21 days)
- 📊 **Progress Tracking** - Monitor your learning journey


## Installation

```bash
# Clone the project
git clone https://github.com/BHOYE10/SQL_SRS.git
cd SQL_SRS

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Initialize database
python init_db.py

# Launch application
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Project Structure

```
SQL_SRS/
├── app.py              # Main Streamlit application
├── init_db.py          # Database initialization script
├── requirements.txt    # Python dependencies
├── answers/            # Expected SQL query results
├── data/               # Generated data and databases
└── README.md           # This file
```

## Technologies

- **Python** - Core programming language
- **Streamlit** - Web application framework
- **SQLite** - Database management
- **pandas** - Data manipulation and validation
- **Git/GitHub** - Version control

## How It Works

1. **Select a SQL theme** from the dropdown menu
2. **View the tables** and their structure
3. **Write your SQL query** in the text area
4. **Submit** and see if your result matches the expected output
5. **Schedule review** based on your performance (2, 7, or 21 days)

## Author

**Mamadou Bhoye Cisse**
- GitHub: [@BHOYE10](https://github.com/BHOYE10)
- LinkedIn: [Mamadou-Bhoye-Cisse](https://linkedin.com/in/Mamadou-Bhoye-Cisse)
- Email: bhoyecisse460@gmail.com

---

⭐ If you find this project helpful, consider giving it a star on GitHub!
