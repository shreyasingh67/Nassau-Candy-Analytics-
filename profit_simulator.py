
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

# Display available products
print("===== AVAILABLE PRODUCTS =====")

for i, name in enumerate(products["Product Name"], start=1):
    print(f"{i}. {name}")

# Select a product
try:
    choice = int(input("\nEnter product number: "))

    if choice < 1 or choice > len(products):
        print("Invalid product number.")
        raise SystemExit

    product = products.iloc[choice - 1]

    # Read assumptions from user
    price_change = float(
        input("Selling price change (%) e.g. 10 or -5: ")
    )
    cost_change = float(
        input("Cost change (%) e.g. 5 or -3: ")
    )

    if price_change <= -100 or cost_change <= -100:
        print("Change cannot be -100% or lower.")
        raise SystemExit

    # Current figures
    sales = product["Sales"]
    cost = product["Cost"]
    current_profit = product["Gross Profit"]

    # Scenario assumptions:
    # Units sold remain constant.
    # Sales change with price.
    # Total cost changes by the entered cost percentage.
    new_sales = sales * (1 + price_change / 100)
    new_cost = cost * (1 + cost_change / 100)
    new_profit = new_sales - new_cost

    current_margin = current_profit / sales * 100
    new_margin = new_profit / new_sales * 100

    print("\n===== WHAT-IF SIMULATION =====")
    print("Product:", product["Product Name"])

    print("\nCurrent Gross Profit:", round(current_profit, 2))
    print("Estimated Gross Profit:", round(new_profit, 2))
    print("Profit Change:", round(new_profit - current_profit, 2))

    print("\nCurrent Gross Margin (%):", round(current_margin, 2))
    print("Estimated Gross Margin (%):", round(new_margin, 2))

    print("\nNote: This is a scenario estimate, not a forecast.")

except ValueError:
    print("Please enter valid numeric values.")