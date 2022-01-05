from google.auth import credentials
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)

gs = gspread.authorize(credentials)

doc = gs.open_by_url('https://docs.google.com/spreadsheets/d/1yN06LVB57fJwqC7BNdi0iMCErumQcrXxIB-aJr0JM80/edit#gid=0')
ws = doc.get_worksheet(0) # 첫번째 sheet을 가져오는 것

val = ws.acell('B1').value
print(val)

val2 = ws.row_values('1') # 1번째 행을 가져옴
print(val2)

val3 = ws.col_values('1') # 몇번째 열인지 지정
print(val3)

val4 = ws.range('A2:B3')
print(val4)

for val5 in val4:
    print(val5.value)    # 데이터 꺼내쓰기

ws.update_acell('B1', 'B1data_updated') # 특정 셀 업데이트
ws.append_row(['newA', 'newB', 'newC']) # 다음행에 데이터 행추가