import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 8080))
server.listen(1)

print("Servidor ouvindo na porta 8080...")

client_socket, client_address = server.accept()
print(f"Conexão recebida de {client_address}")

client_socket.send(b"Hello from server!")

client_socket.close()

server.close()
