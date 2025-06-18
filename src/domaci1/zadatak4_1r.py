def reverse_recursive(string: str) -> str:
    """
    Rekurzivna funkcija koja obrni zadani string.

    Args:
        string (str): Zadani string

    Returns:
        str: Obrnuti string
    """
    # Bazni slucaj: Ako je string prazan, vrati prazan string
    if len(string) == 0:
        return ""

    # Rekurzivni slucaj: Vrati string sa jednom prvom znakom
    return string[-1] + reverse_recursive(string[:-1])


strings_to_test = [
    "",
    "abc",
    "123",
    "1234",
    "12345",
    "123456",
    "1234567",
    "12345678",
    "123456789",
    "1234567890",
    "neka recenica za test",
]

expected_results = {
    "": "",
    "abc": "cba",
    "123": "321",
    "1234": "4321",
    "12345": "54321",
    "123456": "654321",
    "1234567": "7654321",
    "12345678": "87654321",
    "123456789": "987654321",
    "1234567890": "0987654321",
    "neka recenica za test": "tset az acinecer aken",
}

for string, expected in expected_results.items():
    result = reverse_recursive(string)
    if result == expected:
        print(f"'{string}' obrnuto je '{result}' ✓")
    else:
        print(f"'{string}' obrnuto je '{result}' ✗ (Ocekivano: '{expected}')")
