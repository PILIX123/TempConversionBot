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


def milesToKM(miles: float) -> float:
    return round(miles*1.609, 2)


def KMToMiles(km: float) -> float:
    return round(km/1.609, 2)


def yardToM(yard: float) -> float:
    return round(yard/1.094, 2)


def MToYard(m: float) -> float:
    return round(m*1.094, 2)


def inchToCM(inch: float) -> float:
    return round(inch*2.54, 2)


def CMToInch(cm: float) -> float:
    return round(cm/2.54, 2)


def CMToFoot(cm: float) -> float:
    return round(cm/30.48, 2)


def footToCM(ft: float) -> float:
    return round(ft*30.48, 2)
