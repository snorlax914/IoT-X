#클
from socket import *
import os
import sys
import time
import requests
import json

HOST = '192.168.0.23'
PORT = 9998
index = 0
old_fire_flag = '0'
while True:
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print('연결에 성공했습니다.')
    filePath = 'C:\\Users\\whisu\\OneDrive\\Desktop\\iot'
    fire_flag = client_socket.recv(10).decode('utf-8')
    if (fire_flag=='1') and (old_fire_flag == '0'):
        url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
        headers = {
            "Authorization": "Bearer " + "urWf1dr-a1k2XA5YNf_HcvJbOt4zGlTdISfgVzB4Cj10lwAAAYpGb_6E"
        }
        data = {
            "template_object" : json.dumps({ "object_type" : "text",
                                            "text" : "화재 발생",
                                            "link" : {
                                                        "web_url" : "https://localhost.com",
                                                        "mobile_web_url" : "https://localhost.com"
                                                    }
            })
        }
        response = requests.post(url, headers=headers, data=data)
        if response.json().get('result_code') == 0:
            print('메시지를 성공적으로 보냈습니다.')
        else:
            print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
            with open(filePath+"\\"+'fire_flag.txt', 'w') as f: #현재dir에 filename으로 파일을 받는다
                try:
                    f.write(fire_flag)
                except Exception as ex:
                    print(ex)

    filename = str(index) + '.jpg'
    client_socket.sendall(filename.encode('utf-8'))

    data = client_socket.recv(1024)
    data_transferred = 0
    

    if not data:
       print('파일 %s 가 서버에 존재하지 않음' %filename)
       sys.exit()

    with open(filePath+"\\"+filename, 'wb') as f: #현재dir에 filename으로 파일을 받는다
        try:
            while data: #데이터가 있을 때까지
                f.write(data) #1024바이트 쓴다
                data_transferred += len(data)
                data = client_socket.recv(1024) #1024바이트를 받아 온다
            index += 1
            if index == 6:
                index = 0
        except Exception as ex:
            print(ex)
    with open('C:\\Users\\whisu\\OneDrive\\Desktop\\iot\\flag_fire.txt', 'w') as f:
        try:
            f.write(fire_flag)
        except Exception as ex:
            print(ex)

    print(fire_flag)
    old_fire_flag = fire_flag
    print('파일 %s 받기 완료. 전송량 %d' %(filename, data_transferred))
    time.sleep(2)