import socket
import threading
from logging import shutdown

clients = []
lock = threading.Lock()

def handle_client(client_socket, address):
    global clients
    try:
        with lock:
            clients.append(client_socket)
        print(f"Klient {address} připojen.")
        client_socket.send("Vítejte na serveru!\n".encode())

        buffer = ""
        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            buffer += data.decode()
            while "\n" in buffer:
                command, buffer = buffer.split("\n", 1)
                command = command.strip()

                if command == "count":
                    count = len(clients)
                    client_socket.send(f"Aktuálně připojených klientů: {count}\n".encode())

                elif command.startswith("broadcast "):
                    message = command[len("broadcast "):].strip()
                    broadcast_message = f"[BROADCAST] {message}\n"
                    with lock:
                        for client in clients:
                            if client != client_socket:
                                client.send(broadcast_message.encode())
                elif command == "shutdown":
                    client_socket.send("Zahajujeme hlasování o vypnutí serveru. Zadejte 'yes' nebo 'no'.\n".encode())
                    agree = 0
                    disagree = 0
                    with lock:
                        for client in clients:
                            if client != client_socket:
                                client.send("Hlasujte o vypnutí serveru: 'yes' nebo 'no'\n".encode())
                                respond =  client.recv(1024).decode().strip()
                                if respond == "yes":
                                    agree += 1
                                elif respond == "no":
                                    disagree += 1
                    if agree == len(clients) - 1:
                        client_socket.sendall("Všichni souhlasili. Server se vypíná...\n".encode())
                        shutdown_server()
                    else:
                        client_socket.sendall(
                            f"Vypnutí serveru zamítnuto. Souhlasilo: {agree}, Nesouhlasilo: {disagree}\n".encode())
    except Exception as e:
        print(f"Chyba při komunikaci s klientem {address}: {e}")

    finally:
        with lock:
            clients.remove(client_socket)
        print(f"Klient {address} odpojen.")
        client_socket.close()

def shutdown_server():
    with lock:
        for client in clients:
            client.send("Server se vypíná...\n".encode())
            client.close()
        clients.clear()
    print("Server vypnut.")
    exit(0)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 65532))
    server.listen(5)
    print(f"Server běží na 127.0.0.1:65532")

    try:
        while True:
            client_socket, address = server.accept()
            clients_thread = threading.Thread(target=handle_client, args=(client_socket, address))
            clients_thread.start()
    except KeyboardInterrupt:
        print("Server byl manuálně ukončen.")
        shutdown_server()

if __name__ == "__main__":
    main()


