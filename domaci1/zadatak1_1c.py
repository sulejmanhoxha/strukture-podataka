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


numbers_to_test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

expected_results = {
    0: 1,
    1: 1,
    2: 2,
    3: 6,
    4: 24,
    5: 120,
    6: 720,
    7: 5040,
    8: 40320,
    9: 362880,
    10: 3628800,
}

for n, expected in expected_results.items():
    result = factorial_recursive(n)
    if result == expected:
        print(f"{n}! = {result} ✓")
    else:
        print(f"{n}! = {result} ✗ (Očekivano: {expected})")
