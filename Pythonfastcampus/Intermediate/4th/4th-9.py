# 예외처리
# try~except~finally

try:
    print(int('asdf'))
    print('alghost')
except Exception as e:
    print(e)
finally:
    print('done')