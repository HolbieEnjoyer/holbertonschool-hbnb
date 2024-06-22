import app.application as app
from app.models.user import *
from app.models.review import Review

def main():
    john = User.create_user({
        "first_name": "John",
        "last_name": "Doe",
        "email": "peti@mail.com",
        "password": "petrolik1"
    })

    jane = User.create_user({
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "jane@mail.com",
        "password": "petrolik1"
    })

    place1 = john.create_place({
        "name": "Place 1",
        "description": "Description 1",
        "address": "Address 1",
        "city": "City 1",
        "latitude": 1.1,
        "longitude": 1.1,
        "num_rooms": 1,
        "num_bathrooms": 1,
        "price_per_night": 1,
        "max_guests": 1
    })

    place2 = john.create_place({
        "name": "Place 2",
        "description": "Description 1",
        "address": "Address 1",
        "city": "City 1",
        "latitude": 1.2,
        "longitude": 1.2,
        "num_rooms": 1,
        "num_bathrooms": 1,
        "price_per_night": 1,
        "max_guests": 1
    })

    place2.add_amenity("Toilet")
    place2.add_amenity("Wifi")
    place2.add_amenity("oled TV")

    place1.add_review(jane, Review(5.0, "Amazing place"))
    place1.add_review(john, Review(4.0, "I mean it's alright like"))
    place2.add_review(jane, Review(5.0, "Splendid"))
    print("=================================")

    print(place1)
    print("=================================")
    print(place2)

    print("\n\n")
    place1.list_reviews()

    jane.list_reviews()
    print("+++++++++++++++++++++++++++++++++")
    john.remove_place(place1.id)
    john.list_places()
    jane.list_places()
    print("+++++++++++++++++++++++++++++++++")
    print(place1)
    pass

if __name__ == "__main__":
    main()