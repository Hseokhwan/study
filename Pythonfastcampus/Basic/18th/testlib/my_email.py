class Email:
    def __init__(self):
        self.from_email = ''
        self.to_email = ''
        self.subject = ''
        self.contents = ''

    def send_mail(self):
        print('From: ' + self.from_email)
        print('To: ' + self.to_email)
        print('Subject: ' + self.subject)
        print('Contents: ' + self.contents)

if __name__ == '__main__':
    e = Email()
    e.from_email = 'alghost@fastcampus.com'
    e.to_eamil = 'yskim@gmail.com'
    e.subject = 'subject'
    e.contents = 'contents'
    e.send_mail()
    
print(__name__) # 코드가 잘 실행되었는지 알려줌