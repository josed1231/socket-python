import socket
import threading

contador_clientes = 0
lock = threading.Lock()

def handle_client(conn, addr):
    global contador_clientes
    
    print(f"cliente conectado desde {addr}")
    
    try:
        name = conn.recv(1024).decode()
        with lock:
            contador_clientes += 1
            numero = contador_clientes
        
        print(f"cliente {numero} atendido desde {addr}")
        
        response = f"hola {name}, eres el cliente numero {numero}"
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
    