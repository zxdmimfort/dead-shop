import socket
from .base import *


DEBUG = True

# hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
# INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1"]
