def main(s,n,k):
    """
    The s string variable is given. return from index n to index k.
    Args:
        s(str): parameter
        n(int): parameter
        k(int): parameter
    Returns:
        str: answer
    """
    return s[n:k]

s,n,k = "codeacademy",2,6
print(main(s,n,k))