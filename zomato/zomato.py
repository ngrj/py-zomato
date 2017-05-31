import requests

class Zomato(object):

    def __init__(self, key=None, url="https://developers.zomato.com/api/v2.1/"):
        self.developer_key = key
        self.base_url = url

    def set_developer_key(self, key):
        self.developer_key = key

    def get_developer_key(self):
        return self.developer_key

    def get_base_url(self):
        return self.base_url

    def get_request_headers(self, developer_key=None, response_type="application/json"):
        return {'Accept':response_type,'user-key':developer_key}
    
    def get_request_url(self, endpoint):
        return "{0}{1}".format(self.base_url, endpoint)
    
    def make_get_request(self, url, params=None, headers=None):
        req = requests.get(url, params=params, headers=headers)
        return req
    
    def get_categories(self):
        developer_key = self.get_developer_key()
        request_headers = self.get_request_headers(developer_key=developer_key)
        req = self.make_get_request(url = self.get_request_url("categories"), headers=request_headers)
        return req.json()

    def get_cities(self, city_ids=[], query="", latitude="", longitude="", count=25):
        city_ids = ",".join(city_ids)
        params = {'city_ids':city_ids, "q":query, "lat": latitude, "long": longitude, "count": count}
        developer_key = self.get_developer_key()
        request_headers = self.get_request_headers(developer_key=developer_key)
        req = self.make_get_request(url = self.get_request_url("cities"), params = params, headers = request_headers)
        return req.json()