from app.models.user import User
from app.models.place import Place
import re

all_users = {}
all_places = {}

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

