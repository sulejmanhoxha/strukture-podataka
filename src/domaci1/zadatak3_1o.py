def count_even_digits_recursive(n: int) -> int:
    """
    Rekurzivna funkcija koja prebrojava neparni brojeva u zadatom broju.

    Args:
        n (int): Broj ciji se neparni brojevi broje

    Returns:
        int: Broj neparnih brojeva u zadatom broju
    """
    # Bazni slucaj: Ako je broj manji od 10, provjeri je li neparni
    if n < 10:
        return 1 if n % 2 != 0 else 0

    # Rekurzivni slucaj: Broj neparnih brojeva je 1 + broj neparnih brojeva ostatka broja
    return (1 if n % 2 != 0 else 0) + count_even_digits_recursive(n // 10)


numbers_to_test = [4, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789, 1234567890, 2758270190183]

expected_results = {
    4: 0,
    12: 1,
    123: 2,
    1234: 2,
    12345: 3,
    123456: 3,
    1234567: 4,
    12345678: 4,
    123456789: 5,
    1234567890: 5,
    4365783464: 4,
    2758270190183: 7,
}

for n, expected in expected_results.items():
    result = count_even_digits_recursive(n)
    if result == expected:
        print(f"{n} ima {result} neparnih brojeva ✓")
    else:
        print(f"{n} ima {result} neparnih brojeva ✗ (Očekivano: {expected})")
