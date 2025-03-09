from bs4 import BeautifulSoup

with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

weather_data = []
for row in soup.find("table").find("tbody").find_all("tr"):
    cols = row.find_all("td")
    day = cols[0].text.strip()
    temp = int(cols[1].text.strip().replace("°C", ""))
    condition = cols[2].text.strip()
    weather_data.append((day, temp, condition))

print("5-Day Weather Forecast:")
for day, temp, condition in weather_data:
    print(f"{day}: {temp}°C, {condition}")

hottest_day = max(weather_data, key=lambda x: x[1])
print(f"\nHottest day: {hottest_day[0]} with {hottest_day[1]}°C")

sunny_days = [day for day, temp, condition in weather_data if condition == "Sunny"]
print(f"Sunny days: {', '.join(sunny_days)}")

avg_temp = sum(temp for _, temp, _ in weather_data) / len(weather_data)
print(f"Average Temperature: {avg_temp:.2f}°C")
