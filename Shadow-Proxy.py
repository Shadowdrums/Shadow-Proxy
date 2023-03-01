import socket
import binascii

def start_proxy():
    # Ask for proxy server IP address and port number
    proxy_ip = input("Enter proxy server IP address: ")
    proxy_port = int(input("Enter proxy server port number: "))

    # Set up the proxy server to listen on the specified IP address and port
    proxy_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_server.bind((proxy_ip, proxy_port))
    proxy_server.listen(1)
    print(f'Proxy server listening on {proxy_ip}:{proxy_port}...')

    # Ask for destination IP address and port number
    dest_ip = input("Enter destination IP address: ")
    dest_port = int(input("Enter destination port number: "))

    # Save destination configuration to a hex-encoded .txt file
    dest_config = f"{dest_ip}:{dest_port}"
    with open('dest_config.txt', 'w') as f:
        f.write(binascii.hexlify(dest_config.encode()).decode())

    # Wait for an incoming connection
    client_socket, client_address = proxy_server.accept()
    print(f'Received connection from {client_address}')

    # Forward the connection to the destination server
    dest_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest_socket.connect((dest_ip, dest_port))
    print(f'Connected to destination server {dest_ip}:{dest_port}')

    # Start forwarding data between the client and destination servers
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break

        # Forward data to the destination server
        dest_socket.sendall(data)

        # Receive data from the destination server
        data = dest_socket.recv(1024)
        if not data:
            break

        # Forward data back to the client
        client_socket.sendall(data)

    # Close the sockets
    client_socket.close()
    dest_socket.close()

if __name__ == '__main__':
    start_proxy()
