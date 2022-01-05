datafile = open('data.txt', 'r', encoding='utf-8')

line = 'init' # init 이 아닌 어떤 문자야도 상관 없음
while line:
    line = datafile.readline().strip() # readline 한줄씩 읽어오는 함수 / strip 은 문자 또는 공백 제거
    print(line)
