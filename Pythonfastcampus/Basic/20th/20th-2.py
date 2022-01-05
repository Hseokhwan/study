values = []
values.append(('alghost', 'fastone'))
values.append(('yskim', 'fastcampus'))
values.append(('jelee', 'fastfive'))

datafile = open('result.csv', 'w')

for line in values:
    data = ','.join(line)  # 구분자로 문자열 만듬
    datafile.write(data+'\n')
datafile.close()