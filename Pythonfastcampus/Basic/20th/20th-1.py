datafile = open('data.csv', 'r')

for line in datafile.readlines():      # readlines 모든 내용을 행 단위로 짤라서 읽어옴
    data = line.strip().split(',')    # , 단위로 쪼갬
    print(data[0])
    print(data[1])
    print(data[2])
    print('-'*10)


