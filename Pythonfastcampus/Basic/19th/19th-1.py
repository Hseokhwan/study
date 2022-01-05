datafile = open('data.txt', 'r', encoding='utf-8') # r 은 읽기전용으로 불러오는 것, 오류나서 encoding 넣음
data = datafile.read() # read 는 전체 내용을 읽어오는 함수(파일이 너무 크면 파이썬에 문제가 생길 수 있음)
print(data)