def maximum(value1, value2, value3):
    """Return the maximum of three values."""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value
print("Maximum number: ", max(12, 27, 36))
print("Minimum number: ",min(15, 9, 27, 14))
