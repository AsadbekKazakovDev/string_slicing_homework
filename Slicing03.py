def main(s):
    """The s string variable is given. Return all characters except the one at the beginning and end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    return s[1:-1]
s = "Python"
print(main(s))
s = "Codeacademy"
print(main(s))