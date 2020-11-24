import os
import json
from jsonschema import Draft7Validator

BASE_DIR = os.path.abspath(os.getcwd())
json_files_path = os.path.join(BASE_DIR, 'json/event/')
schemas_path = os.path.join(BASE_DIR, 'json/schema/')


def validate_json(json_file, schema):
    error_list = ['Errors:']
    validator = Draft7Validator(schema)
    errors = sorted(validator.iter_errors(json_file), key=lambda e: e.path)
    for error in errors:
        error_list.append(' - ' + error.message + ' - pls, correct that')

    if error_list:
        return error_list
    else:
        return 'File is not valid'


json_files_list = os.listdir(json_files_path)
json_schemas_list = os.listdir(schemas_path)

with open('README_LOG.txt', mode='w', encoding='utf-8') as log:
    for number, file in enumerate(json_files_list, 1):

        log.writelines("\n№ of test: {0},\nFile - {1}\n".format(number, file))
        with open(os.path.join(json_files_path, file), mode='r', encoding='utf-8') as json_file:

            try:
                json_file = json.loads(json_file.read())  # having a py dict for json
            except TypeError:
                log.writelines('JSON file is not Valid or Empty\n')
                continue

            if not json_file:
                log.writelines('JSON file is empty\n')
                continue

            schema_name = json_file['event'] + '.schema'

            if schema_name not in json_schemas_list:
                log.writelines(f"SCHEMA file not found: {schema_name}, pls correct that\n")
                continue
            else:
                log.writelines(f"Schema: {schema_name}\n")

            with open(os.path.join(schemas_path, schema_name), mode='r') as schema:
                schema = json.loads(schema.read())

                log.writelines(f'{line}\n' for line in validate_json(json_file, schema))

    log.writelines('\nEnd of tests')
