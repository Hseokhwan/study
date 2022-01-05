from openpyxl import load_workbook
wb = load_workbook('simple_data.xlsx') # 엑셀을 읽어서 파이썬으로 가져오는 클래스 변수
data = wb.active # Sheet 을 선택하는 과정, active는 활성화된 엑셀Sheet (가장 마지막에 활성화된 Sheet)

print(data['A1'].value)
print(data['A2'].value)
print(data['B1'].value)
print(data['B2'].value)

