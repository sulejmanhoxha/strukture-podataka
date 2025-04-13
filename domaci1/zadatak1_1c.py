def factorial_recursive(n):
    """
    Rekurzivna funkcija koja racuna faktorijel broja n.

    Primjer: 5! = 5 * 4 * 3 * 2 * 1 = 120

    Args:
        n (int): Broj ciji se faktorijel racuna

    Returns:
        int: Faktorijel broja n
    """
    # Bazni slucaj: 0! = 1
    if n == 0:
        return 1

    return n * factorial_recursive(n - 1)
