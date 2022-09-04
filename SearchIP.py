import socket
import getpass  

user = getpass.getuser()
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)


print("El nombre de tu ordenador es: " + hostname)
print("tu direción IP es: " + ip)
print("tu nombre de usuario es: " + user)
