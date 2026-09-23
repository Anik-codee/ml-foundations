# Machine Learning Foundations (ML-Foundations)

## Purpose of the Repository
This repository documents my foundational journey into Python programming, version control, and data engineering practices as part of my machine learning preparation roadmap. It houses clean, well-tested scripts and notebooks designed to build robust core competencies.

## Week 1 Topics Covered
* **Environment & Version Control:** Setting up VS Code, virtual environments (`.venv`), `.gitignore`, and Git/GitHub workflows.
* **Python Basics:** Variables, arithmetic, and custom functions (`basics.py`).
* **Conditionals & Logic:** Boolean logic, comparison operators, and decision-making structures (`conditions.py`).
* **Collections:** Lists, loops, list comprehensions, and dictionaries (`lists_loops_and_dictionaries.py`).
* **Data Processing & NumPy:** Parsing CSV files using Python's native modules and performing exploratory numerical computing with NumPy arrays (`csv_numpy.ipynb`).
* **Mini Projects:** Building a modular Machine Sensor Summary Tool(`sensor_summary.py`).

## Folder Structure
ml-foundations/
│
├── .venv/                  # Isolated Python virtual environment (ignored by Git)
├── week1/                  # Week 1 learning modules and projects
│   ├── basics.py      # Python variables and functions
│   ├── conditions.py  # Conditional logic exercises
│   ├── lists_loops_and_dictionaries.py # Lists, loops, and dictionaries
│   ├── csv_numpy.ipynb    # NumPy exploratory notebook
│   ├── sensor_data.csv     # Sample machine sensor dataset
│   └── sensor_summary.py   # Machine sensor summary mini project
├── .gitignore              # Specifies intentionally untracked files to ignore
├── requirements.txt        # Project package dependencies
└── README.md               # Repository overview documentation

## Environment Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/Anik-codee/ml-foundations.git](https://github.com/Anik-codee/ml-foundations.git)
   cd ml-foundations
   ```
2. Activate your virtual environment:
* **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
* **Windows (Command Prompt):** `.venv\Scripts\activate.bat`

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run the Sensor Summary Tool
To execute the modular machine sensor summary program from the repository root, run:
   ```bash
python week1/sensor_summary.py
```    
## Sample Output
```text   
MACHINE SENSOR SUMMARY
Machines analyzed: 5
Average temperature: 76.8 C
Highest temperature: 95 C
Lowest temperature: 65 C
Average rotational speed: 1416 RPM
Average torque: 47.4 Nm

Warning and critical machines:
- Motor-B: 82 C
- Motor-D: 95 C
Highest-risk machine: Motor-D
```

## What I Learned
Through Week 1, I learned setting up isolated Python development environments, writing modular code using functions rather than long blocks of scripts, handling flat-file data parsing with Python's built-in `csv` library, leveraging NumPy for fast vector calculations, and tracking progress professionally using Git version control.