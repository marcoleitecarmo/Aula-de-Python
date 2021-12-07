import subprocess

# Windows - ping 127.0.0.1

# Linux - ping 172.0.0.1 -c 4


proc = subprocess.run(
    ['ping', '127.0.01', '-c', '4'],
    capture_output=True,
    text=True
)

saida = proc.stdout
saida = saida.replace('icmp_seq', 'MC')
print(saida)

