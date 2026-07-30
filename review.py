# demo.py
def handle_request(req):
    user = fetch_account_owner(req["id"])   # this function is defined NOWHERE in the repo
    return user
