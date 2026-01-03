\# Student Grade Analyzer



\## 📌 Overview

A simple Student Grade Analyzer data analysis project built with \*\*Python and Pandas\*\*.  

It analyzes student exam scores, assigns grades, ranks students based on performance, and generates meaningful insights from the data.



The project uses a \*\*Jupyter Notebook\*\* for exploration and analysis, and a \*\*Python script\*\* for reusable data processing.



---



\## 📊 Dataset

The dataset contains exam results for \*\*1000 students\*\*, including:



\- Gender  

\- Race/Ethnicity  

\- Parental level of education  

\- Lunch type  

\- Test preparation course  

\- Math score  

\- Reading score  

\- Writing score  



The dataset is commonly used for educational performance analysis.



---



\## ⚙️ Features

\- Calculates total and average scores per student  

\- Assigns grades (A–F) based on average score  

\- Ranks students by performance  

\- Generates a processed results CSV file  

\- Analyzes performance patterns based on:

&nbsp; - Gender

&nbsp; - Lunch type

&nbsp; - Test preparation course  

\- Provides meaningful insights using grouped statistics



---



\## 📁 Project Structure



student-grade-analyzer/

├── StudentsPerformance.csv # Raw dataset

├── analyzerr.py # Core analysis logic

├── student\_score\_data\_analyzer.ipynb # Exploration \& insights

├── finalized\_results.csv # Generated results

└── README.md # Project documentation





---



\## 🚀 How to Run the Project



\### 1️⃣ Install dependencies

```bash

pip install pandas



\### 2️⃣ Run the analysis script

python analyzerr.py





This will generate a finalized\_results.csv file containing:



Total score

Average score

Grade

Rank



You can run the script either from the VS Code terminal or a regular command-line interface.



📒 Notebook Analysis

The Jupyter Notebook (student\_score\_data\_analyzer.ipynb) includes:

Data inspection

Performance comparisons by group

Grade distribution analysis

Written interpretations of results



The notebook is intended for exploration and insight generation, while the Python script is used for automation and reuse.



🧠 Key Insights

Students who completed the test preparation course generally performed better across all subjects.

Students with standard lunch plans achieved higher average scores than those on free/reduced lunch.

Reading and writing scores were, on average, higher than math scores.

Most students fall within the A and B grade categories.



🛠️ Tools Used



Python

Pandas

Jupyter Notebook

VS Code



📌 Notes

This project focuses on data analysis and interpretation, not predictive modeling or visualization.

Visualizations can be added later as an extension.



✅ Status

✔ Completed

✔ Open for future improvements (visuals, CLI, ML extensions)



