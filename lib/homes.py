class Home:
    def __init__(self, id, title, description, location, price_per_night, user_id):
        self.id = id
        self.title = title
        self.description = description
        self.location = location
        self.price_per_night = price_per_night
        self.user_id = user_id

    def __repr__(self):
        return f"Home({self.id}, {self.title}, {self.description}, {self.location}, {self.price_per_night}, {self.user_id})"

    def __eq__(self, other):
            return self.__dict__ == other.__dict__
    

    # def is_valid(self):
    #     if self.title == None or self.title == "":
    #         return False
    #     if self.description == None or self.description == "":
    #         return False
    #     if self.location == None or self.location == "":
    #         return False
    #     if self.price_per_night == None or self.price_per_night == "":
    #         return False
    #     if self.price_per_night <= 0:
    #         return False
    #     return True

    # def generate_errors(self):
    #     errors = []
    #     if self.title == None or self.title == "":
    #         errors.append("Title is required")
    #     if self.description == None or self.description == "":
    #         errors.append("Description is required")
    #     if self.location == None or self.location == "":
    #         errors.append("Location is required")
    #     if self.price_per_night == None or self.price_per_night == "":
    #         errors.append("Price per night is required")
    #     if not isinstance(self.price_per_night, (int, float)):
    #         errors.append("Price per night must be a number")
    #     if self.price_per_night <= 0:
    #         errors.append("Price per night must be a positive number")
    #     return errors

    def is_valid(self) -> bool:
        return (
            bool(self.title)
            and bool(self.description)
            and bool(self.location)
            and isinstance(self.price_per_night, (int, float))
            and self.price_per_night > 0
        )

    def generate_errors(self) -> list[str]:
        errors = []
        if not self.title:
            errors.append("Title is required")
        if not self.description:
            errors.append("Description is required")
        if not self.location:
            errors.append("Location is required")
        if not isinstance(self.price_per_night, (int, float)):
            errors.append(f"Price per night must be a number, got {type(self.price_per_night).__name__}")
        elif self.price_per_night <= 0:
            errors.append("Price per night must be a positive number")
        return errors