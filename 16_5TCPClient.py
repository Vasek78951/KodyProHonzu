import socket

def start_client(server_host, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((server_host, server_port))
        print("Connected to server. Type 'exit' to disconnect.\n")

        while True:
            message = input("Client> ").strip()
            if not message:
                print("Empty input. Please type a message.")
                continue
            if message.lower() == "exit":
                print("Disconnecting from server.")
                break

            print(f"Sending: {message}")  # Debugging: show the message sent
            client_socket.sendall((message + "\n").encode('utf-8'))
            response = client_socket.recv(1024).decode('utf-8')
            print(f"SERVER> {response}")  # Debugging: show the server's response



# Run the TCP client
if __name__ == "__main__":
    start_client("127.0.0.1", 65532)
