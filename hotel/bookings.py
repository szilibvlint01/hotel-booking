import json


def load_bookings(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_bookings(file_path, bookings):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(bookings, file)


def create_booking(room, guest_name):
    booking = {
        "room_id" : room["id"],
        "room_type": room["type"],
        "guest": guest_name
    }
    return booking


def add_booking(bookings, booking):
    bookings.append(booking)

def show_bookings(bookings):
    for booking in bookings:
        print(f"Room ID: {booking["room_id"]}")
        print(f"Room type: {booking["room_type"]}")
        print(f"Guest: {booking["guest"]}")
        print("-----------------------------")