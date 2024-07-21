import socket

def send_file(ip, port, file_path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))

    with open(file_path, 'rb') as file:
        data = file.read(1024)
        while data:
            client_socket.send(data)
            data = file.read(1024)

    print("File sent successfully!")
    client_socket.close()

def receive_file(port, file_path):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)

    print(f"Waiting for a connection on port {port}...")

    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    with open(file_path, 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)

    print("File received successfully!")
    client_socket.close()
    server_socket.close()

# Example usage for sending
# send_file('receiver_ip_address', 12345, 'file_to_send.txt')

if __name__ == '__main__':
    while True:
        try:
            receive_file(3389, 'images/init_images/source_image.jpg')
        except Exception as e:
            print(e)
            continue

        try:
            send_file('81.205.194.201', 56789, 'outputs/img2img-samples/samples/mirror.png')
        except Exception as e:
            print(e)
