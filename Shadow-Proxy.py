import socket
import time

def start_proxy():
    # Get proxy server IP and port from user
    proxy_host = input('Enter proxy server IP address: ')
    proxy_port = int(input('Enter proxy server port: '))

    # Set up the proxy server to listen on the specified port
    proxy_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_server.bind((proxy_host, proxy_port))
    proxy_server.listen(1)
    print(f'Proxy server listening on {proxy_host}:{proxy_port}...')

    # Get destination server IP and port from user
    dest_host = input('Enter destination server IP address: ')
    dest_port = int(input('Enter destination server port: '))
    dest_config = f'{dest_host}:{dest_port}'.encode().hex()

    # Save destination server configuration to a file
    with open('dest_config.txt', 'w') as f:
        f.write(dest_config)
    print(f'Destination configuration saved to dest_config.txt')

    while True:
        try:
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
        except:
            print(f'Destination server {dest_host}:{dest_port} is down, retrying in 5 seconds...')
            time.sleep(5)

if __name__ == '__main__':
    start_proxy()
