def main(s,n):
    """
    The s string variable is given. return n characters from the beginning.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    return s[:n]
s,n = "codeacademy",4
print(main(s,n))