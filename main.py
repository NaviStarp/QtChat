import os
import sys
import threading
import socket
import toml
from pathlib import Path
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QListWidgetItem
from PySide6.QtCore import QFile, QTextStream, Signal, QObject
from ui.PaginaPrincipal import Ui_MainWindow
from ui.PeticionEntrante import Ui_IncomingRequest
from widgets.chats_recientes import load_recent_chats
from widgets.peticionHandler import PeticionHandler

CONFIG_FILE = "config.toml"
DEFAULT_PORT = 12345


class MainWindow(QMainWindow):
    respuesta_recibida = Signal(str, str)  # Señal para manejar respuestas de conexión

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Inicializar tema y componentes
        self.cargar_estilos()
        self.request_handler = PeticionHandler(self.ui)
        self.request_handler.nueva_peticion.connect(self.agregar_solicitud_a_lista)
        self.request_handler.solicitud_enviada.connect(self._mostrar_estado_solicitud)
        self.request_handler.solicitud_procesada.connect(self._remover_solicitud)

        # Conectar señales con slots
        self.respuesta_recibida.connect(self._manejar_respuesta)

        # Cargar configuración inicial
        self.config = self.cargar_configuracion()
        puerto_configurado = self.config.get("puerto", DEFAULT_PORT)
        self.ui.PuertoPersonalizado.setText(str(puerto_configurado))

        # Iniciar el servidor automáticamente al abrir la aplicación
        self.iniciar_servidor(puerto_configurado)

        # Conectar botones a funciones
        self.ui.pushButton.clicked.connect(self.abrir_ajustes)
        self.ui.VolverDeAjustes.clicked.connect(self.volver_principal)
        self.ui.pushButton_2.clicked.connect(self.enviar_solicitud_conexion)

        # Cargar chats recientes
        load_recent_chats(self.ui.listWidget_2)

    def iniciar_servidor(self, puerto_inicial):
        """Inicia el servidor automáticamente al abrir la aplicación."""
        puerto_real = self.request_handler.empezar_escuchar_dinamico(puerto_inicial)
        if puerto_real:
            self.ui.PuertoPersonalizado.setText(str(puerto_real))
            self.config["puerto"] = puerto_real
            self.guardar_configuracion()
        else:
            QMessageBox.warning(self, "Error", "No se pudo iniciar el servidor en ningún puerto disponible.")

    def enviar_solicitud_conexion(self):
        """Manejar el botón de enviar solicitud de conexión."""
        ip_destino = self.ui.IPEdit.toPlainText().strip()
        puerto_destino = self.ui.PuertoEdit.toPlainText().strip()

        # Validaciones básicas
        if not ip_destino or not puerto_destino:
            QMessageBox.warning(self, "Error", "Por favor ingrese IP y puerto")
            return

        try:
            puerto_destino = int(puerto_destino)
            if puerto_destino < 1024 or puerto_destino > 65535:
                QMessageBox.warning(self, "Error", "El puerto debe estar entre 1024 y 65535")
                return

            # Cambiar el estado del botón
            self.ui.pushButton_2.setText("Esperando...")
            self.ui.pushButton_2.setEnabled(False)

            # Enviar solicitud de conexión
            success, socket = self.request_handler.enviar_solicitud_conexion(ip_destino, puerto_destino)
            if success:
                self._conectar_chat(socket)
            else:
                self._cancelar_solicitud()

        except ValueError:
            QMessageBox.warning(self, "Error", "Puerto inválido.")

    def _aceptar_solicitud(self, socket, item):
        """Maneja la aceptación de una solicitud"""
        if self.request_handler.aceptar_conexion(socket):
            self._conectar_chat(socket)
        self._remover_solicitud(item)

    def _rechazar_solicitud(self, socket, item):
        """Maneja el rechazo de una solicitud"""
        self.request_handler.rechazar_conexion(socket)
        self._remover_solicitud(item)

    def _manejar_respuesta(self, respuesta, Clientesocket):
        """Procesar la respuesta en el hilo principal."""
        if respuesta == "aceptada":
            self._conectar_chat(Clientesocket)
        elif respuesta == "rechazada":
            self._cancelar_solicitud()

    def _conectar_chat(self, Clientesocket:socket.socket):
        QMessageBox.information(self,"Conexion establecida!",f"{Clientesocket.getsockname()[0]}:{Clientesocket.getsockname()[1]}")
        self.ui.pushButton_2.setText("Conectar")
        self.ui.pushButton_2.setEnabled(True)

    def _cancelar_solicitud(self):
        QMessageBox.warning(self, "Conexión rechazada", "El usuario rechazó la conexión.")
        self.ui.pushButton_2.setText("Conectar")
        self.ui.pushButton_2.setEnabled(True)

    def cargar_estilos(self):
        directorio_base = os.path.dirname(__file__)
        ruta_estilos = os.path.join(directorio_base, "styles", "styles.qss")
        file = QFile(ruta_estilos)
        if not file.open(QFile.ReadOnly | QFile.Text):
            print(f"Error al abrir el archivo de estilos: {ruta_estilos}")
            return
        stream = QTextStream(file)
        self.setStyleSheet(stream.readAll())

    def cargar_configuracion(self):
        if not os.path.exists(CONFIG_FILE):
            return {}
        with open(CONFIG_FILE, "r") as f:
            return toml.load(f)

    def guardar_configuracion(self):
        with open(CONFIG_FILE, "w") as f:
            toml.dump(self.config, f)

    def abrir_ajustes(self):
        self.ui.FramePrincipal.setCurrentIndex(1)

    def volver_principal(self):
        self.ui.FramePrincipal.setCurrentIndex(0)

    def _mostrar_estado_solicitud(self, exito, mensaje):
        """Muestra el estado de la solicitud enviada"""
        if exito:
            QMessageBox.information(self, "Solicitud Enviada", mensaje)
        else:
            QMessageBox.warning(self, "Error", mensaje)
        self.ui.pushButton_2.setText("Conectar")
        self.ui.pushButton_2.setEnabled(True)

    def _remover_solicitud(self, item):
        """Elimina una solicitud de la lista"""
        self.ui.listWidget.takeItem(self.ui.listWidget.row(item))

    def agregar_solicitud_a_lista(self, socket, ip, puerto):
        try:
            widget_solicitud = QWidget()
            ui = Ui_IncomingRequest()
            ui.setupUi(widget_solicitud)

            ui.ipLabel.setText(f"IP: {ip}:{puerto}")

            item_lista = QListWidgetItem(self.ui.listWidget)
            item_lista.setSizeHint(widget_solicitud.sizeHint())

            # Modificar los handlers para que remuevan el item
            ui.acceptButton.clicked.connect(lambda: self._aceptar_solicitud(socket, item_lista))
            ui.rejectButton.clicked.connect(lambda: self._rechazar_solicitud(socket, item_lista))

            self.ui.listWidget.addItem(item_lista)
            self.ui.listWidget.setItemWidget(item_lista, widget_solicitud)

        except Exception as e:
            print(f"Error al agregar solicitud a la lista: {e}")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())