import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000)) 

server.listen(1) 

print("servidor esperando conexion...")
conn, addr = server.accept()
print("Cliente conectado", addr)

conn. sendall(b"hola desde el servidor")
conn.close()