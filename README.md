# Career Progression & Promotion Gap Analysis for Retention Optimization

## 📌 Project Overview

This project focuses on using **HR Analytics and Machine Learning** to analyze employee career progression, identify promotion gaps, detect career stagnation, and uncover potential retention opportunities.

Traditional employee attrition models primarily focus on predicting **who may leave the organization**. This project takes a different approach by focusing on **why employees may eventually become disengaged** by analyzing structural career-related factors such as prolonged promotion gaps, role stagnation, limited training opportunities, and managerial continuity.

The project was developed in the context of **Palo Alto Networks** and aims to demonstrate how career intelligence can support proactive and data-driven employee retention strategies.

---

## 🎯 Problem Statement

Organizations often rely on employee attrition models to identify employees who may leave. However, prediction alone does not explain the underlying career conditions that may contribute to disengagement.

This project addresses the following questions:

* Which employees are experiencing prolonged promotion gaps?
* Which employees have remained in the same role for an extended period?
* Are employees receiving sufficient training and development opportunities?
* How does managerial continuity relate to career growth?
* Can employees be grouped into meaningful career trajectory patterns?
* Which employees represent potential retention opportunities?

The goal is to move from **reactive attrition management** toward **proactive career-focused retention**.

---

## 🎯 Project Objectives

The main objectives of the project are:

1. Analyze employee career progression patterns.
2. Identify employees experiencing promotion stagnation.
3. Measure role stagnation and career growth.
4. Analyze training and development intensity.
5. Examine managerial continuity.
6. Identify distinct career trajectory groups using clustering.
7. Develop a Promotion Gap Risk Score.
8. Develop a Retention Opportunity Index.
9. Identify employees who may benefit from proactive interventions.
10. Build an interactive Streamlit dashboard for HR decision-making.

---

# 📊 Dataset

The dataset contains employee-level HR information covering demographics, employment, compensation, satisfaction, performance, training, and career progression.

### Major Features

| Category        | Features                                                                            |
| --------------- | ----------------------------------------------------------------------------------- |
| Demographics    | Age, Gender, MaritalStatus, Education, EducationField                               |
| Employment      | Department, JobRole, JobLevel                                                       |
| Compensation    | DailyRate, HourlyRate, MonthlyIncome, MonthlyRate                                   |
| Career          | YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager   |
| Experience      | TotalWorkingYears, NumCompaniesWorked                                               |
| Training        | TrainingTimesLastYear                                                               |
| Performance     | PerformanceRating, PercentSalaryHike                                                |
| Satisfaction    | JobSatisfaction, EnvironmentSatisfaction, RelationshipSatisfaction, WorkLifeBalance |
| Work Conditions | BusinessTravel, OverTime                                                            |
| Target          | Attrition                                                                           |

---

# ⚙️ Methodology

The project follows a complete data analytics and machine learning workflow.

```text
Raw HR Dataset
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Feature Scaling
      ↓
Career Path Clustering
      ↓
Cluster Interpretation
      ↓
Promotion Gap Risk Scoring
      ↓
Retention Opportunity Index
      ↓
Streamlit Dashboard
      ↓
HR Insights & Recommendations
```

---

# 🧹 1. Data Preprocessing

The dataset was prepared before performing analysis and clustering.

The preprocessing workflow included:

* Missing-value analysis
* Duplicate detection
* Data type validation
* Numerical feature analysis
* Categorical feature analysis
* Outlier detection using IQR
* Numerical feature scaling
* Preparation of categorical variables for analysis

Extreme values were carefully examined because some long-tenure employees may represent legitimate career patterns rather than data errors.

---

# 🔧 2. Feature Engineering

Several career-focused features were created to transform raw HR attributes into meaningful career intelligence indicators.

### Promotion Gap Ratio

Measures the proportion of company tenure that has elapsed since the employee's last promotion.

```text
Promotion Gap Ratio =
YearsSinceLastPromotion / YearsAtCompany
```

A higher value indicates a relatively larger promotion gap.

---

### Role Stagnation Index

Measures the proportion of company tenure spent in the employee's current role.

```text
Role Stagnation Index =
YearsInCurrentRole / YearsAtCompany
```

A high value may indicate limited role mobility.

---

### Training Intensity Score

Measures training participation relative to company tenure.

```text
Training Intensity Score =
TrainingTimesLastYear / YearsAtCompany
```

This helps identify employees who may have limited recent development exposure.

---

### Manager Stability Indicator

Measures the proportion of company tenure spent with the current manager.

```text
Manager Stability Indicator =
YearsWithCurrManager / YearsAtCompany
```

This provides an indication of managerial continuity.

