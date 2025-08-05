import requests
import configuration
import data

# Функция для создания нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

# Функция для получения заказа по его треку
def get_order_by_track(track):
    get_params = {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                        params=get_params)