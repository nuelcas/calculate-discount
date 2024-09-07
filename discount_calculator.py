def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to apply.
    
    Returns:
    float: The final price after discount or the original price if discount is less than 20%.
    """
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price after discount
        final_price = price - discount_amount
        return final_price  # Return the final price
    else:
        return price  # Return the original price if discount is less than 20%

# Prompt the user for the original price
original_price = float(input("Enter the original price of the item: "))

# Prompt the user for the discount percentage
discount_percentage = float(input("Enter the discount percentage: "))

# Call the calculate_discount function to get the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price
print("The final price after applying the discount is:", final_price)
