from hotel.rooms import(
    load_rooms,
    save_rooms,
    show_rooms,
    get_available_rooms,
    find_room_by_id,
    update_room_status
)

from hotel.bookings import(
    load_bookings,
    save_bookings,
    create_booking,
    add_booking,
    show_bookings
)

def main():

    rooms = load_rooms("data/rooms.json")
    bookings = load_bookings("data/bookings.json")

    while True:

        print()
        print("Welcome to the Hotel!")
        print()
        print("1. Show available rooms.")
        print()
        print("2. Book room.")
        print()
        print("3. Show bookings.")
        print()
        print("4. Exit")

        choice = input("Choose an option: ")

        match choice:
            case "1":
                available_rooms = get_available_rooms(rooms)
                show_rooms(available_rooms)
            case "2":
                choose_room = input("Choose an available room: ")

                if not choose_room.isdigit():
                    print("Please enter a number.")
                else:
                    room = find_room_by_id(rooms, int(choose_room))

                    if room == None:
                        print("Room not found!")
                        continue
                    elif room["available"] == False:
                        print("Room is not available.")
                        continue
                    else:
                        name = input("What is your name? ")

                        booking = create_booking(room, name)
                        add_booking(bookings, booking)
                        update_room_status(rooms, booking)

                        save_rooms("data/rooms.json", rooms)
                        save_bookings("data/bookings.json", bookings)

                        print("Booking successful!")

            case "3":
                if len(bookings) == 0:
                    print("There are no bookings yet.")
                else:
                    show_bookings(bookings)

            case "4":
                print("Goodbye!")
                break

            case _:
                print("Choose a valid option.")

main()