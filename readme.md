# 🛍️ Customer Behavior Analysis and Business Decision Making

## 📌 Project Overview

This project analyzes customer behavior using the **Mall Customers Dataset** to uncover purchasing patterns, spending habits, and business insights. Through statistical analysis, data visualization, and hypothesis testing, the project helps businesses understand customer segments and make data-driven decisions.

The analysis focuses on customer demographics such as age, gender, annual income, and spending score to identify trends that influence consumer behavior.

---

## 🎯 Objectives

* Understand customer demographics and spending patterns.
* Perform exploratory data analysis (EDA).
* Detect outliers and analyze data distributions.
* Compare spending behavior across genders.
* Measure relationships between customer attributes.
* Apply statistical testing for business decision-making.
* Generate actionable business insights.

---

## 📂 Dataset

**Dataset:** Mall Customers Dataset

### Features:

| Column                 | Description                       |
| ---------------------- | --------------------------------- |
| CustomerID             | Unique customer identifier        |
| Gender                 | Male/Female                       |
| Age                    | Customer age                      |
| Annual Income (k$)     | Annual income in thousand dollars |
| Spending Score (1-100) | Customer spending behavior score  |

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy

---

## 📊 Project Workflow

### 1. Data Understanding

* Dataset loading
* Shape and structure analysis
* Data type inspection
* Missing value detection

### 2. Descriptive Analysis

* Mean
* Median
* Mode

For:

* Age
* Annual Income
* Spending Score

### 3. Data Visualization

* Histograms
* Distribution Plots
* Boxplots
* Scatter Plots

### 4. Outlier Detection

Used the **Interquartile Range (IQR)** method to identify outliers in:

* Age
* Annual Income
* Spending Score

### 5. Group-Based Analysis

Compared:

* Average annual income by gender
* Average spending score by gender

### 6. Correlation Analysis

Analyzed relationships between:

* Age vs Spending Score
* Annual Income vs Spending Score

### 7. Inferential Statistics

Performed an Independent **T-Test** to determine whether spending behavior differs significantly between male and female customers.

#### Hypotheses

* **H₀:** No significant difference exists in spending scores between genders.
* **H₁:** A significant difference exists in spending scores between genders.

### 8. Confidence Interval Analysis

Calculated a 95% confidence interval for the average spending score.

### 9. Business Insights

Generated business-focused insights based on:

* Customer income levels
* Spending patterns
* Gender-based behavior
* Correlation findings

---

## 📈 Key Insights

* Customer spending behavior can vary independently of income levels.
* Correlation analysis helps identify factors affecting spending habits.
* Statistical testing provides evidence-based conclusions for marketing decisions.
* Customer segmentation can improve targeting strategies and customer engagement.

---

## 🚀 How to Run the Project

### Clone Repository

```bash
git clone https://github.com/your-username/customer-behavior-analysis.git
```

### Navigate to Project Folder

```bash
cd customer-behavior-analysis
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scipy
```

### Run Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
projectUnlox-2.ipynb
```

---

## 📁 Project Structure

```text
├── projectUnlox-2.ipynb
├── Mall_Customers.csv
├── README.md
```

---

## 🔮 Future Improvements

* Customer Segmentation using K-Means Clustering
* Predictive Modeling for Spending Score
* Interactive Dashboard with Streamlit or Power BI
* Advanced Customer Lifetime Value Analysis

---

## 👨‍💻 Author

**Sandhya Shakya**

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 📜 License

This project is open-source and available under the MIT License.
