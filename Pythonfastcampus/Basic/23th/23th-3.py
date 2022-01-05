from openpyxl import load_workbook
wb = load_workbook('simple_data.xlsx')
data = wb['Sheet_test'] # 인덱싱으로 원하는 sheet 가져올 수 있음

area = data['A1:B2'] # 행 순서로 출력
for row in area:
    for cell in row:
        print(row.value) # for 문이 2번인 이유: area를 담은 row 변수는 행마다 나누어져있는 튜플 데이터, 그걸 다시 변수 cell에 넣어서 각 cell 값 출력

print('-'*20)

cols = data['A:B'] # 열 순서로 출력
for col in cols:
    for cell in col:
        print(cell.value)

print('-'*20)

rows = data['1:2'] # 행 순서로 출력
for row in rows:
    for cell in row:
        print(cell.value)