import socket
import threading
from PySide6.QtCore import Signal, QObject


class PeticionHandler(QObject):
    nueva_peticion = Signal(object, str, int)  # Socket, IP, Puerto
    solicitud_enviada = Signal(bool, str)  # Éxito/Fallo, Mensaje
    solicitud_procesada = Signal(object)  # QListWidgetItem a remover

    def __init__(self, ventana_principal):
        super().__init__()
        self.ventana_principal = ventana_principal
        self.socket_servidor = None
        self.escuchando = False

    def empezar_escuchar_dinamico(self, puerto_inicial):
        if self.socket_servidor:
            self.escuchando = False
            self.socket_servidor.close()

        for puerto in range(puerto_inicial, 65536):
            try:
                self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                self.socket_servidor.bind(('', puerto))
                self.socket_servidor.listen(5)
                self.escuchando = True
                threading.Thread(target=self._escuchar_conexiones, daemon=True).start()
                return puerto
            except OSError:
                if self.socket_servidor:
                    self.socket_servidor.close()
                continue
        return None

    def _escuchar_conexiones(self):
        try:
            while self.escuchando:
                try:
                    self.socket_servidor.settimeout(1.0)
                    socket_cliente, direccion = self.socket_servidor.accept()
                    threading.Thread(target=self._manejar_cliente,
                                     args=(socket_cliente, direccion),
                                     daemon=True).start()
                except socket.timeout:
                    continue
                except Exception as e:
                    if self.escuchando:
                        print(f"Error en accept: {e}")
        finally:
            if self.socket_servidor:
                self.socket_servidor.close()

    def _manejar_cliente(self, socket_cliente, direccion):
        try:
            ip, puerto = direccion
            self.nueva_peticion.emit(socket_cliente, ip, puerto)
        except Exception as e:
            print(f"Error al manejar cliente: {e}")
            if socket_cliente:
                socket_cliente.close()

    def _enviar_respuesta(self, socket_cliente, respuesta):
        try:
            socket_cliente.send(respuesta.encode('utf-8'))
        except Exception as e:
            print(f"Error al enviar respuesta: {e}")

    def aceptar_conexion(self, socket_cliente):
        self._enviar_respuesta(socket_cliente, "ACCEPTED")
        return True

    def rechazar_conexion(self, socket_cliente):
        self._enviar_respuesta(socket_cliente, "REJECTED")
        socket_cliente.close()
        return False

    def enviar_solicitud_conexion(self, ip, puerto):
        cliente_socket = None
        try:
            cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente_socket.settimeout(100)
            cliente_socket.connect((ip, puerto))

            # Esperar respuesta
            respuesta = cliente_socket.recv(1024).decode('utf-8')

            if respuesta == "ACCEPTED":
                self.solicitud_enviada.emit(True, f"Solicitud aceptada por {ip}:{puerto}")
                return True, cliente_socket
            elif respuesta == "REJECTED":
                self.solicitud_enviada.emit(False, f"Solicitud rechazada por {ip}:{puerto}")
                return False, None
            else:
                self.solicitud_enviada.emit(False, f"Respuesta inválida del servidor: {respuesta}")
                return False, None

        except ConnectionRefusedError:
            self.solicitud_enviada.emit(False, f"Conexión rechazada por {ip}:{puerto}")
            return False, None
        except socket.timeout:
            self.solicitud_enviada.emit(False, f"Tiempo de espera agotado al conectar con {ip}:{puerto}")
            return False, None
        except Exception as e:
            self.solicitud_enviada.emit(False, f"Error al enviar solicitud: {str(e)}")
            return False, None
        finally:
            if cliente_socket and not respuesta == "ACCEPTED":
                cliente_socket.close()

    def detener(self):
        self.escuchando = False
        if self.socket_servidor:
            self.socket_servidor.close()
            self.socket_servidor = None