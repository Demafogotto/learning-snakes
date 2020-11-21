weather = {"city": "Moscow", "temperature": 20}
print(weather["city"])
weather["temperature"] = weather["temperature"] - 5
print(weather)
weather.get("country", "Russia")
weather["date"] = "27.05.2019"
print(len(weather))
