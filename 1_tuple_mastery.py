def flight_itineraries(itineraries):
    result = ""
    for index, itinerary in enumerate(itineraries, 1):
        name, origin, destination = itinerary
        itinerary_code = (index, name, "from", origin, "to", destination)
        print(itinerary_code)

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

flight_itineraries(itineraries)

