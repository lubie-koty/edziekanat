def check_pesel(pesel: str) -> str:
    if len(pesel) != 11:
        raise ValueError("Passed PESEL is invalid")
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    checksum = sum(weight * int(number) for weight, number in zip(weights, pesel)) % 10
    checksum = 10 - checksum if checksum != 0 else checksum
    if checksum != int(pesel[-1]):
        raise ValueError("Passed PESEL is invalid")
    return pesel
