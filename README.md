# Shadow-Proxy
Reverse Proxy, Author will not be help liable for miss use with this source code. Have pre documented approval befor using on a device that you do not own

The code is a Python script that sets up a proxy server on the local device, listens for incoming connections from a client on a specific port, and forwards the connection to a destination server specified by the user.

When the script is run, it prompts the user for the IP address and port number of the proxy server to be used. It then prompts the user for the IP address and port number of the destination server where the client connection will be forwarded.

After the user inputs the necessary information, the script creates a text file named "destination_config.txt" in the current directory and encodes the destination IP and port information in hexadecimal format, writing it to the file. This file is used to store the destination configuration so that the script can retrieve it later for subsequent connections without the need to re-enter the information.

The script then sets up the proxy server to listen on the specified port and waits for an incoming connection from a client. When a connection is received, it establishes a connection to the destination server using the IP and port information provided by the user.

The script then creates two threads to handle the incoming client connection and the outgoing connection to the destination server, respectively. The thread for the client connection receives data from the client, sends it to the destination server, and then waits for a response. The thread for the destination server connection receives data from the destination server, sends it back to the client, and then waits for another request.

In the event that a reverse shell connection is made to the proxy server, the script would still forward the connection to the destination server. However, it is worth noting that this could potentially lead to security issues if not properly configured.

Overall, the script is designed to allow for easy forwarding of incoming client connections to a specified destination server using a proxy server.
