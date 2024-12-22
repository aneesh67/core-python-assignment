def seats(total_seats, booked_seats, book=None, cancel=None):
    if book and book not in booked_seats:
        booked_seats.append(book)
    if cancel and cancel in booked_seats:
        booked_seats.remove(cancel)
    available_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
    return available_seats

total_seats = 10
booked_seats = [2, 5, 7]
available = seats(total_seats, booked_seats, book=3, cancel=5)
print(f"Available seats: {available}")
