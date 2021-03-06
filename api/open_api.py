
import requests
import json
url = 'https://openapi.naver.com/v1/datalab/search'
header = {
  'X-Naver-Client-Id': 'W0RV5qCq8s9QAQiwcCo5',
  'X-Naver-Client-Secret': 'Nj1HIrSNyf',
  'Content-Type': 'application/json'
}

data = {
  'startDate':'2021-01-01',
  'endDate':'2021-12-31',
  'timeUnit':'week',
  'keywordGroups':[
    {
      'groupName':'이재명',
      'keywords':['더불어민주당', '이재명']
    },
    {
      'groupName':'윤석열',
      'keywords':['국민의힘', '윤석열']
    }, 
    {
      'groupName':'허경영',
      'keywords':['국가혁명당', '허경영']
    },
    {
      'groupName':'안철수',
      'keywords':['국민의당', '안철수']
    },
    {
      'groupName':'심상정',
      'keywords':['정의당', '심상정']
    }
  ],
  'ages':['3', '4', '5', '6', '7', '8', '9', '10', '11']
}

jsonData = json.dumps(data)
response = requests.post( url, data=jsonData, headers=header )
print( response.status_code )

result = response.json()

