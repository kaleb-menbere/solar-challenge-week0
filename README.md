# 🌞 Solar Challenge Week 0

## 🧩 Overview
This repository is part of the **10Academy Solar Challenge** — Week 0 focuses on **Git, environment setup, and basic CI/CD**.  
The goal is to establish a clean, reproducible development environment and workflow that ensures collaboration and consistency across systems.

---

## ⚙️ Environment Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/kaleb-menbere/solar-challenge-week0.git
cd solar-challenge-week0
```

---

### 2️⃣ Create and Activate a Virtual Environment

#### 🪟 On Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### 🐧 On Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

If `requirements.txt` changes later, simply rerun this command to stay updated.

---

### 4️⃣ Verify the Setup
Check Python and library versions:
```bash
python --version
pip list
```

Expected core packages:
- pandas  
- numpy  
- matplotlib  

---

### 5️⃣ Run CI Check (Optional)
GitHub Actions automatically verifies environment setup on each push or pull request.

You can test it locally by running:
```bash
python --version
pip install -r requirements.txt
```

---

## 🧠 Project Structure
```
solar-challenge-week0/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── __init__.py
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
├── scripts/
│   ├── __init__.py
│   └── README.md
├── .gitignore
├── requirements.txt
├── README.md
└── venv/ (excluded via .gitignore)
```

---

## 🌿 Git Workflow

1️⃣ **Create a new branch for each task**
```bash
git checkout -b your-branch-name
```

2️⃣ **Stage and commit changes**
```bash
git add .
git commit -m "feat: describe your change here"
```

3️⃣ **Push the branch**
```bash
git push origin your-branch-name
```

4️⃣ **Open a Pull Request**  
Go to GitHub → Compare & Pull Request → Merge into `main`.

---

## 🧩 .gitignore
The project ignores:
```
venv/
data/
*.csv
.ipynb_checkpoints/
__pycache__/
```

---

## ✅ Continuous Integration (CI)
- **Workflow file:** `.github/workflows/ci.yml`
- Runs automatically on every push or pull request.
- Installs dependencies and confirms that the environment builds successfully.

---

## 📘 How to Contribute
1. Fork the repository  
2. Create a feature branch  
3. Commit your changes  
4. Push and submit a Pull Request  

---

## 🧑‍💻 Author
**Kaleb Menbere**  
📧 [GitHub Profile](https://github.com/kaleb-menbere)  
🌍 10Academy — Solar Challenge Week 0
