from email.mime.text import MIMEText # Class
from email.mime.multipart import MIMEMultipart
import smtplib # 패키지
import re # 정규표현식

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USER = '' # 내 메일 주소
SMTP_PASSWORD = '' # 패스워드

def send_mail(name, addr, subject, contents, attachment=None): # None = 기본값을 지정하며 아무것도 없음을 의미, attachment가 없어도 전송 됌
    if not re.match('(^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', addr): # 적합한지 검사 ^,$ 문자열 시작과 끝을 의미
        print('Wrong email') # 확인용
        return

    msg = MIMEMultipart('alternative')
    if attachment:
        msg = MIMEMultipart('mixed') # msg 변수가 text, file 모두를 가질 수 있음을 의미

    msg['From'] = SMTP_USER
    msg['To'] = addr
    msg['Subject'] = name + '님, ' + subject

    text = MIMEText(contents, _charset='utf-8') # _charset 문자열 읽는 형식? 방법?
    msg.attach(text) # append와 비슷함

    if attachment:
        from email.mime.base import MIMEBase
        from email import encoders 

        file_data = MIMEBase('application', 'octect-stream') # 파일 타입
        file_data.set_payload(open(attachment, 'rb').read()) # rb는 r+b 바이너리로 읽겠다는 뜻
        encoders.encode_base64(file_data)

        import os
        filename = os.path.basename(attachment)
        file_data.all_header('Content=Disposition', 'attachment; filename="'+filename+'"')
        msg.attach(file_data)
        

    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    smtp.sendmail(SMTP_USER, addr, msg.as_string())
    smtp.close()

contents = ''' 안녕하세요,

자동화로 보내지는 메일입니다. '''    

send_mail('황석환', 'tjrghks2322@naver.com', '자동화 메일입니다.', contents)