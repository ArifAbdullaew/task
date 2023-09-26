вы

1) Клонируем репозиторий себе в IDE или скачиваем ZIP архив

``` bash
git clone <ссылка на репозиторий>
```

2) Переходим в репозиторий

``` bash
cd <Путь проекта>
```

3) Создаем виртуальное окружение и устанавливаем все необходимые зависимости

``` bash
python -m venv venv
```

```bash
.\venv\Scripts\activate
```

``` bash
py -m pip install -r requirements.txt
```

3)Запуск сервиса

```
py task.py
```