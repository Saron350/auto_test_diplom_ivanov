import sender_stand_request
import data
import configuration

# Тест, который полностью выполняет сценарий
def test_create_and_get_order_by_track():
    # Шаг 1: Создание заказа
    new_order_response = sender_stand_request.post_new_order(data.order_body)
    assert new_order_response.status_code == 201, "При создании заказа получен некорректный статус-код"

    # Шаг 2: Сохранение номера трека заказа
    track = new_order_response.json().get("track")
    assert track, "Номер трека заказа не был получен"

    # Шаг 3: Выполнение запроса на получение заказа по треку
    get_order_response = sender_stand_request.get_order_by_track(track)

    # Шаг 4: Проверка, что код ответа равен 200
    assert get_order_response.status_code == 200, "При получении заказа по треку получен некорректный статус-код"
    # Иван Иванов, 33-я когорта — Финальный проект. Инженер по тестированию плюс
    