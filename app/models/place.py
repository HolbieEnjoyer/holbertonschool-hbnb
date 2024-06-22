from app.models.entity import Entity

class Place(Entity):
    def __init__(self, name, description, address, city, latitude, longitude, num_rooms, num_bathrooms, price_per_night, max_guests):
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
        self.host = None
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.amenities = set()
        self.reviews = {}

    def clean(self):
        self.amenities.clear()
        self.reviews.clear()
        self.host = None
        pass

    def add_review(self, user, review):
        if user.email in self.reviews:
            print("You have already left a review on this place")
            return
        review.user = user.email
        user.reviews.append(self.id)
        self.reviews.update({user.email: review})
        pass

    def add_amenity(self, amenity):
        self.amenities.add(amenity)
        pass

    def list_reviews(self):
        for r in self.reviews.values():
            print(r)
            print("################################")
        pass



    def __eq__(self, place):
        if (not isinstance(place, Place)):
            return False 
        return self.name == place.name and self.address == place.address and self.city == place.city and self.latitude == place.latitude and self.longitude == place.longitude

    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nAddress: {self.address}\nCity: {self.city}\nLatitude: {self.latitude}\nLongitude: {self.longitude}\nHost: {self.host and self.host.email} \nNumber of Rooms: {self.num_rooms}\nNumber of Bathrooms: {self.num_bathrooms}\nPrice per Night: {self.price_per_night}\nMax Guests: {self.max_guests}\nAmenities: {self.amenities}\nReviews: {self.reviews.__len__()}"
        
