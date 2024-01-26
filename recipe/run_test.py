from timezonefinder import TimezoneFinder

tz = TimezoneFinder().timezone_at(lng=13.358, lat=52.5061)
assert tz == "Europe/Berlin"
