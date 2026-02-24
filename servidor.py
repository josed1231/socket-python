import socket
import threading
import time

contador_clientes = 0
lock = threading.Lock()

def handle_client(conn, addr):
    global contador_clientes
    
    print(f"[*] Cliente conectado desde {addr}")
    
    try:
        name = conn.recv(1024).decode()
        
        # Simulamos la atención del banco con el delay de 5 segundos
        print(f"[-] Atendiendo a {name}... por favor espere.")
        time.sleep(5) 
        
        with lock:
            contador_clientes += 1
            numero = contador_clientes
        
        print(f"[+] Cliente {numero} ({name}) atendido desde {addr}")
        
        response = f"Hola {name}, eres el cliente numero {numero}"
        conn.sendall(response.encode())
        
    except Exception as e:
        print(f"[!] Error con {addr}: {e}")
    finally:
        conn.close()
        print(f"[*] Conexion cerrada con {addr}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen()
 
print("Servidor del banco esperando a los 50 clientes...")

# --- MODIFICACIÓN: Límite estricto de 50 conexiones ---
hilos_activos = []

for i in range(50):
    conn, addr = server.accept()
    
    client_thread = threading.Thread(
        target=handle_client,
        args=(conn, addr)
    )
    hilos_activos.append(client_thread)
    client_thread.start()

# Esperamos a que el servidor termine de atender a los 50 antes de cerrarse
for hilo in hilos_activos:
    hilo.join()

print("\n--- EL BANCO HA CERRADO. Se atendió al límite de 50 clientes. ---")
server.close()