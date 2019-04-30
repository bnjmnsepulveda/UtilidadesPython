"""
ejecutar comando en python 3
"""
import shlex, subprocess
command_line = 'sudo apt-get install python3 -y'
args = shlex.split(command_line)
salida = subprocess.call(args)
print(salida)
