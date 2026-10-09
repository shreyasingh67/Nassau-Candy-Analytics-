
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Load cost and margin analysis
df = pd.read_csv("cost_margin_risk_analysis.csv")

# Graph 1: Product-wise Gross Margin
df_margin = df.sort_values("Gross Margin (%)")

plt.figure(figsize=(12, 7))
plt.barh(
    df_margin["Product Name"],
    df_margin["Gross Margin (%)"]
)
plt.axvline(
    df["Gross Margin (%)"].median(),
    linestyle="--",
    label="Median Product Margin"
)
plt.title("Product-wise Gross Margin Comparison")
plt.xlabel("Gross Margin (%)")
plt.ylabel("Product")
plt.legend()
plt.tight_layout()
plt.savefig("product_margin_comparison.png", dpi=200)
plt.close()

print("Saved: product_margin_comparison.png")

# Graph 2: Sales vs Cost
plt.figure(figsize=(9, 6))
plt.scatter(df["Sales"], df["Cost"])

for _, row in df.iterrows():
    if row["Product Name"] in [
        "Kazookles",
        "Lickable Wallpaper",
        "Wonka Bar - Scrumdiddlyumptious"
    ]:
        plt.annotate(
            row["Product Name"],
            (row["Sales"], row["Cost"]),
            fontsize=8
        )

plt.title("Product Sales vs Cost Analysis")
plt.xlabel("Sales")
plt.ylabel("Cost")
plt.grid(True)
plt.tight_layout()
plt.savefig("sales_vs_cost.png", dpi=200)
plt.close()

print("Saved: sales_vs_cost.png")
print("Both analysis graphs generated successfully!")