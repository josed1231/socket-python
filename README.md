# socket-python

Este proyecto muestra cómo realizar una conexión entre un **servidor** y un **cliente** utilizando la librería `socket` de Python.

El objetivo es demostrar el funcionamiento básico de la comunicación en red bajo el modelo **cliente-servidor**, comúnmente utilizado en aplicaciones distribuidas.

---

## Descripción

Se implementa una conexión donde:

* El **servidor** se mantiene a la espera de solicitudes.
* El **cliente** se conecta al servidor.
* Se establece la comunicación entre ambos mediante sockets.
---

##  Tecnologías utilizadas

* Python
* Librería `socket`
---

## Funcionamiento

1. El servidor se ejecuta primero y queda en estado de escucha.
2. El cliente se ejecuta después e intenta conectarse al servidor.
3. Una vez establecida la conexión, se permite el intercambio de datos.

---

##  Evidencia de ejecución

### Servidor

<img width="1919" height="1007" alt="imagen servidor programacion distribuida" src="https://github.com/user-attachments/assets/21db8b92-8e82-413d-a6ba-60eeec4f9658" />

### Cliente

<img width="1915" height="1028" alt="imagen cliente programacion distribuida" src="https://github.com/user-attachments/assets/2ee34adf-b584-4020-bfce-92edc0f61a29" />

---

##  Cómo ejecutar el proyecto

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/josed1231/socket-python.git
   ```

2. Ejecutar el servidor:

   ```bash
   python server.py
   ```

3. En otra terminal, ejecutar el cliente:

   ```bash
   python client.py
   ```
