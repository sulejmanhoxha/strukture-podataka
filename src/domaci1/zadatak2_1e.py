def count_digits_recursive(n: int) -> int:
    """
    Rekurzivna funkcija koja prebrojava broj cifara zadatog broja.

    Args:
        n (int): Broj ciji se cifre broje

    Returns:
        int: Broj cifara zadatog broja
    """
    # Bazni slucaj: Ako je broj manji od 10, ima jednu cifru
    if n < 10:
        return 1

    # Rekurzivni slucaj: Broj cifara je 1 + broj cifara ostatka broja
    return 1 + count_digits_recursive(n // 10)


numbers_to_test = [
    4,
    12,
    123,
    1234,
    12345,
    123456,
    1234567,
    12345678,
    123456789,
    1234567890,
]

expected_results = {
    4: 1,
    12: 2,
    123: 3,
    1234: 4,
    12345: 5,
    123456: 6,
    1234567: 7,
    12345678: 8,
    123456789: 9,
    1234567890: 10,
}

for n, expected in expected_results.items():
    result = count_digits_recursive(n)
    if result == expected:
        print(f"{n} ima {result} cifara ✓")
    else:
        print(f"{n} ima {result} cifara ✗ (Očekivano: {expected})")
