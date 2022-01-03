import urllib.request

# urllib은 urlretrieve함수를 이용해서 한 번에 파일로 저장
url = 'https://unsplash.com/photos/g9P21WrK_7g/download?ixid=MnwxMjA3fDB8MXxhbGx8NHx8fHx8fDJ8fDE2NDExODI0MTk&force=true'
path = 'web/data/download2.jpg'
urllib.request.urlretrieve( url, path )