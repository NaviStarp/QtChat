import os

from PySide6.QtWidgets import QMainWindow, QWidget, QListWidgetItem
from PySide6.QtCore import Qt, QDateTime, Signal, QObject, QMetaObject, QFile, QTextStream
import socket
import threading

from ui.Chat import Ui_MainWindow
from ui.mensajeEnviado import Ui_SentMessage
from ui.mensajeRecibido import Ui_ReceivedMessage


class MensajeHandler(QObject):
    mensaje_recibido = Signal(str)

    def __init__(self):
        super().__init__()


class VentanaChat(QMainWindow):
    def __init__(self, socket_cliente: socket.socket, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.cargar_estilos()


        self.socket = socket_cliente
        self.running = True

        # Configurar mensaje handler
        self.mensaje_handler = MensajeHandler()
        self.mensaje_handler.mensaje_recibido.connect(self._mostrar_mensaje_recibido)

        # Configurar interfaz
        ip, puerto = self.socket.getpeername()
        self.ui.Chat_ip.setText(f"Chat con {ip}:{puerto}")

        # Conectar eventos
        self.ui.EnviarBoton.clicked.connect(self._handle_enviar)
        self.ui.EnviarTexto.returnPressed = self._handle_enviar

        # Iniciar thread de escucha
        self.thread_recepcion = threading.Thread(target=self._escuchar_mensajes, daemon=True)
        self.thread_recepcion.start()
    def cargar_estilos(self):
        directorio_base = os.path.dirname(__file__)
        ruta_estilos = os.path.join(directorio_base, "..","styles", "styles.qss")
        file = QFile(ruta_estilos)
        if not file.open(QFile.ReadOnly | QFile.Text):
            print(f"Error al abrir el archivo de estilos: {ruta_estilos}")
            return
        stream = QTextStream(file)
        self.setStyleSheet(stream.readAll())
    def _handle_enviar(self):
        mensaje = self.ui.EnviarTexto.toPlainText().strip()
        if not mensaje:
            return

        # Crear thread para envío
        threading.Thread(target=self._enviar_mensaje, args=(mensaje,), daemon=True).start()

        # Actualizar UI inmediatamente
        self._mostrar_mensaje_enviado(mensaje)
        self.ui.EnviarTexto.clear()

    def _enviar_mensaje(self, mensaje):
        try:
            self.socket.send(mensaje.encode('utf-8'))
        except Exception as e:
            print(f"Error al enviar: {e}")
            QMetaObject.invokeMethod(self, "close", Qt.QueuedConnection)

    def _mostrar_mensaje_enviado(self, mensaje):
        widget_mensaje = QWidget()
        ui_mensaje = Ui_SentMessage()
        ui_mensaje.setupUi(widget_mensaje)


        ui_mensaje.messageContent.setText(mensaje)
        ui_mensaje.timeLabel.setText(QDateTime.currentDateTime().toString('hh:mm'))

        item = QListWidgetItem(self.ui.ListaMensajes)
        item.setFlags(item.flags() & ~Qt.ItemIsSelectable)
        item.setSizeHint(widget_mensaje.sizeHint())
        self.ui.ListaMensajes.addItem(item)
        self.ui.ListaMensajes.setItemWidget(item, widget_mensaje)
        self.ui.ListaMensajes.scrollToBottom()

    def _mostrar_mensaje_recibido(self, mensaje):
        widget_mensaje = QWidget()
        ui_mensaje = Ui_ReceivedMessage()
        ui_mensaje.setupUi(widget_mensaje)

        ui_mensaje.messageContent.setText(mensaje)
        ui_mensaje.timeLabel.setText(QDateTime.currentDateTime().toString('hh:mm'))

        item = QListWidgetItem(self.ui.ListaMensajes)
        item.setFlags(item.flags() & ~Qt.ItemIsSelectable)
        item.setSizeHint(widget_mensaje.sizeHint())
        self.ui.ListaMensajes.addItem(item)
        self.ui.ListaMensajes.setItemWidget(item, widget_mensaje)
        self.ui.ListaMensajes.scrollToBottom()

    def _escuchar_mensajes(self):
        while self.running:
            try:
                mensaje = self.socket.recv(1024).decode('utf-8')
                if not mensaje:
                    break
                self.mensaje_handler.mensaje_recibido.emit(mensaje)
            except Exception as e:
                print(f"Error al recibir: {e}")
                break

        QMetaObject.invokeMethod(self, "close", Qt.QueuedConnection)

    def closeEvent(self, event):
        self.running = False
        if self.socket:
            self.socket.close()
        super().closeEvent(event)