
import configuration
import requests
import data


#Функция создания нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                        json = body,
                        headers = data.headers)

response_new_order = post_new_order(data.body);
tracker = (response_new_order.json()["track"])

#Функция получения заказа по номеру
def get_order_by_track(tracker):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_NUMBER_PATH + "?t=" + str(tracker))

response_order_by_track = get_order_by_track(tracker);