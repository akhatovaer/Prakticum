import sender_stand_request
import data

# Основная функция
def test_order_by_track():
    # Шаг 1: Создать заказ и получить трекер
    response_new_order = sender_stand_request.post_new_order(data.body)
    assert response_new_order.status_code == 201
    tracker_number = response_new_order.json().get("track")

    # Шаг 2: Получить заказ по треку
    response_number = sender_stand_request.get_order_by_track(tracker_number)
    assert response_number.status_code == 200



