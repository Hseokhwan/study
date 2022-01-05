user_input = input('Input: ')
datafile = open('textfile.txt', 'w')
datafile.write(user_input+'\n')  # 기존 내용 삭제됌
datafile.close()      # open 후 close 는 한세트