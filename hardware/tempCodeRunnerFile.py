def userinfofromapi(email):
    """
    for testing. 
    """
    parameters = {"email": email}
    response = requests.get(url + "/userInfo", params = parameters)
    return response.json()