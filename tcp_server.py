import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 50000

sock.bind((host, port))
sock.listen(1)

print('Waiting connection ...')

# コネクションとクライアントの情報が返ってくる
connection, addr = sock.accept()
print('Connection from: ' + str(addr))

while True:
    # クライアントからデータを受信
    data = connection.recv(1024)

    # クライアントからexitというデータが送られてきたら終了
    if data == b'exit':
        break

    print('Recieved a message' + str(data))

    # クライアントにデータを送信
    connection.send(data)
    print('Sent a message: ' + str(data))

# connectinとsocketをクローズ
connection.close()
sock.close()

