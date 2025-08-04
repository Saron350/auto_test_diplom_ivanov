import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

def get_order_by_track(track):
    get_params = {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                        params=get_params)

# Тест создания заказа
def test_create_order():
    test_order = data.order_body.copy()
    response = post_new_order(test_order)
    assert response.status_code == 201, f"При создании заказа получен статус-код: {response.status_code}"

    if response.status_code == 201:
        resp_dict = response.json()
        track = resp_dict.get("track")
        assert track, "Track заказа не был получен"
        print("Track созданного заказа = ", track)
        return track
    else:
        print(f"Ошибка при создании заказа, статус-код: {response.status_code}")
        return None

# Тест получения заказа по треку
def test_get_order_by_track():
    track = test_create_order()  # Получаем track из теста создания
    if track:
        get_result = get_order_by_track(track)
        assert get_result.status_code == 200, f"При получении заказа по track получен статус-код: {get_result.status_code}"
        print("GET-запрос информации по заказу с использованием track завершился успешно!")
    else:
        print("Ошибка при получении track заказа, тест не выполнен")
        # Иван Иванов, 33-я когорта — Финальный проект. Инженер по тестированию плюс