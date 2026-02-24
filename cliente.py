import socket
import threading

def simular_cliente(numero_cliente):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("127.0.0.1", 5000))

        name = f"Usuario_{numero_cliente}"
        client.sendall(name.encode())

        response = client.recv(1024).decode()
        print(f"Respuesta recibida: {response}")

        client.close()
    except Exception as e:
        print(f"Error en el cliente {numero_cliente}: {e}")

if __name__ == "__main__":
    print("Iniciando la llegada de 50 clientes al banco...")
    hilos_clientes = []

    # Lanza exactamente 50 hilos
    for i in range(1, 51):
        hilo = threading.Thread(target=simular_cliente, args=(i,))
        hilos_clientes.append(hilo)
        hilo.start()

    for hilo in hilos_clientes:
        hilo.join()

    print("Todos los clientes han salido del banco.")