import socket
import threading


class ClientHandler:
    def __init__(self, client_socket, address):
        self.client_socket = client_socket
        self.address = address
        self.state = StateKnowNothing(self)

    def handle(self):
        try:
            buffer = ""
            while True:
                data = self.client_socket.recv(1024).decode('utf-8')
                if not data:  # Client disconnected
                    break

                buffer += data
                while "\n" in buffer:
                    message, buffer = buffer.split("\n", 1)
                    message = message.strip()

                    response = self.state.handle_message(message)
                    self.client_socket.send((response + "\n").encode('utf-8'))
        except ConnectionResetError:
            print(f"Client {self.address} disconnected.")
        finally:
            self.client_socket.close()


class State:
    def __init__(self, handler):
        self.handler = handler

    def handle_message(self, message):
        raise NotImplementedError("This method should be implemented by subclasses.")


class StateKnowNothing(State):
    def handle_message(self, message):
        print(f"Received: {message}")
        if message.startswith("R="):
            value = parse_value(message[2:])
            if value is not None:
                self.handler.state = StateKnowR(self.handler, value)
                return "OK"
        elif message.startswith("I="):
            value = parse_value(message[2:])
            if value is not None:
                self.handler.state = StateKnowI(self.handler, value)
                return "OK"
        elif message.startswith("U="):
            value = parse_value(message[2:])
            if value is not None:
                self.handler.state = StateKnowU(self.handler, value)
                return "OK"
        return "Error: Invalid input or missing value.1"

class StateKnowR(State):
    def __init__(self, handler, resistance):
        super().__init__(handler)
        self.resistance = resistance

    def handle_message(self, message):
        if message.startswith("I="):
            value = parse_value(message[2:])
            if value is not None:
                self.handler.state = StateKnowRandU(self.handler, self.resistance, value)
                return "OK"
        elif message.startswith("U="):
            value = parse_value(message[2:])
            if value is not None:
                self.handler.state = StateKnowRandI(self.handler, self.resistance, value)
                return "OK"
        return "Error: Cannot process command in this state."


class StateKnowI(State):
    def __init__(self, handler, current):
        super().__init__(handler)
        self.current = current

    def handle_message(self, message):
        if message.startswith("R="):
            value = parse_value(message[2:])
            if value is not None:
                self.handler.state = StateKnowRandU(self.handler, value, self.current)
                return "OK"
        elif message.startswith("U="):
            value = parse_value(message[2:])
            if value is not None:
                self.handler.state = StateKnowRandR(self.handler, value, self.current)
                return "OK"
        return "Error: Invalid input or missing value."


class StateKnowU(State):
    def __init__(self, handler, voltage):
        super().__init__(handler)
        self.voltage = voltage

    def handle_message(self, message):
        if message.startswith("R="):
            value = parse_value(message[2:])
            if value is not None:
                self.handler.state = StateKnowRandI(self.handler, value, self.voltage)
                return "OK"
        elif message.startswith("I="):
            value = parse_value(message[2:])
            if value is not None:
                self.handler.state = StateKnowRandR(self.handler, self.voltage, value)
                return "OK"
        return "Error: Invalid input or missing value."


class StateKnowRandU(State):
    def __init__(self, handler, resistance, current):
        super().__init__(handler)
        self.resistance = resistance
        self.current = current

    def handle_message(self, message):
        if message == "U=?":
            voltage = self.resistance * self.current
            return f"U={voltage}V"
        return "Error: Invalid input or command."


class StateKnowRandI(State):
    def __init__(self, handler, resistance, voltage):
        super().__init__(handler)
        self.resistance = resistance
        self.voltage = voltage

    def handle_message(self, message):
        if message == "I=?":
            current = self.voltage / self.resistance
            return f"I={current}A"
        return "Error: Invalid input or command."


class StateKnowRandR(State):
    def __init__(self, handler, voltage, current):
        super().__init__(handler)
        self.voltage = voltage
        self.current = current

    def handle_message(self, message):
        if message == "R=?":
            resistance = self.voltage / self.current
            return f"R={resistance}Ω"
        return "Error: Invalid input or command."


def parse_value(value_str):
    try:
        if value_str.endswith("k"):
            return float(value_str[:-1]) * 1000
        elif value_str.endswith("M"):
            return float(value_str[:-1]) * 1000000
        else:
            return float(value_str)
    except ValueError:
        return None


def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Client {address} connected.")
        handler = ClientHandler(client_socket, address)
        threading.Thread(target=handler.handle, daemon=True).start()


if __name__ == "__main__":
    start_server("127.0.0.1", 65532)
