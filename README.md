\# 🍬 Nassau Candy Distributor Analytics



\## Product Line Profitability \& Margin Performance Analysis



\*\*An End-to-End Business Analytics Project Using Python, Pandas, Plotly and Streamlit\*\*



\---



\## 📌 Table of Contents



1\. \[Project Overview](#-project-overview)

2\. \[Business Problem](#-business-problem)

3\. \[Project Objectives](#-project-objectives)

4\. \[Dataset Description](#-dataset-description)

5\. \[Tools and Technologies](#-tools-and-technologies)

6\. \[Project Workflow](#-project-workflow)

7\. \[Data Cleaning and Quality Checks](#-data-cleaning-and-quality-checks)

8\. \[Key Performance Indicators](#-key-performance-indicators)

9\. \[Exploratory Data Analysis](#-exploratory-data-analysis)

10\. \[Profitability Analysis](#-profitability-analysis)

11\. \[Product Performance Segmentation](#-product-performance-segmentation)

12\. \[Pareto Analysis](#-pareto-analysis)

13\. \[Margin Risk Screening](#-margin-risk-screening)

14\. \[Monthly Performance Analysis](#-monthly-performance-analysis)

15\. \[What-If Profit Simulator](#-what-if-profit-simulator)

16\. \[Interactive Dashboard Features](#-interactive-dashboard-features)

17\. \[Key Business Findings](#-key-business-findings)

18\. \[Business Recommendations](#-business-recommendations)

19\. \[Project Structure](#-project-structure)

20\. \[Installation and Setup](#-installation-and-setup)

21\. \[How to Use the Dashboard](#-how-to-use-the-dashboard)

22\. \[Business Metrics and Formulas](#-business-metrics-and-formulas)

23\. \[Assumptions and Limitations](#-assumptions-and-limitations)

24\. \[Future Enhancements](#-future-enhancements)

25\. \[Skills Demonstrated](#-skills-demonstrated)

26\. \[Author](#-author)



\---



\## 📖 Project Overview



The \*\*Nassau Candy Distributor Analytics\*\* project is an end-to-end business analytics solution developed to understand product-level profitability, gross margin performance, cost structure and sales trends.



The project uses Python for data analysis and a Streamlit application to present interactive business insights through KPI cards, charts, tables, filters, downloadable reports and a hypothetical profit simulator.



The main objective is to transform raw transactional data into meaningful information that can support business analysis and data-driven decision-making.



The project focuses on understanding which products contribute most to gross profit, which products have comparatively low margins, how profitability varies across divisions, and how hypothetical changes in selling prices and costs could affect financial performance.



\### Project Highlights



\* Transaction-level data analysis using Pandas.

\* Data cleaning and validation.

\* Product-level profitability and gross margin calculations.

\* Division-wise financial performance analysis.

\* Monthly revenue and profit trend visualization.

\* Product performance classification.

\* Pareto analysis of gross profit contribution.

\* Low-margin product screening.

\* Interactive what-if profit simulation.

\* Downloadable CSV reports.

\* Interactive dashboard developed using Streamlit and Plotly.



\---



\## 🎯 Business Problem



A distributor may generate revenue from several product lines, but revenue alone does not explain which products contribute most effectively to profitability.



A product with high sales may have a comparatively low gross margin because of its cost structure. Another product may have a high margin but contribute little total profit because its sales volume is small.



Without a structured profitability analysis, it can be difficult to identify:



\* Which products contribute the largest share of gross profit.

\* Which divisions drive overall profitability.

\* Which products have margins that deserve further investigation.

\* How gross profit and margin change over time.

\* How hypothetical price and cost adjustments could influence profit.

\* Where additional analysis of pricing, costs and sales performance may be useful.



This project addresses these questions by combining financial calculations, exploratory data analysis, visualizations and an interactive dashboard.



\---



\## 🎯 Project Objectives



The key objectives of this project are:



1\. Analyze total revenue, cost, gross profit and gross margin.

2\. Assess profitability across individual products.

3\. Compare sales and profitability across business divisions.

4\. Calculate each product's contribution to total gross profit.

5\. Identify high-profit products and comparatively low-margin products.

6\. Examine monthly revenue, profit and gross margin trends.

7\. Perform product performance segmentation using sales and margin benchmarks.

8\. Apply Pareto analysis to understand the concentration of gross profit.

9\. Develop a what-if simulator for hypothetical price and cost changes.

10\. Provide interactive filters for date range, division and region.

11\. Generate downloadable transaction and profitability reports.

12\. Present findings through a user-friendly business intelligence dashboard.



\---



\## 📂 Dataset Description



The project uses the \*\*Nassau Candy Distributor\*\* dataset, which contains transaction-level information about orders, customers, products, geographical locations, sales, units, costs and gross profit.



\### Dataset Summary



| Attribute                 | Description                     |

| ------------------------- | ------------------------------- |

| Initial number of records | 10,194                          |

| Number of columns         | 18                              |

| Data format               | CSV                             |

| Main subject              | Product sales and profitability |

| Main analysis level       | Transaction and product         |

| Data processing tool      | Pandas                          |

| Dashboard tool            | Streamlit                       |



The dataset's exact date range and any data-format assumptions should be verified against the source file before publishing the final project documentation.



\### Dataset Columns



| Column           | Description                                       |

| ---------------- | ------------------------------------------------- |

| `Row ID`         | Identifier for a dataset row                      |

| `Order ID`       | Identifier associated with an order               |

| `Order Date`     | Date on which the order was placed                |

| `Ship Date`      | Date on which the order was shipped               |

| `Ship Mode`      | Shipping method associated with the order         |

| `Customer ID`    | Customer identifier                               |

| `Country/Region` | Country or region associated with the transaction |

| `City`           | City associated with the transaction              |

| `State/Province` | State or province associated with the transaction |

| `Postal Code`    | Postal code associated with the transaction       |

| `Division`       | Business division of the product                  |

| `Region`         | Geographic region associated with the transaction |

| `Product ID`     | Product identifier                                |

| `Product Name`   | Name of the product                               |

| `Sales`          | Sales amount recorded for the transaction         |

| `Units`          | Number of units recorded                          |

| `Gross Profit`   | Gross profit recorded for the transaction         |

| `Cost`           | Cost recorded for the transaction                 |



\*\*Note:\*\* The dataset is used for analytical and educational purposes. Its original source and license should be reviewed before redistributing the raw file.



\---



\## 🛠 Tools and Technologies



\### Python



Used as the primary programming language for data processing, calculations and analysis.



\### Pandas



Used for:



\* Loading CSV files.

\* Cleaning and standardizing product names.

\* Parsing date columns.

\* Grouping and aggregating transaction data.

\* Calculating financial metrics.

\* Creating summary tables.

\* Exporting analysis results to CSV.



\### NumPy



Used for numerical operations and data analysis support.



\### Plotly



Used to create interactive charts, including monthly trends, product profitability and division comparisons.



\### Streamlit



Used to develop the interactive web dashboard, filters, KPI cards, downloadable reports and what-if simulator.



\### Matplotlib and Seaborn



Used for generating supporting analytical visualizations during the analysis phase.



\### CSV



Used as the input format and for exporting analytical reports.



\### PowerShell and Visual Studio Code/Notepad



Used to manage the project environment and edit Python files on Windows.



\---



\## 🔄 Project Workflow



The project follows a structured data analytics workflow:



1\. \*\*Data collection:\*\* Load the distributor dataset from a CSV file.

2\. \*\*Data inspection:\*\* Examine dimensions, columns, data types and values.

3\. \*\*Data cleaning:\*\* Parse dates, standardize product names and validate important fields.

4\. \*\*Data quality checks:\*\* Examine duplicates, invalid values and gross profit consistency.

5\. \*\*Exploratory data analysis:\*\* Study sales, costs, units and product distributions.

6\. \*\*Financial calculations:\*\* Calculate gross margins and profit contribution.

7\. \*\*Product analysis:\*\* Rank products and compare profitability.

8\. \*\*Trend analysis:\*\* Aggregate financial metrics by month.

9\. \*\*Risk screening:\*\* Identify products with comparatively low margins.

10\. \*\*Scenario analysis:\*\* Estimate the impact of hypothetical price and cost changes.

11\. \*\*Visualization:\*\* Build charts and supporting tables.

12\. \*\*Dashboard development:\*\* Combine the analysis into an interactive Streamlit application.

13\. \*\*Report generation:\*\* Export filtered data and summary reports.



\---



\## 🧹 Data Cleaning and Quality Checks



Data quality is essential because errors in dates, costs or sales can distort profitability calculations.



The initial quality checks reported the following results:



| Check                       | Initial Result |

| --------------------------- | -------------: |

| Duplicate rows              |              0 |

| Zero or negative sales      |              0 |

| Zero or negative cost       |              0 |

| Zero or negative units      |              0 |

| Gross profit mismatches     |              0 |

| Invalid order dates         |              0 |

| Invalid ship dates          |              0 |

| Ship date before order date |              0 |



\### Data Preparation Steps



\*\*1. Date parsing\*\*



The order date field is converted to a datetime format so that transactions can be grouped by month and filtered by date.



\*\*2. Product name standardization\*\*



Leading and trailing spaces are removed, and inconsistent spacing around hyphens is normalized. This helps prevent the same product from being treated as multiple categories.



\*\*3. Data aggregation\*\*



Transaction-level records are grouped by product or division to calculate total sales, cost, gross profit and units.



\*\*4. Gross profit validation\*\*



Reported gross profit is checked against the difference between sales and cost.



\*\*5. Invalid-value checks\*\*



The analysis examines duplicate records, invalid dates and non-positive financial or unit values.



These checks describe the initial dataset inspection. They should be rerun whenever the underlying data is changed.



\---



\## 📊 Key Performance Indicators



The dashboard displays five major KPIs.



\### 1. Total Revenue



The total sales amount recorded for the selected dataset or filters.



\### 2. Total Cost



The total recorded cost associated with the selected transactions.



\### 3. Total Gross Profit



The difference between total sales and total cost, assuming the supplied gross profit field follows this relationship.



\### 4. Gross Margin



The percentage of revenue retained as gross profit before expenses that are not represented in the dataset's cost field.



\### 5. Units Sold



The total number of units recorded for the selected transactions.



All KPI values respond to the dashboard's date, division and region filters.



\---



\## 🔍 Exploratory Data Analysis



Exploratory data analysis helps identify patterns and differences before making business recommendations.



The project examines:



\* Revenue distribution across products.

\* Cost and gross profit differences.

\* Gross margin variation.

\* Division-wise contribution.

\* Monthly financial trends.

\* Products with high sales and low margins.

\* Products with small sales but high margins.

\* Concentration of gross profit among leading products.



The analysis combines aggregated tables with visualizations to make financial patterns easier to understand.



\---



\## 💰 Profitability Analysis



Product profitability is evaluated using sales, cost, gross profit, gross margin and profit contribution.



\### Product-Level Analysis



Each product is evaluated to understand:



\* How much revenue it generates.

\* How much cost is recorded against it.

\* How much gross profit it contributes.

\* What percentage of its sales becomes gross profit.

\* What percentage of total product gross profit it represents.



\### Division-Level Analysis



Products are grouped into business divisions to compare:



\* Total sales.

\* Total cost.

\* Gross profit.

\* Units sold.

\* Gross margin.

\* Contribution to total gross profit.



This analysis helps distinguish divisions that generate the majority of gross profit from those that may require more detailed investigation.



\---



\## 🧩 Product Performance Segmentation



The project uses product sales and gross margin benchmarks to categorize product performance.



The analysis uses median sales and median product gross margin as reference points.



\### Star Products



Products with sales and gross margin at or above their respective median benchmarks.



These products may be important contributors to the business and can be prioritized for further performance monitoring.



\### High Sales – Low Margin



Products with sales at or above the sales benchmark but gross margin below the margin benchmark.



These products may deserve investigation into pricing, costs and product-level economics.



\### Growth Opportunity



Products with sales below the sales benchmark but gross margin at or above the margin benchmark.



These products may warrant investigation into distribution, demand and potential sales opportunities.



\### Low Sales – Low Margin



Products below both benchmarks.



These products may require closer monitoring to understand their business role and economic performance.



\*\*Important:\*\* These categories are analytical classifications, not automatic decisions to discontinue products or change prices.



\---



\## 📈 Pareto Analysis



Pareto analysis examines how much of the total gross profit is contributed by the highest-ranked products.



Products are sorted in descending order of gross profit, and cumulative profit contribution is calculated.



\### Initial Findings



\* The top four products contributed approximately \*\*77.30%\*\* of total product gross profit.

\* The top five products contributed approximately \*\*95.06%\*\*.

\* Five products were required to exceed 80% cumulative gross profit contribution.



This indicates that gross profit in the initial analysis was concentrated among a small group of products.



The findings can help analysts prioritize product monitoring, although they do not establish that lower-ranked products are unimportant.



\---



\## ⚠️ Margin Risk Screening



The project identifies products whose gross margins are comparatively low.



The initial analysis reported the following examples:



| Product            | Gross Margin |

| ------------------ | -----------: |

| Kazookles          |        7.69% |

| Fun Dip            |       40.00% |

| Nerds              |       46.67% |

| SweeTARTS          |       46.67% |

| Lickable Wallpaper |       50.00% |

| Wonka Gum          |       52.00% |



Kazookles recorded a gross profit of approximately $92.75 on sales of $1,205.75.



Although its margin was low relative to other products, the reported gross profit was still positive.



\### Why This Analysis Matters



A low gross margin can indicate that a product's recorded costs consume a large share of its revenue.



However, gross margin alone does not establish whether a product is commercially unsuccessful. Product volume, strategic importance, operating expenses, customer demand and other business factors may also matter.



The dashboard therefore treats low-margin results as a screening signal for further investigation.



\---



\## 📅 Monthly Performance Analysis



Monthly aggregation is used to understand how revenue, gross profit and gross margin change over time.



The project includes:



\* Monthly revenue trend.

\* Monthly gross profit trend.

\* Monthly gross margin trend.

\* Monthly summary tables.

\* Comparison of financial performance across months.



\### Initial Findings



In the initial monthly analysis:



\* December 2025 recorded the highest monthly revenue, approximately \*\*$12,338.27\*\*.

\* December 2025 also recorded the highest monthly gross profit, approximately \*\*$8,115.95\*\*.

\* Monthly gross margins ranged from approximately 64.54% to 66.75%.



These results describe the initial monthly analysis and should be rechecked against the current date-filtered data before being used in a business report.



\---



\## 🧪 What-If Profit Simulator



The dashboard contains an interactive simulator for exploring hypothetical price and cost adjustments.



Users can select a product and change:



\* Selling price percentage.

\* Cost percentage.



The simulator estimates the resulting sales, cost, gross profit and gross margin.



\### Example Scenario



For the initial analysis of \*\*Wonka Bar - Scrumdiddlyumptious\*\*:



| Metric                            | Initial Value |

| --------------------------------- | ------------: |

| Current gross profit              |    $19,357.50 |

| Hypothetical selling price change |          +10% |

| Hypothetical cost change          |           +5% |

| Estimated gross profit            |    $21,719.12 |

| Estimated gross margin            |        70.83% |

| Estimated profit change           |    +$2,361.62 |



This scenario illustrates how the calculations respond to hypothetical changes.



\### Important Assumptions



\* Units sold remain constant.

\* Sales change in proportion to the selling price adjustment.

\* Costs change in proportion to the cost adjustment.

\* No demand response or price elasticity is modeled.

\* The result is an illustrative scenario, not a forecast of actual business performance.



\---



\## 🖥 Interactive Dashboard Features



The Streamlit dashboard combines the main analyses in one application.



\### 1. Sidebar Filters



Users can filter the analysis by:



\* Division.

\* Region.

\* Start date.

\* End date.



The filtered data drives the displayed KPIs, charts and reports.



\### 2. KPI Cards



Displays total revenue, total cost, gross profit, gross margin and units sold.



\### 3. Monthly Performance Charts



Interactive charts display revenue, gross profit and gross margin trends.



\### 4. Division Profitability



Compares financial performance across divisions using charts and tables.



\### 5. Product Profitability



Displays product rankings, gross profit, gross margin and profit contribution.



\### 6. Downloadable Reports



The dashboard provides CSV downloads for:



\* Filtered transactions.

\* Product profitability.

\* Division profitability.



\### 7. What-If Profit Simulator



Allows users to explore hypothetical product price and cost changes.



\### 8. Business Insights and Recommendations



Highlights the highest gross-profit product, the lowest-margin product, below-median-margin products and potential areas for further investigation.



\---



\## 📌 Key Business Findings



The following figures come from the initial analysis of the supplied dataset.



\### Overall Financial Performance



| Metric               | Initial Result |

| -------------------- | -------------: |

| Total Revenue        |    $141,783.63 |

| Total Cost           |     $48,340.83 |

| Total Gross Profit   |     $93,442.80 |

| Overall Gross Margin |         65.91% |



\### Division Contribution



The Chocolate division contributed approximately \*\*95.06% of total gross profit\*\* in the initial division analysis.



The Other division had a gross margin of approximately \*\*44.84%\*\*, lower than the Chocolate division's margin of approximately 67.45%.



\### Leading Product



Wonka Bar - Scrumdiddlyumptious generated approximately \*\*$19,357.50 in gross profit\*\* in the initial product analysis.



\### Low-Margin Product



Kazookles recorded a gross margin of approximately \*\*7.69%\*\*, making it an important candidate for further cost and pricing investigation.



\### Profit Concentration



The top five products contributed approximately \*\*95.06% of total product gross profit\*\* in the initial Pareto analysis.



These findings provide a starting point for deeper investigation rather than final business decisions.



\---



\## 💡 Business Recommendations



Based on the initial analysis, the following actions may be worth investigating.



\### 1. Monitor Leading Profit Contributors



Track the sales, cost and availability of leading gross-profit products.



The goal is to understand whether their contribution remains stable over time.



\### 2. Investigate Low-Margin Products



Review selling prices, recorded costs and units sold for products with comparatively low gross margins.



Before recommending a price adjustment, investigate demand and competitive conditions.



\### 3. Evaluate Division Performance



Compare division-level revenue, gross margin and profit contribution to understand differences in product mix and recorded costs.



\### 4. Monitor Monthly Trends



Investigate unusual changes in monthly revenue and gross profit. These changes may be associated with order volume, product mix, seasonality or other factors that require additional evidence.



\### 5. Use Scenario Analysis Carefully



Use the simulator to understand how hypothetical assumptions affect profitability calculations.



Validate assumptions with actual sales and cost behavior before using them for planning.



\### 6. Review Low-Sales Products in Context



A low-sales product is not automatically a poor business decision. Consider its margin, strategic importance, customer demand and overall role in the product portfolio.



\---



\## 📁 Project Structure



The project directory contains the following files:



```text

Nassau\_Candy\_Analytics/

│

├── app.py

├── main.py

├── profit\_simulator.py

├── scenario\_comparison.py

├── requirements.txt

├── .gitignore

├── README.md

│

├── Nassau Candy Distributor.csv

│

├── cost\_margin\_risk\_analysis.csv

├── division\_profitability.csv

├── monthly\_profitability.csv

├── pareto\_profit\_analysis.csv

├── product\_performance\_matrix.csv

├── product\_profitability.csv

├── scenario\_comparison.csv

│

├── monthly\_profit\_trend.png

├── monthly\_margin\_trend.png

├── product\_margin\_comparison.png

└── sales\_vs\_cost.png

```



\### Important Files



\* \*\*`app.py`\*\* — interactive Streamlit dashboard.

\* \*\*`main.py`\*\* — initial data analysis script.

\* \*\*`profit\_simulator.py`\*\* — individual product profit simulation.

\* \*\*`scenario\_comparison.py`\*\* — compares predefined pricing and cost scenarios.

\* \*\*`requirements.txt`\*\* — Python package dependencies.

\* \*\*`.gitignore`\*\* — excludes environment folders and sensitive local configuration.

\* \*\*CSV reports\*\* — contain summarized analytical results.

\* \*\*PNG charts\*\* — saved visualizations from the analysis.



The raw dataset should be included in a public repository only if its source and license permit redistribution.



\---



\## ⚙️ Installation and Setup



\### Prerequisites



Ensure Python is installed and available from your terminal.



\### Step 1: Clone the Repository



Replace the placeholder URL with your actual GitHub repository URL.



```bash

git clone YOUR\_REPOSITORY\_URL

cd Nassau\_Candy\_Analytics

```



\### Step 2: Create a Virtual Environment



```bash

python -m venv venv

```



\### Step 3: Activate the Environment



On Windows PowerShell:



```powershell

.\\venv\\Scripts\\Activate.ps1

```



\### Step 4: Install Dependencies



```bash

pip install -r requirements.txt

```



\### Step 5: Place the Dataset



Place `Nassau Candy Distributor.csv` in the project root directory, alongside `app.py`.



Verify that the filename matches the filename used in the code.



\### Step 6: Launch the Dashboard



```bash

streamlit run app.py

```



Streamlit will display a local URL in the terminal. Open that URL in your browser to access the dashboard.



\---



\## 🧭 How to Use the Dashboard



1\. Launch the application using Streamlit.

2\. Select one or more divisions from the sidebar.

3\. Select the required regions.

4\. Choose a start date and end date.

5\. Review the KPI cards to understand the filtered financial performance.

6\. Explore monthly revenue, gross profit and gross margin charts.

7\. Review division-wise profitability.

8\. Examine product rankings and margin contribution.

9\. Download the filtered transactions or summary reports.

10\. Select a product in the What-If Simulator.

11\. Adjust the selling price and cost percentages.

12\. Review the estimated profit change and margin.

13\. Read the business insights and recommendations.



The dashboard recalculates its analysis using the selected filters.



\---



\## 🧮 Business Metrics and Formulas



\### 1. Gross Profit



\*\*Formula:\*\*



Gross Profit = Sales − Cost



This measures the difference between sales and the recorded cost.



\### 2. Gross Margin



\*\*Formula:\*\*



Gross Margin (%) = (Gross Profit / Sales) × 100



This measures gross profit as a percentage of sales.



\### 3. Revenue Contribution



\*\*Formula:\*\*



Revenue Contribution (%) = (Product Sales / Total Sales) × 100



This measures the share of total revenue generated by an individual product.



\### 4. Profit Contribution



\*\*Formula:\*\*



Profit Contribution (%) = (Product Gross Profit / Total Gross Profit) × 100



This measures the share of total gross profit contributed by a product.



\### 5. Cost Ratio



\*\*Formula:\*\*



Cost Ratio (%) = (Cost / Sales) × 100



This measures the recorded cost as a percentage of sales.



\### 6. Profit per Unit



\*\*Formula:\*\*



Profit per Unit = Gross Profit / Units Sold



This estimates gross profit per recorded unit, assuming the units and financial totals use compatible aggregation.



\### 7. Estimated Scenario Profit



\*\*Formula:\*\*



Estimated Sales = Current Sales × (1 + Price Change / 100)



Estimated Cost = Current Cost × (1 + Cost Change / 100)



Estimated Gross Profit = Estimated Sales − Estimated Cost



These scenario calculations assume that units sold remain constant.



\---



\## ⚠️ Assumptions and Limitations



This project has several important limitations.



\### Dataset Limitations



\* Findings depend on the accuracy and coverage of the supplied dataset.

\* The meaning of the `Cost` field determines how gross margin should be interpreted.

\* The dataset does not necessarily represent every operating expense of a distributor.

\* Historical patterns do not guarantee future results.



\### Scenario Simulator Limitations



\* The simulator assumes units sold remain constant.

\* It does not model demand, price elasticity or competitor responses.

\* It does not model taxes, additional operating expenses or changes in product mix.

\* Its results should be treated as hypothetical calculations, not forecasts.



\### Margin Screening Limitations



\* Below-median margin does not mean a product is making a loss.

\* Product comparisons do not account for every strategic or operational factor.

\* Pricing recommendations require additional information before implementation.



\### Dashboard Limitations



\* All displayed results depend on the selected filters.

\* Monthly aggregations reflect the dates available in the dataset.

\* Exported reports contain the data and summaries available in the current application.



\---



\## 🚀 Future Enhancements



Potential improvements include:



\* Automated anomaly detection for unusual sales and profit changes.

\* Advanced product segmentation.

\* Demand and sales forecasting.

\* More comprehensive cost analysis.

\* Interactive Pareto charts.

\* Product-level profitability alerts.

\* Improved executive KPI summaries.

\* Automated report generation.

\* Deployment of the dashboard to a cloud platform.

\* GitHub documentation with verified screenshots.

\* Unit tests and automated data validation.

\* A more polished, responsive dashboard layout.



These enhancements can be added incrementally as the project develops.



\---



\## 💼 Skills Demonstrated



This project demonstrates practical experience with:



\* Python programming.

\* Data cleaning and preprocessing.

\* Exploratory data analysis.

\* Data aggregation and transformation.

\* Financial KPI calculations.

\* Product and division profitability analysis.

\* Trend analysis.

\* Data visualization.

\* Interactive dashboard development.

\* Scenario analysis.

\* Business insight generation.

\* CSV reporting.

\* Project documentation.



\---



\## 👩‍💻 Author



\*\*Shreya Singh\*\*



Data Analyst Aspirant



Interested in data analytics, business intelligence, Python, data visualization and transforming raw data into actionable business insights.



\---



\## ⭐ Project Summary



The Nassau Candy Distributor Analytics project demonstrates how transaction-level data can be transformed into an interactive profitability analysis application.



By combining data cleaning, financial metrics, product comparisons, trend analysis, scenario simulation and dashboard reporting, the project provides a foundation for evidence-based business analysis.



\*\*Built with Python, Pandas, Plotly and Streamlit.\*\*



