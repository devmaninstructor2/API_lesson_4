# FULLCOSMOS

FULLCOSMOS - маленькая утилита, скачивающая фотографии с nasa и spacex и загружает их  в телеграм канал.


### Как установить
Предварительно необходимо создать телеграм бота и получить его токен; после создайте канал в телелеграм и получить его id; а также получите токен nasa

Далее, вам необходимо создать файл `.env` рядом с main.py и поместить свой NASA токен в переменную NASA_TOKEN, токен вашего бота телеграм в TG_TOKEN и id канала в телеграм в TG_CHAT_ID:
```python
NASA_TOKEN=NoCIHo8fhBS3PyclGht8EtBbe2VGrJoK5jk2dh4e
TG_TOKEN=2058949722:AAEpEgg2s_LocfJ930wts3nIqwEubaXrvEI
TG_CHAT_ID=@mychannelid
```

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```


### Примеры запуска

Запускается скрипт без использования аргументов, после чего по окончанию работы создадутся папки spacex, nasa_apod и nasa_epic рядом с main.py и в ваш телеграм канала будут загружаться картинки раз в сутки.

```
$ python main.py
```


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
