# JSON for Humans
#### A little script to validate a JSONs files by JSON-schemas

----
### Описание
Тестовое задания для ***Welltory***  
 
### Задача
> Вам предлагается задача на умение отлаживать данные и предоставлять результат в человеко-понятном виде.
> Необходимо написать скрипт, который сможет найти максимальное количество ошибок структуры и данных в первой папке.
> Примечание: часть ошибок может быть связано с JSON схемой, может с самими данными и ключами для них.

### Настройка и локальный запуск
- при желании скрипт ```validator.py``` находится в корне готовый к запуску

### Результаты валидации
```Дублирование с файла README_LOG.txt```

---
№ of test: 1,
File - 1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json
Schema: label_selected.schema
Errors:
 - 'id' is a required property - pls, correct that
 - 'labels' is a required property - pls, correct that
 - 'rr_id' is a required property - pls, correct that
 - 'timestamp' is a required property - pls, correct that
 - 'unique_id' is a required property - pls, correct that
 - 'user' is a required property - pls, correct that
 - 'user_id' is a required property - pls, correct that

№ of test: 2,
File - 297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json
Schema: sleep_created.schema
Errors:
 - 'source' is a required property - pls, correct that
 - 'timestamp' is a required property - pls, correct that
 - 'finish_time' is a required property - pls, correct that
 - 'activity_type' is a required property - pls, correct that
 - 'time_start' is a required property - pls, correct that
 - 'unique_id' is a required property - pls, correct that

№ of test: 3,
File - 29f0bfa7-bd51-4d45-93be-f6ead1ae0b96.json
JSON file is empty

№ of test: 4,
File - 2e8ffd3c-dbda-42df-9901-b7a30869511a.json
SCHEMA file not found: meditation_created.schema, pls correct that

№ of test: 5,
File - 3ade063d-d1b9-453f-85b4-dda7bfda4711.json
SCHEMA file not found: cmarker_calculated.schema, pls correct that

№ of test: 6,
File - 3b4088ef-7521-4114-ac56-57c68632d431.json
Schema: cmarker_created.schema
Errors:
 - 'cmarkers' is a required property - pls, correct that
 - 'datetime' is a required property - pls, correct that

№ of test: 7,
File - 6b1984e5-4092-4279-9dce-bdaa831c7932.json
SCHEMA file not found: meditation_created.schema, pls correct that

№ of test: 8,
File - a95d845c-8d9e-4e07-8948-275167643a40.json
JSON file is empty

№ of test: 9,
File - ba25151c-914f-4f47-909a-7a65a6339f34.json
SCHEMA file not found: label_       selected.schema, pls correct that

№ of test: 10,
File - bb998113-bc02-4cd1-9410-d9ae94f53eb0.json
Schema: sleep_created.schema
Errors:
 - 'source' is a required property - pls, correct that
 - 'timestamp' is a required property - pls, correct that
 - 'finish_time' is a required property - pls, correct that
 - 'activity_type' is a required property - pls, correct that
 - 'time_start' is a required property - pls, correct that
 - 'unique_id' is a required property - pls, correct that

№ of test: 11,
File - c72d21cf-1152-4d8e-b649-e198149d5bbb.json
SCHEMA file not found: meditation_created.schema, pls correct that

№ of test: 12,
File - cc07e442-7986-4714-8fc2-ac2256690a90.json
Schema: label_selected.schema
Errors:
 - 'id' is a required property - pls, correct that
 - 'labels' is a required property - pls, correct that
 - 'rr_id' is a required property - pls, correct that
 - 'timestamp' is a required property - pls, correct that
 - 'unique_id' is a required property - pls, correct that
 - 'user' is a required property - pls, correct that

№ of test: 13,
File - e2d760c3-7e10-4464-ab22-7fda6b5e2562.json
Schema: cmarker_created.schema
Errors:
 - 'cmarkers' is a required property - pls, correct that
 - 'datetime' is a required property - pls, correct that

№ of test: 14,
File - f5656ff6-29e1-46b0-8d8a-ff77f9cc0953.json
Schema: sleep_created.schema
Errors:
 - 'source' is a required property - pls, correct that
 - 'timestamp' is a required property - pls, correct that
 - 'finish_time' is a required property - pls, correct that
 - 'activity_type' is a required property - pls, correct that
 - 'time_start' is a required property - pls, correct that
 - 'unique_id' is a required property - pls, correct that

№ of test: 15,
File - fb1a0854-9535-404d-9bdd-9ec0abb6cd6c.json
Schema: cmarker_created.schema
Errors:
 - 'cmarkers' is a required property - pls, correct that
 - 'datetime' is a required property - pls, correct that

№ of test: 16,
File - ffe6b214-d543-40a8-8da3-deb0dc5bbd8c.json
Schema: cmarker_created.schema
Errors:
 - 'cmarkers' is a required property - pls, correct that
 - 'datetime' is a required property - pls, correct that
 - None is not of type 'integer' - pls, correct that

End of tests

---