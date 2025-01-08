import os

from PySide6.QtCore import QFile, QTextStream
from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QWidget, QListWidgetItem
from ui.chatReciente import Ui_RecentChat
import ui.resources_rc


class RecentChatWidget(QWidget):
    def __init__(self, ip, port, last_connection):
        super().__init__()
        self.ui = Ui_RecentChat()  # No pasamos argumentos aquí
        self.ui.setupUi(self)
        directorio_base = os.path.dirname(__file__)

        # Crear una ruta relativa para el archivo de estilos
        ruta_estilos = os.path.join( "styles", "styles.qss")

        # Cargar archivo de estilos
        file = QFile(ruta_estilos)
        if not file.open(QFile.ReadOnly | QFile.Text):
            print(f"Error al abrir el archivo de estilos: {ruta_estilos}")
            return

        # Leer y aplicar los estilos
        stream = QTextStream(file)
        self.setStyleSheet(stream.readAll())

        # Configurar los datos del chat
        self.ui.ipLabel.setText(f"IP: {ip}:{port}")
        self.ui.lastConnection.setText(f"Última conexión: {last_connection}")
        iconoEscalado = QPixmap(":/res/cuenta.svg").scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio,
                                  Qt.TransformationMode.SmoothTransformation)
        self.ui.profilePic.setPixmap(iconoEscalado)
        # Conectar el botón
        self.ui.connectButton.clicked.connect(lambda: self.connect_to_chat(ip, port))

    def connect_to_chat(self, ip, port):
        print(f"Conectando a {ip}:{port}")
        # Aquí irá tu lógica de conexión


def load_recent_chats(list_widget):
    """Función para cargar los chats recientes en cualquier QListWidget"""
    # Ejemplo de datos de chats recientes
    chats_recientes = [
        {"ip": "192.168.1.1", "port": "8080", "last_connection": "Hace 2 horas"},
        {"ip": "192.168.1.2", "port": "8081", "last_connection": "Hace 1 día"},
        {"ip": "192.168.1.3", "port": "8082", "last_connection": "Hace 3 días"}
    ]

    # Limpiar la lista actual
    list_widget.clear()

    # Agregar cada chat reciente a la lista
    for chat in chats_recientes:
        # Crear un QListWidgetItem
        item = QListWidgetItem()
        # Crear el widget personalizado
        chat_widget = RecentChatWidget(
            chat["ip"],
            chat["port"],
            chat["last_connection"]
        )
        # Establecer el tamaño del item basado en el widget
        item.setSizeHint(chat_widget.sizeHint())
        # Agregar el item a la lista
        list_widget.addItem(item)
        # Establecer el widget para el item
        list_widget.setItemWidget(item, chat_widget)
