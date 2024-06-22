from app.models.entity import Entity

class Review(Entity):
    def __init__(self, rating, content):
        super().__init__()
        self.user = "InvalidUser"
        self.rating = rating
        self.content = content

    def __str__(self) -> str:
        return f"{self.user} Rating: {self.rating}\n{self.content}\n"