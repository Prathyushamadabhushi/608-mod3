def calculateTax(amount, taxPercent):
    return amount * taxPercent/100.0
    
def calculateTip(amount, tipPercent):
    return amount * tipPercent/100.0
    
def calculateTotal(amount, taxPercent, tipPercent):
    return amount * (1 + taxPercent/100.0 + tipPercent/100.0)
        
# #Create purchase object given an amount
# purchase = calculateTax(100.0);

# Set the tax and tip percentages
taxPercent = 7.5
tipPercent = 20.0

# Use the object to calculate tax and tip
tax = calculateTax(100.0, taxPercent)
tip = calculateTip(100.0, tipPercent)
total = calculateTotal(100.0, taxPercent, tipPercent)

# Display some useful information
print("calculate tax:", calculateTax(100.0, taxPercent))
print("calculate tip:", calculateTip(100.0, tipPercent))
print("calculate Total:", calculateTotal(100.0, taxPercent, tipPercent))
