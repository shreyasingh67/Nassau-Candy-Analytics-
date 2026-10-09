

import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================================
# PAGE CONFIGURATION
# ==================================================
st.set_page_config(
    page_title="Nassau Candy Analytics",
    page_icon="🍬",
    layout="wide"
)

# ==================================================
# LOAD DATA
# ==================================================
@st.cache_data
def load_data():
    df = pd.read_csv("Nassau Candy Distributor.csv")

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        dayfirst=True,
        errors="coerce"
    )

    df["Product Name"] = (
        df["Product Name"]
        .str.strip()
        .str.replace(r"\s*-\s*", " - ", regex=True)
    )

    df = df.dropna(subset=["Order Date"])

    return df


df = load_data()

# ==================================================
# DASHBOARD HEADER
# ==================================================
st.title("🍬 Nassau Candy Distributor")
st.subheader(
    "Product Line Profitability & Margin Performance"
)
st.caption("Interactive Business Intelligence Dashboard")

# ==================================================
# SIDEBAR FILTERS
# ==================================================
st.sidebar.title("Dashboard Filters")

divisions = sorted(df["Division"].dropna().unique())
regions = sorted(df["Region"].dropna().unique())

selected_divisions = st.sidebar.multiselect(
    "Select Division",
    divisions,
    default=divisions
)

selected_regions = st.sidebar.multiselect(
    "Select Region",
    regions,
    default=regions
)

st.sidebar.subheader("Date Range")

min_date = df["Order Date"].min().date()
max_date = df["Order Date"].max().date()

start_date = st.sidebar.date_input(
    "Start Date",
    value=min_date,
    min_value=min_date,
    max_value=max_date
)

end_date = st.sidebar.date_input(
    "End Date",
    value=max_date,
    min_value=min_date,
    max_value=max_date
)

if start_date > end_date:
    st.sidebar.error(
        "Start Date cannot be after End Date."
    )
    st.stop()

# ==================================================
# FILTER DATA
# ==================================================
filtered = df[
    df["Division"].isin(selected_divisions)
    & df["Region"].isin(selected_regions)
    & (df["Order Date"].dt.date >= start_date)
    & (df["Order Date"].dt.date <= end_date)
].copy()

if filtered.empty:
    st.warning(
        "No data found. Please change the filters or date range."
    )
    st.stop()

# ==================================================
# KEY PERFORMANCE INDICATORS
# ==================================================
total_sales = filtered["Sales"].sum()
total_cost = filtered["Cost"].sum()
total_profit = filtered["Gross Profit"].sum()
total_units = filtered["Units"].sum()

gross_margin = (
    total_profit / total_sales * 100
    if total_sales != 0 else 0
)

st.markdown("## 📊 Key Performance Indicators")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Total Revenue", f"${total_sales:,.2f}")
c2.metric("Total Cost", f"${total_cost:,.2f}")
c3.metric("Gross Profit", f"${total_profit:,.2f}")
c4.metric("Gross Margin", f"{gross_margin:.2f}%")
c5.metric("Units Sold", f"{total_units:,.0f}")

st.divider()

# ==================================================
# MONTHLY PERFORMANCE
# ==================================================
st.markdown("## 📈 Monthly Performance")

monthly = (
    filtered.set_index("Order Date")
    .resample("MS")
    .agg({
        "Sales": "sum",
        "Gross Profit": "sum",
        "Cost": "sum"
    })
    .reset_index()
)

monthly["Gross Margin (%)"] = (
    monthly["Gross Profit"]
    / monthly["Sales"].replace(0, float("nan"))
    * 100
)

left, right = st.columns(2)

