def convertTemperature(celsius:float) -> list[float]:
    return [celsius + 273.15, (celsius * 1.80) + 32]

print(convertTemperature(36.5))


