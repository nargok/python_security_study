import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 50000

server = (ip, port)
sock.connect(server)

msg = ''
while msg != 'exit':
    # 標準入力からデータを取得
    msg = input('-> ')

    # サーバーにデータを送信
    sock.send(msg.encode())

    # サーバ-からデータを受信
    data = sock.recv(1024)

    # サーバーから受信したデータを出力
    print('Received from server: ' + str(data))

sock.close()

