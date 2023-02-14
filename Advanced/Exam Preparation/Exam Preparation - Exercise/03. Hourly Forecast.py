def forecast(*locations):

    weathers = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": []
    }

    for location_weather in locations:
        location, weather = location_weather
        try:
            weathers[weather].append(location)
        except KeyError:
            continue

    result = []
    for weather, locs in weathers.items():
        locs = sorted(locs)
        for loc in locs:
            result.append(f"{loc} - {weather}")

    return '\n'.join(result)


''' TESTS '''
# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))
# print()
# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))
# print()
# print(forecast(
#     ("Tokyo", "Rainy"),
#     ("Sofia", "Rainy")))
