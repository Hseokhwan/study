import requests

AUTH_KEY = '894dc5368ce9574789c64978581694a54daa4a3e'

args = {
    'bgn_de' : '20210806',
    'end_de' : '20210806',
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

if data['status'] != '000':
    print(data['message'])
else:
    data_list = data['list']
    for d in data_list:
        print(d['corp_name'])
