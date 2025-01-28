import socket

server_inet_address = ("127.0.0.1", 65532)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    # Bindování na zadanou adresu a port
    server_socket.bind(server_inet_address)
    server_socket.listen()
    print(f"Server start on {server_inet_address[0]}:{server_inet_address[1]}")

    while True:
        print("Waiting for a connection...")
        try:
            # Přijetí spojení
            connection, client_inet_address = server_socket.accept()
            print(f"Client connected from {client_inet_address[0]}:{client_inet_address[1]}")

            # Příprava zprávy
            message = "HELLO\n"
            message_as_bytes = bytes(message, "utf-8")

            # Odeslání zprávy klientovi
            connection.send(message_as_bytes)
            print("Message sent to the client.")

        finally:
            # Uzavření spojení s klientem
            connection.close()
            print("Client connection closed.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Uzavření serverového socketu
    server_socket.close()
    print("Server is closed.")