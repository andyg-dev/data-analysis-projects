# Tech Startup Analytics Project

## Project Overview

This project simulates a real-world data analytics workflow for a charter bus platform. It was designed to showcase skills in **SQL**, **Python**, **Tableau**, and basic **automation** by answering data-driven business questions with measurable impact on revenue, operations, and customer retention.

---

## Business Questions

### 1. Are certain bus operators responsible for higher cancellation rates?

> **Why it matters:** High cancellation rates can hurt customer trust and revenue. Identifying underperforming operators would allow management to take corrective actions or renegotiate contracts.

- **Method:** SQL joins and aggregation across operators and booking status  
- **Analysis:** Chi-square statistical test using Python (`scipy.stats`)  
- **Result:** *No statistically significant difference found in cancellation rates across operators (p = 0.34)*  
- **Impact:** Shifted focus from operator quality to customer behavior and route-level insights

---

### 2. Can we segment customers based on their booking patterns to drive targeted marketing?

> **Why it matters:** Understanding customer behavior enables personalized promotions, loyalty programs, and premium offerings — all of which increase retention and lifetime value.

- **Method:** SQL aggregation to engineer customer features (total spend, trip distance, booking frequency)  
- **Analysis:** K-Means clustering in Python (`scikit-learn`)  
- **Segments Identified:**
  - **Budget Travelers:** Low spend, short distances → target with seasonal discounts
  - **Frequent Long-Distance Riders:** High trip count → reward with loyalty perks
  - **High Spenders:** Premium customers → offer VIP packages

- **Visualization:** Tableau Online scatterplot (Total Spent vs. Avg Distance), color-coded by segment

---

## 🛠️ Tools & Technologies

| Tool      | Purpose                              |
|-----------|---------------------------------------|
| **SQLite**| Database design and SQL queries       |
| **Python**| Data generation, ETL, stats, clustering|
| `pandas`  | Data manipulation and exports         |
| `scipy`   | Chi-square test                       |
| `sklearn` | K-Means clustering                    |
| **Tableau**| Dashboard creation and storytelling  |
| **Automation** | Python scripts for repeatable data pulls and exports |

---

## 🤖 Automation

- Python scripts generate realistic synthetic data and load it into SQLite
- Automated SQL queries extract business metrics and export them to `.csv`

---

## 📈 Deliverables

- `complete_analytics_project.db` — SQLite database
- `pull_data.py` — Script to extract data and export CSVs
- Tableau Dashboards:
  - **Dashboard 1:** Operator-wise Booking Status with Chi-Square Result
  - **Dashboard 2:** Customer Segments (Spending vs. Distance)

---

📬 *Interested in seeing this project live or want the code? Just ask!*
