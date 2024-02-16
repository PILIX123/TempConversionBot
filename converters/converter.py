def celciusToFahrenheit(degrees: float) -> float:
    return (degrees*1.8)+32


def fahrenheitToCelcius(degrees: float) -> float:
    return round(((degrees-32)*(5/9)), 1)


def LPHundredKMToMPGUS(liters: float) -> float:
    return round(235.215/liters, 2)


def LPHundredKMToMPGUK(liters: float) -> float:
    return round(282.418/liters, 2)


def MPGUSToMPGUK(mpg: float) -> float:
    return round(mpg*1.201, 2)


def MPGUKToMPGUS(mpg: float) -> float:
    return round(mpg/1.201, 2)


def MPGUSToLPHundredKM(mpg: float) -> float:
    return round(235.215/mpg, 2)


def MPGUKToLPHundredKM(mpg: float) -> float:
    return round(282.481/mpg, 2)
