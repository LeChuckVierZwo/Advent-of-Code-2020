with open("input") as f:
    seats_notbinary = f.readlines()

seats = []
for seat in seats_notbinary:
    seat = seat.replace("\n", "")
    row = int(seat[:7].replace("F", "0").replace("B", "1"), 2)
    column = int(seat[-3:].replace("L", "0").replace("R", "1"), 2)
    seat_id = row * 8 + column
    seats.append(seat_id)
seats = sorted(seats)
missing_seat = set(range(seats[0], seats[-1])) - set(seats)
print(list(missing_seat)[0])
print(max(seats))