def shortcut(s: str) -> str:
    """
    Removes all lowercase vowels from the given string and returns the result.
    
    Parameters:
    s (str): The input string from which lowercase vowels will be removed.
    
    Returns:
    str: The string with all lowercase vowels removed.
    """
    # Define the set of lowercase vowels
    vowels = 'aeiou'
    
    # Use a list comprehension to filter out vowels
    result = ''.join(char for char in s if char not in vowels)
    
    return result

# Example usage:
input_string = "Absolutely Fantastic"
result = shortcut(input_string)
print(result)  
