def generate_permutations(s, prefix="", permutations=None):
    """
    Generates all permutations of the given string recursively.
    
    Parameters:
    s (str): The remaining string to be permuted.
    prefix (str): The current permutation being built.
    permutations (list): A list to store all generated permutations.

    Returns:
    list: A list of all permutations of the input string.
    """
    # Initialize the list to store permutations on the first call
    if permutations is None:
        permutations = []

    # Base case: If the string is empty, add the completed permutation to the list
    if len(s) == 0:
        permutations.append(prefix)
    else:
        # Recursively build new permutations by fixing each character at the start
        for i in range(len(s)):
            new_prefix = prefix + s[i]  # Add the current character to the prefix
            remaining = s[:i] + s[i+1:]  # Remove the current character from the string
            generate_permutations(remaining, new_prefix, permutations)

    # Return the list of all generated permutations
    return permutations


def generate_permutations_unique(s, prefix="", results=None):
    """
    Generates unique permutations by storing results in a set.

    Parameters:
    s (str): The remaining string to be permuted.
    prefix (str): The current permutation being built.
    results (set): A set to store unique permutations.

    Returns:
    list: A list of unique permutations of the input string.
    """
    # Initialize the set to store unique permutations on the first call
    if results is None:
        results = set()

    # Base case: If the string is empty, add the completed permutation to the set
    if len(s) == 0:
        results.add(prefix)
    else:
        # Recursively build new permutations by fixing each character at the start
        for i in range(len(s)):
            new_prefix = prefix + s[i]  # Add the current character to the prefix
            remaining = s[:i] + s[i+1:]  # Remove the current character from the string
            generate_permutations_unique(remaining, new_prefix, results)

    # Convert the set of unique permutations to a list and return it
    if prefix == "":
        return list(results)


if __name__ == "__main__":
    # Input string from the user
    input_string = input("Enter a string: ")

    # Generate all permutations
    permutations = generate_permutations(input_string)

    # Generate only unique permutations
    unique_permutations = generate_permutations_unique(input_string)

    # Print the results
    print('Permutations: ', permutations)
    print('Unique Permutations: ', unique_permutations)
