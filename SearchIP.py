import socket
import getpass  

user = getpass.getuser()
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("+---------------------------------------------------+")
print("| - Tu nombre de Usuario es: " + user )
print("| - Tu direción IP es: " + ip)
print("| - El nombre de tu Ordenador es: " + hostname )
print("+---------------------------------------------------+")
