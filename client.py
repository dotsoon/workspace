import socket

# 네트워크 통신을 하기 위한 소켓 객체를 생성
# Ipv4를 이용한 TCP 통신용 소켓
# 이렇게 생성된 소켓 객체를 통해서 서보와 통신(입/출력)을 할 수 있다
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('DEBUG:::소켓 생성 완료')

# 파일 입/출력할 때 open을 통해서 입/출력 하기 위한 파일 객체를 얻어 온 것처럼
# 통신(입/출력)하기 위한 서버와의 객체 생성
# 소켓 프로그래밍에서는 connect()를 통해서 통신 하기위한 서버의 객체를 얻어올 수 있다.
# 생성된 객체를 통해서 입/출력(통신)

# 읽거나 쓰기 위한 파일의 경로와 유사
# 통신하기 위한 네트워크 상의 경로 정도로 이해
serverAddress = socket.gethostbyname('info.cern.ch')
serverPort = 80

# 오픈하기 위한 서버의 경로는 튜플로 전달
sock.connect( (serverAddress, serverPort ))
print('DEBUG:::connect 완료')

# 서버에 HTML 코드를 요청 => Request Header
request_header = 'GET /index.html HTTP/1.1\r\n'
request_header += 'Host: info.cern.ch\r\n'
request_header += '\r\n'

# 요청대로 처리가 되어서 HTML 코드가 잘 다운 되는지 확인
sock.send( request_header.encode() )
response = sock.recv(1024)
print( response.decode() )




sock.close()