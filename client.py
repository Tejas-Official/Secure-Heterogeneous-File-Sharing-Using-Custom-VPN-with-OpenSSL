
import socket
import ssl

def send_file_to_server(file_path, host, port):
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations(r"C:\Users\Asus\Desktop\project-directory\certs\server.crt")
    
    # Bypass SSL verification
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print(f"Connected to {host}:{port}")
            with open(file_path, "rb") as file:
                data = file.read()
                ssock.sendall(data)
            print(f"Sent {len(data)} bytes")

send_file_to_server("", 'localhost', 65432)
