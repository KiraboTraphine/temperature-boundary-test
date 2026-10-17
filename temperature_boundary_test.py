def classify_temperature(temperature):
    if temperature < 40:
        return "Normal"
    elif temperature <= 70:
        return "Warning"
    else:
        return "Critical"


# TEST READINGS
test_readings = [69, 70, 71]

for temperature in test_readings:
    print(
        temperature, "°C ->",
        classify_temperature(temperature)
    )