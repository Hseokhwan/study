import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    'https://www.googleapis.com/auth/drive',
    'https://spreadsheets.google.com/feeds'
    ]
credentials = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)

gs = gspread.authorize(credentials)

doc = gs.create('온라인테스트2')

ws = doc.get_worksheet(0)

for i in range(5):
    ws.append_row([i, str(i) + 'data'])

doc.share('tjrghks3663@gmail.com', perm_type='user', role = 'owner')

