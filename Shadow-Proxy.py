import socket
import os

def start_proxy(proxy_host, proxy_port, dest_host, dest_port):
    # Set up the proxy server to listen on the specified port
    proxy_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_server.bind((proxy_host, proxy_port))
    proxy_server.listen(1)
    print(f'Proxy server listening on {proxy_host}:{proxy_port}...')

    # Wait for an incoming connection
    client_socket, client_address = proxy_server.accept()
    print(f'Received connection from {client_address}')

    # Forward the connection to the destination server
    dest_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest_socket.connect((dest_host, dest_port))
    print(f'Connected to destination server {dest_host}:{dest_port}')

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
    # Ask for the proxy server and destination server details
    proxy_host = input("Enter the proxy server's IP address: ")
    proxy_port = int(input("Enter the proxy server's port: "))
    dest_host = input("Enter the destination server's IP address: ")
    dest_port = int(input("Enter the destination server's port: "))

    # Save the destination configuration to a hex-encoded file
    with open('destination_config.txt', 'w') as f:
        f.write(dest_host + '\n')
        f.write(str(dest_port) + '\n')
    print(f'Destination configuration saved to {os.getcwd()}/destination_config.txt')

    # Start the proxy server
    start_proxy(proxy_host, proxy_port, dest_host, dest_port)
