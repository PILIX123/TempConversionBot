def celciusToFahrenheit(degrees: float) -> float:
    return (degrees*1.8)+32


def fahrenheitToCelcius(degrees: float) -> float:
    return round(((degrees-32)*(5/9)), 1)
