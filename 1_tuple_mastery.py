def flight_itineraries(itineraries):
    result = ""
    for index, itinerary in enumerate(itineraries, 1):
        name, origin, destination = itinerary
        result += f"Itinerary {index}: {name} - From {origin} to {destination}\n"
    return result.strip()

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
print(flight_itineraries(itineraries))
