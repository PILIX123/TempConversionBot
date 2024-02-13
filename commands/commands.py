from utils.utils import findTempAndDegree
from converters.converter import celciusToFahrenheit, fahrenheitToCelcius


def reply(message: str) -> str:
    values = findTempAndDegree(message)
    if values == None:
        return
    match values[1].lower():
        case 'f':
            return f"{values[0]}°F is {fahrenheitToCelcius(values[0])}°C"
        case 'c':
            return f"{values[0]}°C is {celciusToFahrenheit(values[0])}°F"