with left:
    fig = px.line(
        monthly,
        x="Order Date",
        y=["Sales", "Gross Profit"],
        title="Monthly Revenue vs Gross Profit",
        markers=True,
        labels={
            "value": "Amount ($)",
            "Order Date": "Month",
            "variable": "Metric"
        }
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    fig = px.line(
        monthly,
        x="Order Date",
        y="Gross Margin (%)",
        title="Monthly Gross Margin Trend",
        markers=True
    )
    st.plotly_chart(fig, use_container_width=True)

st.dataframe(
    monthly.round(2),
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==================================================
# DIVISION PROFITABILITY
# ==================================================
st.markdown("## 🏢 Division Profitability")

division_summary = (
    filtered.groupby("Division", as_index=False)
    .agg({
        "Sales": "sum",
        "Cost": "sum",
        "Gross Profit": "sum",
        "Units": "sum"
    })
)

division_summary["Gross Margin (%)"] = (
    division_summary["Gross Profit"]
    / division_summary["Sales"].replace(0, float("nan"))
    * 100
)

division_total_profit = division_summary["Gross Profit"].sum()

division_summary["Profit Contribution (%)"] = (
    division_summary["Gross Profit"]
    / division_total_profit * 100
    if division_total_profit != 0 else 0
)

left, right = st.columns(2)

with left:
    fig = px.bar(
        division_summary,
        x="Division",
        y="Gross Profit",
        color="Division",
        title="Gross Profit by Division"
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.dataframe(
        division_summary.round(2),
        use_container_width=True,
        hide_index=True
    )

st.divider()

# ==================================================
# PRODUCT PROFITABILITY
# ==================================================
st.markdown("## 🍫 Product Profitability")

product_summary = (
    filtered.groupby("Product Name", as_index=False)
    .agg({
        "Sales": "sum",
        "Cost": "sum",
        "Gross Profit": "sum",
        "Units": "sum"
    })
)

product_summary["Gross Margin (%)"] = (
    product_summary["Gross Profit"]
    / product_summary["Sales"].replace(0, float("nan"))
    * 100
)

product_total_profit = product_summary["Gross Profit"].sum()

product_summary["Profit Contribution (%)"] = (
    product_summary["Gross Profit"]
    / product_total_profit * 100
    if product_total_profit != 0 else 0
)

product_summary = product_summary.sort_values(
    "Gross Profit", ascending=False
)

st.markdown("### Top 10 Products by Gross Profit")

top_products = product_summary.head(10).sort_values(
    "Gross Profit"
)

fig = px.bar(
    top_products,
    x="Gross Profit",
    y="Product Name",
    orientation="h",
    color="Gross Profit",
    title="Top 10 Products by Gross Profit"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("### Complete Product Performance Table")

st.dataframe(
    product_summary.round(2),
    use_container_width=True,
    hide_index=True
)

st.divider()

# ==================================================
# DOWNLOAD REPORTS
# ==================================================
st.markdown("## 📥 Download Reports")

d1, d2, d3 = st.columns(3)

with d1:
    st.download_button(
        "Download Filtered Transactions",
        data=filtered.to_csv(index=False).encode("utf-8"),
        file_name="filtered_transactions.csv",
        mime="text/csv"
    )

with d2:
    st.download_button(
        "Download Product Report",
        data=product_summary.to_csv(
            index=False
        ).encode("utf-8"),
        file_name="product_profitability_report.csv",
        mime="text/csv"
    )

with d3:
    st.download_button(
        "Download Division Report",
        data=division_summary.to_csv(
            index=False
        ).encode("utf-8"),
        file_name="division_profitability_report.csv",
        mime="text/csv"
    )

st.divider()

# ==================================================
# WHAT-IF PROFIT SIMULATOR
# ==================================================
st.markdown("## 🧪 What-If Profit Simulator")

st.write(
    "Explore how hypothetical price and cost changes "
    "may affect product profitability."
)

product_names = sorted(
    filtered["Product Name"].dropna().unique()
)

chosen_product = st.selectbox(
    "Choose a product",
    product_names
)

price_change = st.slider(
    "Selling price change (%)",
    min_value=-20,
    max_value=30,
    value=5
)

cost_change = st.slider(
    "Cost change (%)",
    min_value=-20,
    max_value=30,
    value=3
)

selected_product_data = filtered[
    filtered["Product Name"] == chosen_product
]

current_sales = selected_product_data["Sales"].sum()
current_cost = selected_product_data["Cost"].sum()
current_profit = selected_product_data["Gross Profit"].sum()

estimated_sales = current_sales * (1 + price_change / 100)
estimated_cost = current_cost * (1 + cost_change / 100)

estimated_profit = estimated_sales - estimated_cost

estimated_margin = (
    estimated_profit / estimated_sales * 100
    if estimated_sales != 0 else 0
)

profit_difference = estimated_profit - current_profit

s1, s2, s3 = st.columns(3)

s1.metric(
    "Estimated Gross Profit",
    f"${estimated_profit:,.2f}",
    f"${profit_difference:,.2f}"
)

s2.metric(
    "Estimated Gross Margin",
    f"{estimated_margin:.2f}%"
)

s3.metric(
    "Current Gross Profit",
    f"${current_profit:,.2f}"
)

st.info(
    "Assumption: units sold remain constant. This is a "
    "hypothetical scenario, not a forecast. Actual demand "
    "may change when prices change."
)

st.divider()

# ==================================================
# BUSINESS INSIGHTS & RECOMMENDATIONS
# ==================================================
st.markdown("## 💡 Business Insights & Recommendations")

insights = product_summary.copy()

if not insights.empty:
    top_product = insights.loc[
        insights["Gross Profit"].idxmax()
    ]

    low_margin_product = insights.loc[
        insights["Gross Margin (%)"].idxmin()
    ]

    median_margin = insights["Gross Margin (%)"].median()

    left, right = st.columns(2)

    with left:
        st.markdown("### 🏆 Top Profit Contributor")
        st.write(f"**Product:** {top_product['Product Name']}")
        st.metric(
            "Gross Profit",
            f"${top_product['Gross Profit']:,.2f}"
        )
        st.metric(
            "Gross Margin",
            f"{top_product['Gross Margin (%)']:.2f}%"
        )

    with right:
        st.markdown("### ⚠️ Lowest-Margin Product")
        st.write(
            f"**Product:** {low_margin_product['Product Name']}"
        )
        st.metric(
            "Gross Margin",
            f"{low_margin_product['Gross Margin (%)']:.2f}%"
        )
        st.metric(
            "Gross Profit",
            f"${low_margin_product['Gross Profit']:,.2f}"
        )

    st.markdown("### 🔎 Margin Risk Screening")

    risk_products = insights[
        insights["Gross Margin (%)"] < median_margin
    ].sort_values("Gross Margin (%)")

    st.write(
        f"Median product gross margin: **{median_margin:.2f}%**"
    )

    if risk_products.empty:
        st.success(
            "No products are below the median margin "
            "in the current selection."
        )
    else:
        st.dataframe(
            risk_products[
                [
                    "Product Name",
                    "Sales",
                    "Cost",
                    "Gross Profit",
                    "Gross Margin (%)"
                ]
            ].round(2),
            use_container_width=True,
            hide_index=True
        )

    st.caption(
        "Below-median margin is a screening signal, not proof "
        "of a loss. Review pricing, costs and sales volume."
    )

    st.markdown("### 🧠 Business Recommendations")

    st.write(
        f"1. **Protect the leading product:** "
        f"{top_product['Product Name']} has the highest gross "
        f"profit in the current filtered data. Monitor its "
        f"availability and cost trends."
    )

    st.write(
        f"2. **Investigate low margin:** "
        f"{low_margin_product['Product Name']} has the lowest "
        f"gross margin in the current selection. Review its "
        f"price and costs before making changes."
    )

    st.write(
        "3. **Focus on profit contribution:** Prioritize products "
        "that contribute most to gross profit while monitoring "
        "lower-margin products."
    )

    st.info(
        "These are data-based recommendations, not proof of a "
        "specific cause. Results update with your selected filters."
    )

# ==================================================
# FOOTER
# ==================================================
st.divider()

st.caption(
    "Project: Product Line Profitability & Margin Performance Analysis"
)

st.caption(
    f"Analysis period: {start_date} to {end_date}"
)

st.caption(
    "Data source: Nassau Candy Distributor dataset."
)