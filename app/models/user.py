from app.models.entity import Entity
from app.models.place import Place
import re

all_users = {}
all_places = {}
class User(Entity):
    def __init__(self, first_name, last_name, email, password):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.places = []
        self.reviews = []

    def create_place(self, place):
        place = Place(place["name"], place["description"], place["address"], place["city"], place["latitude"], place["longitude"], place["num_rooms"], place["num_bathrooms"], place["price_per_night"], place["max_guests"])
        place.host = self;
        if (place not in all_places.values()):
            all_places.update({place.id: place})
            self.places.append(place.id)
        else:
            print("This place already exists you can't create another.")
            return None
        return place
    
    def remove_place(self, place_id):
        if (place_id in self.places):
            place = all_places[place_id]
            place.clean()
            self.places.remove(place_id)
            all_places.pop(place_id)
        else:
            print("This place does not exist.")
        pass

    def create_user(user):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", user["email"]):
            raise Exception("Invalid email")
        if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", user["password"]):
            raise Exception("Invalid password. Password must be at least 8 characters long and contain at least one letter and one number.")
        if (user["email"] in all_users):
            raise Exception("User already exists")
        user = User(user["first_name"], user["last_name"], user["email"], user["password"])
        all_users.update({user.email: user})
        return user

    def list_places(self):
        for rid in self.places:
            print(all_places[rid].name)
        pass

    def list_reviews(self):
        for rid in self.reviews:
            place = all_places[rid]
            print(f"{place.name}\n {all_places[rid].reviews.get(self.email)}")
        pass

    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nPassword: {self.password}\nPlaces: {self.places}\nReviews: {self.reviews.__len__()}"