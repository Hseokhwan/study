import requests

AUTH_KEY = '894dc5368ce9574789c64978581694a54daa4a3e'

res = requests.get('https://opendart.fss.or.kr/api/list.json?crtfc_key=%s&bgn_de=20210806&end_de=20210806&corp_cls=Y' % AUTH_KEY)
data = res.json()

data_list = data['list']
for d in data_list:
    print(d['corp_name'])