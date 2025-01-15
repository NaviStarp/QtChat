# Aplicación de Chat P2P

Una aplicación de chat peer-to-peer desarrollada con Python y PySide6 que permite a los usuarios comunicarse directamente entre sí a través de una conexión de red.

## Características

- Mensajería directa peer-to-peer
- Inicialización automática del servidor
- Configuración de puerto personalizable
- Historial de chats recientes
- Gestión de solicitudes de conexión
- Asignación dinámica de puertos
- Interfaz gráfica intuitiva

## Requisitos Previos

- Python 3.11 o superior
- PySide6
- toml

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/NaviStarp/QtChat
cd QtChat3
```

2. Crea y activa un entorno virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # En Windows usar: .venv\Scripts\activate
```

3. Instala las dependencias necesarias:
```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

```
.
├── main.py                 # Punto de entrada de la aplicación
├── config.toml            # Configuración de la aplicación
├── chats.toml            # Historial de chats recientes
├── ui/                   # Archivos Python relacionados con la UI
│   ├── Chat.py
│   ├── chatReciente.py
│   ├── mensajeEnviado.py
│   ├── mensajeRecibido.py
│   ├── PaginaPrincipal.py
│   └── PeticionEntrante.py
├── widgets/              # Widgets personalizados
│   ├── chats_recientes.py
│   ├── peticionHandler.py
│   └── VentanaChat.py
├── res/                 # Recursos (archivos SVG)
└── styles/              # Hojas de estilo QSS
```

## Uso

1. Inicia la aplicación:
```bash
python main.py
```

2. La aplicación comenzará automáticamente a escuchar en el puerto configurado (por defecto: 12345)

3. Para conectarte con otro usuario:
   - Ingresa su dirección IP y puerto en los campos de conexión
   - Haz clic en "Conectar" para enviar una solicitud de conexión
   - Espera a que el otro usuario acepte la conexión

4. Para aceptar conexiones entrantes:
   - Las solicitudes de conexión aparecerán en la lista de peticiones entrantes
   - Haz clic en "Aceptar" para establecer la conexión o "Rechazar" para declinarla

## Configuración

La aplicación utiliza un archivo `config.toml` para almacenar la configuración:
- Configuración del puerto
- Conexiones recientes
- Preferencias de la aplicación

Puerto predeterminado: 12345 (puede modificarse en la configuración)

## Características en Detalle

### Inicialización Automática del Servidor
- La aplicación inicia automáticamente un servidor al arrancar
- Asignación dinámica de puerto si el puerto predeterminado no está disponible

### Gestión de Conexiones
- Manejo de solicitudes de conexión entrantes
- Mantiene una lista de conexiones recientes
- Muestra estado de conexión y notificaciones

### Interfaz de Usuario
- Diseño limpio e intuitivo
- Historial de chats recientes
- Notificaciones de solicitudes de conexión

## Desarrollo

El proyecto utiliza:
- PySide6 para la interfaz gráfica
- Programación con sockets para comunicaciones de red
- TOML para almacenamiento de configuración
- Recursos SVG para iconos

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.
