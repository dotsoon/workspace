import requests
import xmltodict
import pandas as pd
from collections import defaultdict

serviceKey = '9Td+AysuLzv3Fq4/SIhE/ri4rGiZiFjD92SQxmfQalI/2vW3xPEOcSNURc+LUMqpgZoCrTL8gD1mXFb1QhXBIg=='
url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'

params ={
  'serviceKey' : serviceKey, 
  'pageNo' : '1', 
  'numOfRows' : '10', 
  'startCreateDt' : '20200101', 
  'endCreateDt' : '20220107' 
}

response = requests.get(url, params=params)
print(response.status_code)

result = xmltodict.parse(response.text)
result

result.keys()
type(result['response'])
result['response'].keys()
result['response']['header']
result['response']['body'].keys()

print( result['response']['body']['numOfRows'])
print( result['response']['body']['pageNo'])
print( result['response']['body']['totalCount'])

# for row in result ['response']['body']['items']['item']:
#  print('날짜:', row['createDt'])
#  print('지역:', row['gubun'])
#  print('사망자 수:', row['deathCnt'])
#  print('확진자 수:', row['defCnt'])


confirmed = {}
for row in result['response']['body']['items']['item']:
  # print( row['createDt'].split(' ')[0])
  key = row['createDt'].split(' ')[0]

  if key in confirmed.keys():
    confirmed[key][row['gubun']] = row['defCnt']
  else:
    confirmed[key] = {}
    confirmed[key][row['gubun']] = row['defCnt']


confirm = defaultdict(dict)

for row in result['response']['body']['items']['item']:
  key = row['createDt'].split(' ')[0]
  locate = row['gubun']
  if locate != '검역' and locate != '합계':
    confirm[key][locate] = row['defCnt']

pd.DataFrame( confirm ).T.sort_index()

death = defaultdict(dict)
for row in result['response']['body']['items']['item']:
  key = row['createDt'].split(' ')[0]
  locate = row['gubun']
  if locate != '검역' and locate != '합계':
    death[key][locate] = row['deathCnt']

pd.DataFrame( death ).T.sort_index()