---

### Career Growth Score

A composite score was developed using career level, salary growth, performance, training, and promotion delay.

```python
CareerGrowthScore = (
    JobLevel * 2
    + PercentSalaryHike / 10
    + PerformanceRating
    + TrainingTimesLastYear
    - YearsSinceLastPromotion
)
```

This score provides a simplified measure of overall career progression.

---

# 📈 3. Exploratory Data Analysis

EDA was performed to understand employee career and workforce patterns.

The analysis includes:

* Attrition distribution
* Department-wise employee distribution
* Job role distribution
* Age distribution
* Years at company
* Years in current role
* Years since last promotion
* Career stage distribution
* Training participation
* Career growth
* Promotion gaps
* Managerial continuity
* Department-level career patterns
* Role-level stagnation
* Career progression versus attrition

Visualizations were created using **Matplotlib, Seaborn, and Plotly**.

---

# 🤖 4. Career Path Clustering

Employee career trajectories were analyzed using **unsupervised machine learning**.

### Primary Algorithm

**K-Means Clustering**

K-Means was selected to identify groups of employees with similar career progression characteristics.

The clustering features include:

* YearsAtCompany
* YearsInCurrentRole
* YearsSinceLastPromotion
* YearsWithCurrManager
* Promotion Gap Ratio
* Role Stagnation Index
* Training Intensity Score
* Manager Stability Indicator
* Career Growth Score
* TrainingTimesLastYear
* JobLevel

Before clustering, numerical features were standardized using `StandardScaler`.

---

# 📊 5. Cluster Evaluation

The number of clusters was evaluated using:

### Elbow Method

The Elbow Method was used to analyze Within-Cluster Sum of Squares (WCSS) across different values of K.

### Silhouette Score

Silhouette analysis was used to evaluate cluster separation and cohesion.

Hierarchical clustering was also used as a validation technique to compare the structure identified by K-Means.

---

# 🧩 6. Career Cluster Interpretation

After clustering, each group was analyzed based on its career characteristics.

Potential career profiles include:

### 🚀 Fast-Track Performers

Employees showing strong career progression, higher job levels, and relatively shorter promotion gaps.

### 📌 Stable Contributors

Employees demonstrating relatively stable career trajectories with moderate progression.

### 🌱 Early-Career Explorers

Employees with shorter organizational tenure who are still developing their career paths.

### ⚠️ Promotion-Stalled Employees

Employees experiencing relatively long promotion gaps and high role stagnation.

### 🔴 High-Risk Stagnation Profiles

Employees showing multiple career stagnation indicators such as long promotion gaps, limited training, and weak career progression.

> Cluster labels are based on the actual characteristics observed in the final clustering results.

---

# 🚦 7. Promotion Gap Risk Scoring

A Promotion Gap Score was developed to identify employees experiencing potential career stagnation.

The score combines:

* Promotion Gap Ratio
* Role Stagnation Index
* Training Intensity
* Manager Stability

The resulting employees are classified into different risk categories:

| Risk Level  | Interpretation                      |
| ----------- | ----------------------------------- |
| 🟢 Low      | Healthy career progression          |
| 🟡 Medium   | Some signs of stagnation            |
| 🟠 High     | Significant promotion gap           |
| 🔴 Critical | Severe career stagnation indicators |

This score is intended as a **career intervention indicator**, not as a prediction that an employee will leave.

---

# 🎯 8. Retention Opportunity Index

The Retention Opportunity Index identifies employees who may benefit from proactive career interventions.

The index considers factors such as:

* Promotion stagnation
* Role stagnation
* Training needs
* Managerial continuity
* Career progression

Employees with higher scores receive higher intervention priority.

Possible intervention categories include:

* Promotion review
* Career development planning
* Training and certification
* Internal role rotation
* Mentorship
* Cross-functional projects
* Career counseling

---

# 👨‍💼 9. Managerial Insights

The project also analyzes managerial continuity and its relationship with employee career growth.

The analysis includes:

* Manager tenure
* Manager stability
* Promotion gaps
* Career growth
* Role stagnation
* Team-level career patterns

This allows HR stakeholders to identify teams where career progression may require additional attention.

---

# 🖥️ 10. Streamlit Dashboard

An interactive Streamlit application was developed to present the analytical results.

## 🏠 Home Dashboard

Provides an overall workforce overview including:

* Total employees
* Average promotion gap
* Average career growth
* Critical employees
* Attrition distribution
* Promotion risk distribution
* Department-level career growth
* Department-level promotion gaps

---

## 📊 Career Clustering Dashboard

Provides:

