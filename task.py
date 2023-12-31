import requests  # Импортируем библиотеку requests для выполнения HTTP-запросов
import time  # Импортируем библиотеку time для работы с временем
import json

# Функция для получения данных PPG по заданному id
def get_ppg_data(ppg_id):  # Формируем URL для GET-запроса с заданным id
    url = f"https://api.ec-leasing.ru/escmd_api_vkr2023/getppg/{ppg_id}"
    response = requests.get(url)  # Выполняем GET-запрос к серверу

    return response.text  # Возвращаем результат запроса в формате JSON


# Функция для обработки данных PPG
def process_ppg_data(ppg_data):
    ppg_points = ppg_data[0]['data']  # Извлекаем список значений PPG из словаря
    result = len(ppg_points)  # Вычисляем длину списка точек
    return result, ppg_points


# Функция для отправки результатов на сервер
def send_results(ppg_id, result):
    url = f"https://api.ec-leasing.ru/escmd_api_vkr2023/postresults/{ppg_id}"  # Формируем URL для POST-запроса с заданным id
    json_data = {"result": result}  # Подготавливаем JSON с результатами и id
    response = requests.post(url, json=json_data)  # Выполняем POST-запрос к серверу с данными
    return response.json()  # Возвращаем результат запроса в формате JSON

def save_ppg_data_to_file(ppg_data):
    with open("ppg_data.txt", "w") as file:
        file.write(str(ppg_data))

# Основная функция, запускающая бесконечный цикл
def main():
    ppg_id = 100  # Задаем начальное значение PPG
    try:
        while True:  # Запускаем бесконечный цикл
            ppg_data = get_ppg_data(ppg_id)  # Получаем данные PPG с заданным id
            print(f"Received PPG data with id {ppg_id}")

            ppg_data = json.loads(ppg_data)  # Преобразуем строку JSON в объект Python
            result, ppg_data = process_ppg_data(ppg_data)
            print(f"Processed PPG data. Result (Length): {result}")

            response = send_results(ppg_id, result)  # Отправляем результаты на сервер
            print(f"Sent results to server. Server response: {response}")

            ppg_id += 1 # Увеличиваем id PPG для следующей итерации
            time.sleep(30) # Приостанавливаем выполнение программы на 15 секунд

    except KeyboardInterrupt:
        print("Program manually interrupted. Exiting...")


if __name__ == "__main__":
    main()
