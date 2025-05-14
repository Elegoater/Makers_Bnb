from lib.homes_repository import HomesRepository
from lib.homes import Home
from datetime import datetime

def test_show_all_homes(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = HomesRepository(db_connection)
    homes = repository.all_homes()
<<<<<<< Updated upstream
    assert str(homes) == '[Home(1, Hotel room I found the key for, This wonderful room has an amazing city view. There is one ensuite bathroom, and three leopards. I do not know how they got in., Central London (most of the time), 100.0, 1), Home(2, The cave, Damp and smelly, Wales, 100.0, 2), Home(3, Garys garage, Room for more than a car, Front of Garys house, 1000.0, 2), Home(4, Steves shed, Better than Garys garage, Back of Steves house, 100.0, 2), Home(5, Barrys basement, Dark and dingy, At the bottom, 50.0, 2), Home(6, Carls climbingframe, Lots of fun to be had, Outside somewhere, 100.0, 2), Home(7, Andys attic, Large and lofty, At the top, 100.0, 2), Home(8, Grahams garden, Lots of room for activities, The back of Grahams house, 10.0, 2), Home(9, Tonys toilet, Fragrant, The bog, 3000.0, 2), Home(10, Freddies fruitbowl, Small and cosy, Kitchen counter, 200.0, 2), Home(11, Penelopes plane, Cosy stay in the cockpit, In the air, 30.0, 2), Home(12, Alanas allotment, Lovely fruit and veg, In a field, 100.0, 2), Home(13, Love island villa, Great spot for a fireside chat, Spain, 100.0, 2), Home(14, Ilonas igloo, Bit chilly, North Pole, 70.0, 2), Home(15, Torys treehouse, Dont visit if scared of heights, In a tree, 500.0, 2)]'
=======
    assert str(homes) == "[Home(1, test_title, test_description, test_location, 100.0, 1), Home(2, test_title2, test_description2, test_location2, 100.0, 2)]"
>>>>>>> Stashed changes

def test_create_home(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = HomesRepository(db_connection)
    repository.create_home("test_title3", "test_description3", "test_location3", 100.0, 1)
    homes = repository.all_homes()
    assert str(homes) == '[Home(1, Hotel room I found the key for, This wonderful room has an amazing city view. There is one ensuite bathroom, and three leopards. I do not know how they got in., Central London (most of the time), 100.0, 1), Home(2, The cave, Damp and smelly, Wales, 100.0, 2), Home(3, Garys garage, Room for more than a car, Front of Garys house, 1000.0, 2), Home(4, Steves shed, Better than Garys garage, Back of Steves house, 100.0, 2), Home(5, Barrys basement, Dark and dingy, At the bottom, 50.0, 2), Home(6, Carls climbingframe, Lots of fun to be had, Outside somewhere, 100.0, 2), Home(7, Andys attic, Large and lofty, At the top, 100.0, 2), Home(8, Grahams garden, Lots of room for activities, The back of Grahams house, 10.0, 2), Home(9, Tonys toilet, Fragrant, The bog, 3000.0, 2), Home(10, Freddies fruitbowl, Small and cosy, Kitchen counter, 200.0, 2), Home(11, Penelopes plane, Cosy stay in the cockpit, In the air, 30.0, 2), Home(12, Alanas allotment, Lovely fruit and veg, In a field, 100.0, 2), Home(13, Love island villa, Great spot for a fireside chat, Spain, 100.0, 2), Home(14, Ilonas igloo, Bit chilly, North Pole, 70.0, 2), Home(15, Torys treehouse, Dont visit if scared of heights, In a tree, 500.0, 2), Home(16, test_title3, test_description3, test_location3, 100.0, 1)]'


<<<<<<< Updated upstream
=======
    expected_homes = [
        Home(1, "test_title", "test_description", "test_location", 100.0, 1),
        Home(2, "test_title2", "test_description2", "test_location2", 100.0, 2),
        Home(3, "test_title3", "test_description3", "test_location3", 100.0, 1),
    ]
    assert homes == expected_homes
>>>>>>> Stashed changes

def test_find_home_by_id(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = HomesRepository(db_connection)
    homes = repository.find(1)
<<<<<<< Updated upstream
    assert str(homes) == 'Home(1, Hotel room I found the key for, This wonderful room has an amazing city view. There is one ensuite bathroom, and three leopards. I do not know how they got in., Central London (most of the time), 100.0, 1)'
=======
    assert str(homes) == "Home(1, test_title, test_description, test_location, 100.0, 1)"
>>>>>>> Stashed changes

def test_booked_dates(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = HomesRepository(db_connection)
    booked_dates = repository.fetch_booked_dates(1)
    assert str(booked_dates) == "[]"

def test_booked_dates_with_bookings(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = HomesRepository(db_connection)
    booked_dates = repository.fetch_booked_dates(2)
    assert str(booked_dates) == "[datetime.date(2000, 2, 5), datetime.date(2000, 2, 6)]"

def test_find_all(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = HomesRepository(db_connection)
    homes = repository.find_all(1)
    assert str(homes) == '[Home(1, Hotel room I found the key for, This wonderful room has an amazing city view. There is one ensuite bathroom, and three leopards. I do not know how they got in., Central London (most of the time), 100.0, 1)]'
    
def test_load_calendar_page(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = HomesRepository(db_connection)
    booked_dates = repository.fetch_booked_dates(2)
    days_on_calendar_page = repository.load_calendar_page(booked_dates, offset=0)
    assert str(days_on_calendar_page) == '[(datetime.date(2024, 12, 30), False), (datetime.date(2024, 12, 31), False), (datetime.date(2025, 1, 1), False), (datetime.date(2025, 1, 2), False), (datetime.date(2025, 1, 3), False), (datetime.date(2025, 1, 4), False), (datetime.date(2025, 1, 5), False), (datetime.date(2025, 1, 6), False), (datetime.date(2025, 1, 7), False), (datetime.date(2025, 1, 8), False), (datetime.date(2025, 1, 9), False), (datetime.date(2025, 1, 10), False), (datetime.date(2025, 1, 11), False), (datetime.date(2025, 1, 12), False), (datetime.date(2025, 1, 13), False), (datetime.date(2025, 1, 14), False), (datetime.date(2025, 1, 15), False), (datetime.date(2025, 1, 16), False), (datetime.date(2025, 1, 17), False), (datetime.date(2025, 1, 18), False), (datetime.date(2025, 1, 19), False), (datetime.date(2025, 1, 20), False), (datetime.date(2025, 1, 21), False), (datetime.date(2025, 1, 22), False), (datetime.date(2025, 1, 23), False), (datetime.date(2025, 1, 24), False), (datetime.date(2025, 1, 25), False), (datetime.date(2025, 1, 26), False), (datetime.date(2025, 1, 27), False), (datetime.date(2025, 1, 28), False), (datetime.date(2025, 1, 29), False), (datetime.date(2025, 1, 30), False), (datetime.date(2025, 1, 31), False), (datetime.date(2025, 2, 1), False), (datetime.date(2025, 2, 2), False)]'