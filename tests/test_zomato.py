from zomato import Zomato
from pytest import fixture
import os

@fixture
def category_keys():
    return ['categories']

@fixture
def mumbai_json():
    return {'has_more': 0,'has_total': 0,'location_suggestions': [{'country_id': 1,'country_name': 'India','discovery_enabled': 0,'has_new_ad_format': 1,'id': 3,'is_state': 0,'name': 'Mumbai','should_experiment_with': 0,'state_code': '','state_id': 0,'state_name': ''}],'status': 'success'}

def test_zomato():
    """
    Tests an API call to get zomato data
    """
    zomato_developer_key = os.environ.get('ZOMATO_API_KEY')
    zomato = Zomato()
    zomato.set_developer_key(zomato_developer_key)
    assert zomato.get_developer_key() == zomato_developer_key
    assert zomato.get_request_headers(developer_key=zomato_developer_key) == {'Accept':'application/json','user-key':zomato_developer_key} #, "developer key should be present"
    assert set(category_keys()).issubset(zomato.get_categories().keys())#, "All keys should be in the response"
    assert zomato.get_cities(query="Mumbai") == mumbai_json()