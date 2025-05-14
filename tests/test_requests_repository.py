from lib.requests import Request
from lib.requests_repository import RequestRepository
from datetime import datetime

def test_list_all_requests(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = RequestRepository(db_connection)
    requests = repository.list_all_requests()
    assert requests == ["Request(1, unseen, 2000-01-01, 1, 1, 2000-02-05, 2000-02-07)", "Request(2, confirmed, 2000-01-01, 2, 2, 2000-02-05, 2000-02-07)"]

def test_create_request(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = RequestRepository(db_connection)
    # had to make sure this used a user_id and home_id that already existed in the db
    repository.create_request("unseen3", '2000-01-01', '2', '1', '2000-02-01', '2000-03-01')
    requests = repository.list_all_requests()
<<<<<<< Updated upstream
    assert requests == ['Request(1, unseen, 2000-01-01, 1, 1, 2000-02-05, 2000-02-07)', 'Request(2, confirmed, 2000-01-01, 2, 2, 2000-02-05, 2000-02-07)', 'Request(3, unseen, 2000-01-01, 2, 1, 2000-02-01, 2000-03-01)']

=======
    assert requests == ["Request(1, unseen, 2000-01-01, 1, 1, 2000-02-05, 2000-02-07)", "Request(2, confirmed, 2000-01-01, 1, 1, 2000-02-05, 2000-02-07)", 'Request(3, unseen, 2000-01-01, 2, 1, 2000-02-01, 2000-03-01)']
    
>>>>>>> Stashed changes
def test_find_request(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = RequestRepository(db_connection)
    request = repository.find_request(1)
    assert request == "Request(1, unseen, 2000-01-01, 1, 1, 2000-02-05, 2000-02-07)"
    # check this is the same as JOINS on db

def test_find_request_non_existent(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = RequestRepository(db_connection)
    request = repository.find_request(3)
    assert request == None

def test_update_request_dates(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = RequestRepository(db_connection)
    request = repository.update_request_dates('2000-02-01', '2000-02-15', 1)
    assert request == "Request(1, unseen, 2000-01-01, 1, 1, 2000-02-01, 2000-02-15)"

def test_update_request_dates_none(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = RequestRepository(db_connection)
    request = repository.update_request_dates(None, None, 1)
    assert request == "Request(1, unseen, 2000-01-01, 1, 1, None, None)"

def test_update_request_dates_non_existent(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = RequestRepository(db_connection)
    request = repository.update_request_dates('2000-02-01', '2000-02-15', 3)
    assert request == None
    
def test_delete_request(db_connection):
    db_connection.seed("seeds/makers_bnb.sql")
    repository = RequestRepository(db_connection)
    repository.delete_request(2)
    request = repository.list_all_requests()
    assert request == ["Request(1, unseen, 2000-01-01, 1, 1, 2000-02-05, 2000-02-07)"]

<<<<<<< Updated upstream
def test_list_requests_by_user_id(db_connection):
    db_connection.seed("seeds/makers_bnb.sql") 
    repository = RequestRepository(db_connection)
    request = repository.list_requests_by_user_id(1)
    assert str(request) == "[{'request_id': 1, 'status': 'unseen', 'date_submitted': datetime.date(2000, 1, 1), 'start_date': datetime.date(2000, 2, 5), 'end_date': datetime.date(2000, 2, 7), 'home_title': 'Hotel room I found the key for'}]"
=======
# def test_list_requests_by_user_id(db_connection):
#     db_connection.seed("seeds/makers_bnb.sql") 
#     repository = RequestRepository(db_connection)
#     request = repository.list_requests_by_user_id(1)
#     assert request == [{'request_id': 1, 'status': 'unseen', 'date_submitted': datetime.date(2000, 1, 1), 'start_date': datetime.date(2000, 2, 5), 'end_date': datetime.date(2000, 2, 7), 'home_title': 'test_title'}, {'request_id': 2, 'status': 'confirmed', 'date_submitted': datetime.date(2000, 1, 1), 'start_date': datetime.date(2000, 2, 5), 'end_date': datetime.date(2000, 2, 7), 'home_title': 'test_title'}]
        
>>>>>>> Stashed changes

def test_list_requests_by_user_id_when_user_has_no_requests(db_connection):
    db_connection.seed("seeds/makers_bnb.sql") 
    repository = RequestRepository(db_connection)
    request = repository.list_requests_by_user_id(3)
    assert request == []

def test_confirm_request(db_connection):
    db_connection.seed("seeds/makers_bnb.sql") 
    repository = RequestRepository(db_connection)
    request = repository.confirm_request(1)
    request = repository.find_request(1)
    assert request == "Request(1, confirmed, 2000-01-01, 1, 1, 2000-02-05, 2000-02-07)"

def test_deny_request(db_connection):
    db_connection.seed("seeds/makers_bnb.sql") 
    repository = RequestRepository(db_connection)
    request = repository.deny_request(1)
    assert request == None

def test_list_requests_by_homeowner_id(db_connection):
    db_connection.seed("seeds/makers_bnb.sql") 
    repository = RequestRepository(db_connection)
    request = repository.list_requests_by_home_owner(1)
    assert str(request) == "[{'request_id': 1, 'status': 'unseen', 'date_submitted': datetime.date(2000, 1, 1), 'start_date': datetime.date(2000, 2, 5), 'end_date': datetime.date(2000, 2, 7), 'home_title': 'Hotel room I found the key for'}]"

def test_list_requests_by_homeowner_id_when_homeowner_has_no_requests(db_connection):
    db_connection.seed("seeds/makers_bnb.sql") 
    repository = RequestRepository(db_connection)
    request = repository.list_requests_by_home_owner(3)
    assert request == []

def test_get_request_details_none(db_connection):
    db_connection.seed("seeds/makers_bnb.sql") 
    repository = RequestRepository(db_connection)
    request = repository.get_request_details(3)
    assert request == None

def test_get_request_details_existing(db_connection):
    db_connection.seed("seeds/makers_bnb.sql") 
    repository = RequestRepository(db_connection)
    request = repository.get_request_details(1)
    assert str(request) == "{'id': 1, 'status': 'unseen', 'date_submitted': datetime.date(2000, 1, 1), 'start_date': datetime.date(2000, 2, 5), 'end_date': datetime.date(2000, 2, 7), 'home_title': 'Hotel room I found the key for', 'home_location': 'Central London (most of the time)', 'requester_username': 'test_username', 'requester_email': 'test@email.com'}"