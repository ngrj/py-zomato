from zomato import Zomato
from pytest import fixture
import os

@fixture
def category_keys():
    return ['categories']

@fixture
def mumbai_json():
    return {'has_more': 0,'has_total': 0,'location_suggestions': [{'country_id': 1,'country_name': 'India','discovery_enabled': 0,'has_new_ad_format': 1,'id': 3,'is_state': 0,'name': 'Mumbai','should_experiment_with': 0,'state_code': '','state_id': 0,'state_name': ''}],'status': 'success'}

@fixture
def collections_keys():
    return ['has_more', 'display_text', 'collections', 'has_total', 'share_url']

@fixture
def cuisines_keys():
    return ['cuisines']

@fixture
def establishments_keys():
    return ['establishments']

@fixture
def geocode_keys():
    return ['nearby_restaurants', 'popularity', 'link', 'location']

@fixture
def locations_keys():
    return ['status', 'has_more', 'location_suggestions', 'has_total']

@fixture
def location_detail_keys():
    return ['top_cuisines', 'subzone', 'num_restaurant', 'city', 'nightlife_res', 'popularity', 'best_rated_restaurant', 'nightlife_index', 'nearby_res', 'location', 'popularity_res', 'subzone_id']

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
    assert set(collections_keys()).issubset(zomato.get_collections(city_id=3).keys())
    assert set(cuisines_keys()).issubset(zomato.get_cuisines(city_id=3).keys())
    assert set(establishments_keys()).issubset(zomato.get_establishments(city_id=3).keys())
    assert set(geocode_keys()).issubset(zomato.get_geocode(latitude="19.0985059",longitude="72.8850437").keys())
    res = zomato.get_locations(query="Bandra")
    assert set(locations_keys()).issubset(res.keys())
    assert set(location_detail_keys()).issubset(zomato.get_location_details(entity_type=res['location_suggestions'][0]['entity_type']
, entity_id=res['location_suggestions'][0]['entity_id']
).keys())