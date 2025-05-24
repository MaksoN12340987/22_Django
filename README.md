# Django



#### Запуск проекта
Перед запуском отркдактируйте файл: 
.env.sample
Заполните необходимые переменные и удалите ".sample" из названия

Запустите следующую команду в терминале, находясь в корневой дирректории проекта, чтобы увидеть результат работы всех функций:
```
python manage.py runserver
```

### Требование для запуска:
- python - v3.13
- django >=5.2.1
Для обновления зависимостей необходимо запустить в терминале:
```
poetry update
```


## Модуль manage
При запуске, из корневой папки проекта, будет запущена программа, в ней продемонстрированна работа всех функций


## Пакет catalog:
В пакете описано приложение, выводящие страницы home, contact и response
Внутри присутсвует модуль views.py, в нем описаны контроллеры обработки главной страницы и страницы контактов


## Пакет config
В нем присутствуют главные настройки проекта


******************************************************************************************************************

# Django

## Project launch
Run the following command in the terminal, being in the root directory of the project, to see the result of all functions:
```
python manage.py runserver
```

### Requirement for launch:
- python - v3.13
- django >=5.2.1
To update dependencies, you need to run in the terminal:
```
poetry update
```

## Module manage
When launched, from the root folder of the project, a program will be launched, it demonstrates the operation of all functions

## Package catalog:
The package describes the application that displays the home, contact and response pages
Inside there is a module views.py, it describes the controllers for processing the main page and the contact page

## Package config
It contains the main project settings
