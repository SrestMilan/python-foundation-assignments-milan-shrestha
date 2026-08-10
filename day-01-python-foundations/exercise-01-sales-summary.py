# Product details
product_name = "Wireless Mouse"
unit_price = 1500
quantity_sold = 12
discount_percentage = 0.10


def calculate_and_display_sales(product_name, unit_price, quantity_sold, discount_percentage):
    """Calculate gross sales, discount amount, and final sales amount, then print the report."""
    gross_sales = unit_price * quantity_sold              # Total before discount
    discount_amount = gross_sales * discount_percentage   # Amount deducted
    final_sales = gross_sales - discount_amount            # Amount after discount

    print(f"Product      : {product_name}")
    print(f"Gross Sales  : NPR {gross_sales:.2f}")
    print(f"Discount     : NPR {discount_amount:.2f}")
    print(f"Final Sales  : NPR {final_sales:.2f}")


# Run the calculation and display the report
calculate_and_display_sales(product_name, unit_price, quantity_sold, discount_percentage)
