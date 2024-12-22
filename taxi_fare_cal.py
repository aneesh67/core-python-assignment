def calculate_fares(trips):
    fares = [50 + 10 * trip for trip in trips]
    total_fare = sum(fares)
    for i, fare in enumerate(fares, 1):
        print(f"Trip {i}: ${fare}")
    print(f"Total Fare: ${total_fare}")

trips = [5, 10, 3]
calculate_fares(trips)
