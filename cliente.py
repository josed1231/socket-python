import socket
import threading
import asyncio
import time

async def simular_cliente(numero_cliente):
    try:
        # Abre conexión con el servidor
        reader, writer = await asyncio.open_connection("127.0.0.1", 5000)

        # Solicita / Crea el nombre del cliente
        name = f"Usuario_{numero_cliente}"
        
        # Envía el nombre al servidor
        writer.write(name.encode())
        await writer.drain()

        # Espera respuesta del servidor
        data = await reader.read(1024)
        print(f"Respuesta cliente {numero_cliente}: {data.decode()}")

        # Cierra la conexión
        writer.close()
        await writer.wait_closed()
        
    except Exception as e:
        print(f"Error en el cliente {numero_cliente}: {e}")

async def main():
    print("Iniciando llegada masiva de 50 clientes (Asíncrono)...")
    
    # Guarda el tiempo inicial
    start_time = time.time()
    
    # Creamos una lista de 50 tareas asíncronas
    tareas = []
    for i in range(1, 51):
        # En vez de arrancar un hilo con thread.start(), programamos una tarea (corutina)
        tarea = simular_cliente(i)
        tareas.append(tarea)
        
    # --- LANZAMIENTO CONCURRENTE ---
    # asyncio.gather ejecuta todas las tareas a la vez de forma concurrente
    await asyncio.gather(*tareas)

    # Guarda el tiempo final
    end_time = time.time()
    
    # Calcula el tiempo total de atención (como en tu imagen)
    print("\nTodos los clientes salieron del banco.")
    print(f"Tiempo total de atención: {round(end_time - start_time, 2)} segundos")

if __name__ == "__main__":
    asyncio.run(main())