# QA Automation Pytest UI | RealWorld Test UI App

---
Пример фреймворка UI тестов.

В качестве примера используется ресурс: [UI Test Automation
Playground](http://uitestingplayground.com)

## Описание

Данная реализация автотестов тестов уровня UI описана в качестве примера как необходимо разделять уровни.

### Базовый функционал для реализации [`core_ui`]
В базовом функционале представлены описания компонентов, страниц и их составляющих,
на основе которых можно описывать реализацию. 
В качестве основных составляющих описаны:

#### Компоненты

Это понятие, позволяющее декомпозировать интерфейс на независимые части. \
Например, [Button](https://github.com/Olesyakosyhk/qa-automation-pytest-ui/blob/master/core_ui/components/button.py),
[Input](https://github.com/Olesyakosyhk/qa-automation-pytest-ui/blob/master/core_ui/components/input.py)
или [Link](https://github.com/Olesyakosyhk/qa-automation-pytest-ui/blob/master/core_ui/components/link.py).

Также возможно комбинировать компоненты.\
Например, описать составной компонент Form, который с помощью ООП приема
"Композиция" будет содержать [Input](https://github.com/Olesyakosyhk/qa-automation-pytest-ui/blob/master/core_ui/components/input.py)
и [Button](https://github.com/Olesyakosyhk/qa-automation-pytest-ui/blob/master/core_ui/components/button.py).

Компоненты скрывают в себе логику Selenium'а и позволяют взаимодействовать НЕ через локатор.

Компоненты включаются в страницы, на которых они фактически присутствуют.\
Больше о концепции компонентов [здесь](https://ru.reactjs.org/docs/web-components.html#gatsby-focus-wrapper).

#### Страница
Это класс, содержащий функционал для взаимодействия со страницей.\
Для реализации паттерна Page Objects и Page Factory.


### Описание приложения [`app`]
На этом уровне представлена реализация страниц с соответствующими им компонентами.\
Так же реализованы уникальные, для некоторых страниц, методы. 
Например, для [dynamictable](https://github.com/Olesyakosyhk/qa-automation-pytest-ui/blob/master/app/pages/dynamictable_page.py) 
описаны присущие для этой странице методы.


### Тесты [`tests`]
На уровне тестов не затрагивается реализация взаимодействия с Selenium.
Уровень тестов использует уровень "описания приложения" для описания логики тестов, т.е. используется:
- Allure для составления отчета и описание шагов
- реализация страниц
- проверки


Библиотеки и фреймворки
---
| Название                                                      | Назначение                    | 
|---------------------------------------------------------------|-------------------------------|
| [Pytest](https://docs.pytest.org/)                            | Фреймворк для тестирования    |
| [Selenuim](https://selenium-python.readthedocs.io/index.html) | Фреймворк для тестирования UI |
| [Allure2](https://qameta.io/allure-report/) 	                 | Формирование отчётов          |
 

Переменные окружения
---
| Переменная                | Значения                 | Описание                                     | 
|---------------------------|--------------------------|----------------------------------------------|
| `WEB_DRIVER_WAIT_TIMEOUT` | `>= 0`                   | Ожидание поиска элемента на странице.        |
| `BASE_URL`                | `http://example.com`     | Ссылка на главную страницу.                  |
| `INCLUDE_BROWSERS`        | `chrome, firefox`        | Список браузеров. Указываются через запятую. |
| `CHROME_VERSION`          | `100.0.4896.60` `latest` | Версия браузера Chrome.                      |
| `FIREFOX_VERSION`         | `latest`                 | Версия браузера FireFox.                     |


Test marks
---
| Маркировка        | Описание                                                | 
|-------------------|---------------------------------------------------------|
| `regression`      | Запуск тестов, относящиеся к regression.                |

Больше маркеров можно посмотреть:
 - [в коде](https://github.com/Olesyakosyhk/qa-automation-pytest-ui/blob/master/tests/conftest.py)
 - набрав команду `pytest --markers`


Флаги запуска
---
| Флаг                                | Пример значения                  | Описание                                                                             | 
|-------------------------------------|----------------------------------|--------------------------------------------------------------------------------------|
| `--alluredir`                       | `./allure_results`               | Запуск с формированием отчёта Allure.<br/> По указанному пути будет выгружены данные |
| `--reruns`                          | `5`                              | Количество перезапусков в случае падения теста.                                      |
| `--reruns-delay`                    | `60`                             | Задержка между перезапусками (секунды).                                              |
| `-p`                                | `no:cacheprovider`               | Отключить кеширование результатов тестирования.                                      |
| `-sv`                               |                                  | Дополнительное описания процесса исполнения тестов.                                  |
| `-m`                                | `-m regression`                  | Запуск определенного набора тестов (маркировка).                                     |
| `-n`                                | `auto` `2` `4`                   | Параллельный запуск тестов на N процессорах                                          |
| `--log-cli-level`                   | `INFO` `ERROR`                   | Уровень логирования                                                                  |
| `--suppress-tests-failed-exit-code` |                                  | Замена exit code на 0, если есть неудачные тесты                                     |


Allure
---
| Команда                                             | Описание                         | 
|-----------------------------------------------------|----------------------------------|
| `pytest --alluredir=./allure_results tests/`        | Запуск тестов с Allure отчетом.  |
| `allure serve ./allure_results`                     | Запуск сервера Allure с отчетом. |
| `allure generate --clean --output ./allure_results` | Удалить сгенерированный отчет.   |


Структура проекта
---
```
.
├──app
│   ├──components               # Общие компоненты приложения
│   └───pages                   # Реализация страниц приложения
│
├───core                        # Настройки приложения
│
├───core_ui                     
│   ├───components              # Функционал для реализации UI компонентов
│   └───resources               # Статический код
│
├───tests
|   ├───cases                   # Реализация тестовых случаев
│   ├───fixtures                
│   └───utils                   # Вспомогательные скрипты для тестов
│
├──.env                         # Переменные окружения
├──.env.example                 # Пример переменных окружения
│
├──README.md
│
├──requirements.txt
│
└──setup.cfg                   # Настройки code style
```