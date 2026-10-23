import json

def load_rooms(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

def save_rooms(file_path, rooms):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(rooms, file)

def show_rooms(rooms):
    for room in rooms:
        print(f"Room ID: {room["id"]}")
        print(f"Room type: {room["type"]}")
        print(f"Room price: {room["price"]}")
        print(f"Room available: {room["available"]}")

def get_available_rooms(rooms):
    available_rooms = []

    for room in rooms:
        if room["available"]:
            available_rooms.append(room)
    return available_rooms


def find_room_by_id(rooms, room_id):
    for room in rooms:
        if room["id"] == room_id:
            return room
    return None

def update_room_status(rooms, booking):
    room = find_room_by_id(rooms, booking["room_id"])

    if room:
        room["available"] = False

def find_room_by_type(rooms, room_type):
    correct_type = []
    
    for room in rooms:
        if room["type"] == room_type:
            correct_type.append(room)
    return correct_type