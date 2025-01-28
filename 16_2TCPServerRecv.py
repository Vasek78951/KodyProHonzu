import socket
import datetime
import random

def handle_quote(client_socket):
    quotes = [
        "Život je jako jízda na kole. Abys udržel rovnováhu, musíš se pohybovat. – Albert Einstein",
        "Štěstí není něco, co dostanete hotové. Je to něco, co vzniká z vašich vlastních činů. – Dalajláma",
        "Úspěch není konečný, neúspěch není fatální: to, co se počítá, je odvaha pokračovat. – Winston Churchill",
        "Buď změnou, kterou chceš vidět ve světě. – Mahátma Gándhí",
        "Jediný způsob, jak dělat skvělou práci, je milovat to, co děláš. – Steve Jobs"
    ]
    message = random.choice(quotes)
    client_socket.sendall((message + "\n").encode())

def handle_date(client_socket):
    current_date = datetime.datetime.now()
    client_socket.sendall(f"Aktuální datum a čas: {current_date}\n".encode())

def handle_help(client_socket):
    commands = """
Dostupné příkazy:
1. quote - Vrátí náhodný citát.
2. date - Vrátí aktuální datum a čas.
3. help - Vypíše všechny dostupné příkazy.
4. exit - Odpojí klienta.
5. shutdown-server - Vypne server.
    """
    client_socket.sendall((commands + "\n").encode())

def handle_exit(client_socket):
    client_socket.sendall("Odpojuji vás...\n".encode())
    client_socket.close()

def handle_shutdown(client_socket, server_socket):
    client_socket.sendall("Server se vypíná...\n".encode())
    client_socket.close()
    server_socket.close()
    print("Server vypnut.")
    exit(0)

def handle_unknown(client_socket):
    client_socket.sendall("Neznámý příkaz. Zadejte 'help' pro seznam dostupných příkazů.\n".encode())

COMMANDS = {
    "quote": handle_quote,
    "date": handle_date,
    "help": handle_help,
    "exit": handle_exit,
    "shutdown-server": handle_shutdown
}

def handle_client(client_socket, server_socket):
    buffer = ""
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break  # Client disconnected

            buffer += data  # Append received data to the buffer
            while "\n" in buffer:  # Process full commands
                command, buffer = buffer.split("\n", 1)  # Split on the first newline
                command = command.strip()  # Clean up the command
                if not command:
                    continue  # Skip empty commands

                print(f"Přijatý příkaz: {command}")

                handler = COMMANDS.get(command, handle_unknown)
                if handler == handle_shutdown:
                    handler(client_socket, server_socket)  # Special case for shutting down the server
                elif handler == handle_exit:
                    handler(client_socket)
                    return  # Exit the loop after disconnecting the client
                else:
                    handler(client_socket)

        except Exception as e:
            print(f"Chyba: {e}")
            break

def run_server(host="127.0.0.1", port=65532):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server běží na {host}:{port}")

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Klient {client_address} připojen.")
            client_socket.sendall("Vítejte na serqveru! Zadejte příkaz nebo 'help' pro nápovědu.\n".encode())
            handle_client(client_socket, server_socket)
        except KeyboardInterrupt:
            print("\nServer manuálně ukončen.")
            server_socket.close()
            break

if __name__ == "__main__":
    run_server()
