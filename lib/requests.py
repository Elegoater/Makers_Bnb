class Request:
    def __init__(self, id, status, date_submitted, home_id, user_id, start_date, end_date):
        self.id = id 
        self.status = status
        self.date_submitted = date_submitted
        self.home_id = home_id
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date
    
    def __eq__(self, other):
        if isinstance(other, Request):
            return self.__dict__ == other.__dict__
        return False

    def __repr__(self):
        return f"Request({self.id}, {self.status}, {self.date_submitted}, {self.home_id}, {self.user_id}, {self.start_date}, {self.end_date})"
