
import pandas as pd

# Load original dataset
df = pd.read_csv("Nassau Candy Distributor.csv")

# Standardize product names
df["Product Name"] = (
    df["Product Name"]
    .str.strip()
    .str.replace(r"\s*-\s*", " - ", regex=True)
)

# Summarize products
products = df.groupby(
    "Product Name", as_index=False
).agg({
    "Sales": "sum",
    "Cost": "sum",
    "Gross Profit": "sum",
    "Units": "sum"
})

# Display products
print("===== SELECT A PRODUCT =====")

for i, name in enumerate(products["Product Name"], start=1):
    print(f"{i}. {name}")

try:
    choice = int(input("\nEnter product number: "))

    if choice < 1 or choice > len(products):
        print("Invalid product number.")
        raise SystemExit

    product = products.iloc[choice - 1]

    sales = product["Sales"]
    cost = product["Cost"]
    current_profit = product["Gross Profit"]

    # Define three scenarios:
    scenarios = [
        ("Conservative", 2, 5),
        ("Balanced", 5, 3),
        ("Aggressive", 10, 5)
    ]

    results = []

    for name, price_change, cost_change in scenarios:

        new_sales = sales * (1 + price_change / 100)
        new_cost = cost * (1 + cost_change / 100)

        estimated_profit = new_sales - new_cost
        estimated_margin = estimated_profit / new_sales * 100

        results.append({
            "Scenario": name,
            "Price Change (%)": price_change,
            "Cost Change (%)": cost_change,
            "Estimated Sales": new_sales,
            "Estimated Cost": new_cost,
            "Estimated Gross Profit": estimated_profit,
            "Profit Change": estimated_profit - current_profit,
            "Estimated Margin (%)": estimated_margin
        })

    comparison = pd.DataFrame(results)

    print("\n===== SCENARIO COMPARISON =====")
    print("Product:", product["Product Name"])
    print("Current Gross Profit:", round(current_profit, 2))

    print(
        comparison.round(2).to_string(index=False)
    )

    comparison.to_csv(
        "scenario_comparison.csv", index=False
    )

    print("\nSaved: scenario_comparison.csv")

except ValueError:
    print("Please enter a valid product number.")