
"""
Exercise: Sales List Analysis
Student: Milan Shrestha
Day: 2
"""

monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

# 1. Rank sales from highest to lowest performing month
ranked_sales_desc = sorted(monthly_sales, reverse=True)

# 2. Keep only months that crossed the 100,000 mark (filter comprehension)
top_performing_months = [amount for amount in monthly_sales if amount > 100000]

# 3. Apply 13% tax to every month's sales (transform comprehension, no filtering)
sales_after_tax = [amount * 1.13 for amount in monthly_sales]

# 4. Sum all months to get total revenue for the period
total_revenue = sum(monthly_sales)

# 5. Divide total revenue by number of months to get the average
average_monthly_revenue = total_revenue / len(monthly_sales)

print(f"Ranked high to low: {ranked_sales_desc}")
print(f"Months above 100,000: {top_performing_months}")
print(f"Sales after 13% tax: {sales_after_tax}")
print(f"Total revenue: {total_revenue}")
print(f"Average monthly revenue: {average_monthly_revenue:.2f}")