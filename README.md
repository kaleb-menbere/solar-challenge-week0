# 🌞 Solar Challenge Week 0

## 🧩 Overview
This repository is part of the **10Academy Solar Challenge** — Week 0 focuses on **Git, environment setup, and basic CI/CD**.  
The goal is to establish a clean, reproducible development environment and workflow that ensures collaboration and consistency across systems.

---

## 🧱 Prerequisites

Before starting, make sure you have the following installed on your computer:

| Tool | Version | Purpose | Check Command |
|------|----------|----------|----------------|
| **Python** | 3.8 or higher | Runs the code and creates a virtual environment | `python --version` or `python3 --version` |
| **pip** | Latest | Installs required Python packages | `pip --version` |
| **Git** | Latest | For cloning and version control | `git --version` |
| *(Optional)* **Conda** | Latest | Alternative to venv (optional) | `conda --version` |

💡 **Tip:**  
- On **Windows**, download Python from [python.org/downloads](https://www.python.org/downloads/) and check “✅ Add Python to PATH” during installation.  
- On **macOS/Linux**, Python is often preinstalled. If not, install it via:
  ```bash
  sudo apt install python3 python3-pip -y   # Ubuntu/Debian
  brew install python                       # macOS
  ```

---

## ⚙️ Environment Setup

All commands below should be **copied and pasted directly into your CMD (Windows)** or **Terminal (Mac/Linux)**.

---

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/kaleb-menbere/solar-challenge-week0.git
cd solar-challenge-week0
```

---

### 2️⃣ Create and Activate a Virtual Environment

#### 🪟 On Windows (CMD)
```bash
python -m venv venv
venv\Scripts\activate
```

#### 🐧 On Linux / macOS (Terminal)
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

If `requirements.txt` is updated later, just re-run the same command.

---

### 4️⃣ Verify the Setup
Confirm your environment is working correctly:
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
GitHub Actions automatically verifies environment setup on every push or pull request.

You can test this locally by running:
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
git checkout -b setup-task   # (you can use your own branch name)
```

2️⃣ **Stage and commit changes**
```bash
git add .
git commit -m "feat: update requirements (added pandas)"
```

3️⃣ **Push the branch**
```bash
git push origin setup-task   # (replace with your branch name)
```

4️⃣ **Open a Pull Request**  
Go to **GitHub → Compare & Pull Request → Merge into `main`**.

---

## 🧩 .gitignore
Files and folders excluded from version control:
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
- Installs dependencies and verifies the environment builds correctly.

---

## 📘 How to Contribute
1. Fork the repository  
2. Create a new branch for your feature or fix  
3. Commit your changes with a clear message  
4. Push and open a Pull Request  

---

## 🧑‍💻 Author
**Kaleb Menbere**  
📧 [GitHub Profile](https://github.com/kaleb-menbere)  
🌍 10Academy — Solar Challenge Week 0