* Career cluster distribution
* Cluster-level career growth
* Promotion gap by cluster
* Training participation by cluster
* Attrition by cluster
* Career cluster summary
* Interactive cluster explorer
* Employee-level cluster records

---

## 📈 Promotion Gap Monitor

Provides:

* Promotion Gap Risk distribution
* High-gap employee identification
* Department-level promotion gap analysis
* Role-level stagnation analysis
* Promotion threshold filtering

---

## 🎯 Retention Opportunity Panel

Provides:

* Retention Opportunity Index
* High-priority employee identification
* Training need indicators
* Suggested intervention actions
* Filtered employee records
* CSV download functionality

---

## 👨‍💼 Manager Insights

Provides:

* Manager tenure analysis
* Career growth versus manager stability
* Promotion gap analysis
* Team-level stagnation signals
* Managerial continuity insights

---

# 🔍 Dashboard Filters

Users can interactively filter the analysis using:

* Department
* Job Role
* Career Stage
* Promotion Gap Risk
* Career Cluster
* Retention Priority

This allows HR users to investigate specific employee groups instead of analyzing the entire workforce at once.

---

# 🛠️ Tech Stack

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn
* Plotly

### Machine Learning

* Scikit-learn

### Dashboard

* Streamlit

### Development Environment

* Jupyter Notebook

---

# 📁 Project Structure

```text
Career-Progression-Promotion-Gap-Analysis/
│
├── notebooks/
│   ├── 01_Preprocessing.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_Career_Path_Clustering.ipynb
│   └── 04_Promotion_Gap_Risk_Scoring.ipynb
│
├── data/
│   ├── IBM_HR_Cleaned_IQR.csv
│   ├── Processed_Data.csv
│   ├── Processed_Data_Scaled.csv
│   ├── Clustered_Career_Data.csv
│   └── Final_Career_Intelligence_Output.csv
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

# 📌 Key Performance Indicators

The dashboard focuses on the following KPIs:

| KPI                         | Purpose                                        |
| --------------------------- | ---------------------------------------------- |
| Career Cluster              | Identifies employee career trajectory          |
| Promotion Gap Score         | Measures potential career stagnation           |
| Retention Opportunity Index | Prioritizes potential interventions            |
| Training Need Indicator     | Identifies development requirements            |
| Manager Stability Indicator | Measures managerial continuity                 |
| Career Growth Score         | Provides an overall career progression measure |

---

# 💡 Business Value

The project provides a shift from traditional reactive retention strategies toward proactive career intelligence.

Instead of only asking:

> **"Who is likely to leave?"**

the project asks:

> **"Where are employees experiencing career stagnation, and what can the organization do about it?"**

This enables HR teams to potentially:

* Identify promotion bottlenecks.
* Detect role stagnation.
* Improve employee development.
* Target training opportunities.
* Support internal mobility.
* Identify teams requiring career-growth attention.
* Prioritize retention interventions.
* Make workforce decisions using data.

---

# 📌 Key Insights

The project is designed to uncover patterns such as:

* Employees experiencing prolonged promotion gaps.
* Roles with higher levels of stagnation.
* Career clusters with different progression patterns.
* Employees with limited development opportunities.
* Relationships between managerial continuity and career growth.
* Employee groups that may benefit from proactive retention strategies.

Actual numerical findings should be added to this section after completing the final analysis.

---

# ⚠️ Limitations

The project has several limitations:

1. The dataset represents employee information at a specific point in time.
2. Career trajectories cannot be fully captured without longitudinal employee records.
3. Promotion and retention scores depend on analytical assumptions and selected weights.
4. Clustering results require business interpretation.
5. The framework should not be treated as a direct predictor of employee resignation.
6. Analytical scores should support, rather than replace, HR judgment.

---

# 🚀 Future Enhancements

Future versions of the project could include:

* Longitudinal employee career tracking.
* Automated attrition prediction.
* Explainable AI using SHAP.
* Personalized career recommendation systems.
* Training recommendation engines.
* Internal mobility recommendation.
* Real-time HR database integration.
* Automated HR alerts.
* Advanced employee segmentation.
* Role-specific career path recommendations.

---

# 📊 Project Outcome

The final outcome is an integrated **Career Intelligence System** that combines data analytics, machine learning, scoring frameworks, and interactive visualization.

```text
Employee Data
      ↓
Career Feature Engineering
      ↓
EDA
      ↓
Career Clustering
      ↓
Promotion Gap Analysis
      ↓
Retention Opportunity Identification
      ↓
Interactive Streamlit Dashboard
      ↓
Actionable HR Insights
```

The project demonstrates how data science can be applied not only to predict employee attrition but also to understand **career progression structures that may create retention opportunities**.



