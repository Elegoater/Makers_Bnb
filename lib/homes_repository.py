from lib.homes import Home
import datetime

class HomesRepository:
    def __init__(self, connection):
        self.connection = connection

    def all_homes(self):
        homes = self.connection.execute("SELECT * FROM homes;")
        all_homes = []
        for home in homes:
            item = Home(home["id"], home["title"], home["description"], home["location"], home["price_per_night"], home["user_id"])
            all_homes.append(item)
        return all_homes
    
    def create_home(self, title, description, location, price_per_night, user_id):
        self.connection.execute("INSERT INTO homes (title, description, location, price_per_night, user_id) VALUES ('{}', '{}', '{}', '{}', '{}');".format(title, description, location, price_per_night, user_id))
        return None
    
    def find(self, id):
        home = self.connection.execute("SELECT * FROM homes WHERE id = {};".format(id))
        return Home(home[0]["id"], home[0]["title"], home[0]["description"], home[0]["location"], home[0]["price_per_night"], home[0]["user_id"])
    
    def fetch_booked_dates(self, home_id):
        requests = self.connection.execute("SELECT * FROM requests WHERE home_id = %s;", [home_id])
        booked_dates = []
        for request in requests:
            iter_date = request["start_date"]
            while iter_date < request["end_date"]:
                booked_dates.append(iter_date)
                iter_date += datetime.timedelta(days=1)
        return booked_dates
