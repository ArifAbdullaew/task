import requests  # Импортируем библиотеку requests для выполнения HTTP-запросов
import time  # Импортируем библиотеку time для работы с временем


# Функция для получения данных PPG по заданному id
def get_ppg_data(ppg_id):  # Формируем URL для GET-запроса с заданным id
    url = f"https://api.ec-leasing.ru/escmd_api_vkr2023/getppg/{ppg_id}"
    response = requests.get(url)  # Выполняем GET-запрос к серверу
    return response.json()  # Возвращаем результат запроса в формате JSON


# Функция для обработки данных PPG
def process_ppg_data(ppg_data):
    result = len(ppg_data)  # Вычисляем длину массива ppg_data
    return result, ppg_data  # Возвращаем результат вычисления


# Функция для отправки результатов на сервер
def send_results(ppg_id, result):
    url = f"https://api.ec-leasing.ru/escmd_api_vkr2023/postresults/{ppg_id}"  # Формируем URL для POST-запроса с заданным id
    json_data = {"result": result}  # Подготавливаем JSON с результатами и id
    response = requests.post(url, json=json_data)  # Выполняем POST-запрос к серверу с данными
    return response.json()  # Возвращаем результат запроса в формате JSON


# Основная функция, запускающая бесконечный цикл
def main():
    ppg_id = 100  # Задаем начальное значение PPG
    try:
        while True:  # Запускаем бесконечный цикл
            ppg_data = get_ppg_data(ppg_id)  # Получаем данные PPG с заданным id
            print(f"Received PPG data with id {ppg_id}")

            result, ppg_data = process_ppg_data(ppg_data)  # Обрабатываем данные PPG
            print(f"Processed PPG data. Result (Length): {result}")

            response = send_results(ppg_id, result)  # Отправляем результаты на сервер
            print(f"Sent results to server. Server response: {response}")

            ppg_id += 1 # Увеличиваем id PPG для следующей итерации
            time.sleep(15) # Приостанавливаем выполнение программы на 15 секунд

    except KeyboardInterrupt:
        print("Program manually interrupted. Exiting...")


if __name__ == "__main__":
    main()
