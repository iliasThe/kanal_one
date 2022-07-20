from pprint import pprint

import httplib2
import apiclient.discovery
import json
from oauth2client.service_account import ServiceAccountCredentials


# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'credentials.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1ihQECC6chfBblxIBB_nXLFMmfIdqjeAqublPs7geNt4'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

# Пример чтения файла
values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='A1:E51',
    majorDimension='ROWS'
).execute()
# pprint(values.get('values'))
pprint(values)
with open("sample.json", 'w') as out:
    data = json.dumps(values)
    out.writelines(data)


# # Пример записи в файл
# values = service.spreadsheets().values().batchUpdate(
#     spreadsheetId=spreadsheet_id,
# #     body={
# #         "valueInputOption": "USER_ENTERED",
# #         "data": [
# #             {"range": "B3:C4",
# #              "majorDimension": "ROWS",
# #              "values": [["This is B3", "This is C3"], ["This is B4", "This is C4"]]},
# #             {"range": "D5:E6",
# #              "majorDimension": "COLUMNS",
# #              "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
# # 	]
# #     }
# ).execute()