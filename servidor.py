import socket
import threading
import time
import asyncio

contador_clientes = 0
clientes_terminados = 0
banco_cerrado = None

async def handle_client(reader, writer):
    global contador_clientes, clientes_terminados, banco_cerrado
    
    addr = writer.get_extra_info('peername')
    
    # Asignamos el número de cliente rápidamente al llegar
    contador_clientes += 1
    mi_numero = contador_clientes
    print(f"[*] Cliente {mi_numero} conectado desde {addr}")

    try:
        # Espera datos del cliente
        data = await reader.read(1024)
        name = data.decode()
        
        print(f"[-] Atendiendo a {name}... por favor espere.")
        
        # --- ATENCIÓN ASÍNCRONA (Aquí va el delay de 5 segundos) ---
        await asyncio.sleep(5) 
        
        # Construye la respuesta
        response = f"Hola {name}, eres el cliente numero {mi_numero}"
        writer.write(response.encode())
        await writer.drain()
        
        print(f"[+] Cliente {mi_numero} ({name}) atendido y respondido.")
        
    except Exception as e:
        print(f"[!] Error con {addr}: {e}")
        
    finally:
        # Cerrar conexión
        writer.close()
        await writer.wait_closed()
        
        # Sumamos al terminar de atenderlo, para llevar el control de los 50
        clientes_terminados += 1
        
        # Si ya se atendió al cliente número 50, se levanta la bandera de cierre
        if clientes_terminados >= 50:
            print("\n--- EL BANCO HA CERRADO LUEGO DE ATENDER A LOS 50 CLIENTES ---")
            banco_cerrado.set()

async def main():
    global banco_cerrado
    banco_cerrado = asyncio.Event() # Creamos la bandera de evento
    
    server = await asyncio.start_server(
        handle_client, '0.0.0.0', 5000
    )

    print("Servidor asíncrono del banco esperando a los 50 clientes concurrentes...")

    async with server:
        # El servidor queda en ejecución hasta que el evento del cliente 50 se active
        await banco_cerrado.wait()
        
if __name__ == "__main__":
    asyncio.run(main())