def test_api_endpoint():
    import requests
    response = requests.get('http://localhost:5000/your_endpoint')
    assert response.status_code == 200
    assert 'expected_key' in response.json()