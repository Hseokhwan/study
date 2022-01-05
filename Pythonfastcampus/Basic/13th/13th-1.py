def send_mail(from_email, to_email, subject, contents):
    print('From:\t' + from_email)
    print('To:\t' + to_email)
    print('subject: ' + subject)
    print('contents')
    print('*'*10)
    print(contents)
    print('*'*10)
    print('-'*10)
my_email = 'tjrghks2322@naver.com'

users = []
users.append({'name':'john', 'email':'john@gamail.com'})
users.append({'name':'ray', 'email':'ray@gamail.com'})
users.append({'name':'jay', 'email':'jaygamail.com'})


contents = '''Thank you
- Fastcampus'''

for user in users:
    title = 'Dear. ' + user['name']
    if '@' not in user['email']:
        continue
    send_mail(my_email, user['email'], title, contents)
