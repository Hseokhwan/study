user_input = input('Input: ')
datafile = open('textfile.txt', 'a')  # a 는 append 약자
datafile.write(user_input+'\n')  
datafile.close()     