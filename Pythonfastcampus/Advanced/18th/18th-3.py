import requests
import datetime
import telepot

AUTH_KEY = '894dc5368ce9574789c64978581694a54daa4a3e'

today = datetime.date.today()
start_dt = today - datetime.timedelta(days=30)

args = {
    'bgn_de' : start_dt.strftime('%Y%m%d'),
    'end_de' : today.strftime('%Y%m%d'),
    'corp_cls' : 'Y',
    'sort' : 'crp',
    'page_no' : '2',
    'page_count' : '10'
}
args_str = ''
for k, v in args.items():
    args_str += '&%s=%s' % (k, v)


res = requests.get('https://opendart.fss.or.kr/api/list.json?crtfc_key=%s%s' % (AUTH_KEY, args_str))
data = res.json()

bot = telepot.Bot('1913272827:AAEDSjf8fqNwuJvw8ZXHw5WR41P_re6ti8Q')

if data['status'] != '000':
    bot.sendMessage('1824238459', '공시정보 조회 실패: ' + data['Message'])
    print(data['message'])
else:
    msg = ''
    data_list = data['list']
    for d in data_list:
        for k, v in d.items():
            msg += '%s: %s,' % (k, v)
        msg += '\n'

    bot.sendMessage('1824238459','공시정보 조회 성공\n' + msg)

    
