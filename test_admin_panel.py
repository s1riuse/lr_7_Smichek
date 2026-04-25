import pytest
from django.test import Client

client = Client()

def test_main_page_opens():
    # Проверка, что главная страница открывается
    response = client.get('/')
    assert response.status_code == 200
    assert "Панель управления" in str(response.content)

def test_get_logs_returns_json():
    # Проверка, что /get_logs/ возвращает JSON
    response = client.get('/get_logs/')
    assert response.status_code == 200
    assert response['Content-Type'] == 'application/json'

def test_update_limits_works():
    # Проверка, что лимиты обновляются
    response = client.post('/update_limits/',
                           data='{"rate_limit": 7}',
                           content_type='application/json')
    assert response.status_code == 200
    assert response.json()['limits']['rate_limit'] == 7