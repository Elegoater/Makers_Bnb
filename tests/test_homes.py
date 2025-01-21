from lib.homes import Home

"""
Constructs with an id, title, description, location, price_per_night, user_id
"""

def test_constructs():
    home = Home(1, 'test_title', 'test_description', 'test_location', 'test_price_per_night', 'test_user_id')
    assert home.id == 1
    assert home.title == 'test_title'
    assert home.description == 'test_description'
    assert home.location == 'test_location'
    assert home.price_per_night == 'test_price_per_night'
    assert home.user_id == 'test_user_id'

    
"""
Artists with equal contents are equal
"""
def test_compares():
    home_1 = Home(1, 'test_title', 'test_description', 'test_location', 'test_price_per_night', 'test_user_id')
    home_2 = Home(1, 'test_title', 'test_description', 'test_location', 'test_price_per_night', 'test_user_id')
    assert home_1 == home_2

"""
Artists can be represented as strings
"""
def test_stringifying():
    home = Home(1, 'test_username', 'test_email', 'test_password')
    assert str(home) == "Home(1, test_title, test_description, test_location, test_price_per_night, test_user_id)"

