import socket
import threading

def handle_client(conn, addr):
    print(f"cliente conectado desde {addr}")
    
    try:
        name = conn.recv(1024).decode()
        response = f"hola {name}, estas conectado a un servidor concurrente"
        conn.sendall(response.encode())
    except Exception as e:
        print(f"error  con {addr}: {e}")
    finally:
        conn.close()
        print(f"conexion cerrada con  {addr}")
        
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen()
 
print("servidor esperando conexion...")

while True:
    conn, addr = server.accept()
    
    client_thread = threading.Thread(
        target=handle_client,
        args=(conn, addr)
    )
    client_thread.start()
    