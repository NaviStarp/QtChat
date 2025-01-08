import os

from PySide6.QtCore import QFile, QTextStream
from PySide6.QtGui import QPixmap, Qt
from PySide6.QtWidgets import QWidget, QListWidgetItem, QMessageBox
from pex import toml

from ui.chatReciente import Ui_RecentChat
import ui.resources_rc


class RecentChatWidget(QWidget):
    def __init__(self, ip, port, last_connection,main_window):
        super().__init__()
        self.ui = Ui_RecentChat()  # No pasamos argumentos aquí
        self.ui.setupUi(self)
        self.main_window = main_window
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
        try:
            puerto_destino = int(port)
            self.ui.connectButton.setText("Esperando")
            self.ui.connectButton.setEnabled(False)

            # Enviar solicitud de conexión
            success, socket = self.main_window.request_handler.enviar_solicitud_conexion(ip, puerto_destino)
            if success:
                self.main_window._conectar_chat(socket)
                self.ui.connectButton.setEnabled(True)
                self.ui.connectButton.setText("Conectar")

            else:
                self.main_window._cancelar_solicitud()
                self.ui.connectButton.setEnabled(True)
                self.ui.connectButton.setText("Conectar")

        except ValueError:
            QMessageBox.warning(self, "Error", "Puerto inválido.")


import os
import toml

# def load_recent_chats(list_widget):
#     """Función para cargar los chats recientes en cualquier QListWidget"""
#     archivo_chats = "chats.toml"
#
#     # Verificar si el archivo existe
#     if not os.path.exists(archivo_chats):
#         print(f"Archivo {archivo_chats} no encontrado. Creando un archivo vacío...")
#         with open(archivo_chats, "w") as f:
#             toml.dump({"chats": []}, f)
#
#     try:
#         # Intentar cargar el archivo
#         chats_recientes = toml.load(archivo_chats).get("chats", [])
#     except toml.TomlDecodeError as e:
#         print(f"Error al cargar el archivo TOML: {e}")
#         chats_recientes = []  # Cargar una lista vacía en caso de error
#
#     list_widget.clear()
#
#     for chat in chats_recientes:
#         item = QListWidgetItem()
#         chat_widget = RecentChatWidget(
#             chat["ip"],
#             chat["port"],
#             chat["last_connection"],
#             main_window
#         )
#         item.setSizeHint(chat_widget.sizeHint())
#         list_widget.addItem(item)
#         list_widget.setItemWidget(item, chat_widget)

