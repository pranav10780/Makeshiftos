import subprocess 
from . import helper,echo

binaries = subprocess.run('ls -a /data/data/com.termux/files/home/makeshiftterminal/config/',shell=True,stdout=subprocess.PIPE , text=True)
output = binaries.stdout.split()

output.remove('.')
output.remove('..')
output.remove('handler.py')

def recievedata(data):
    data = data.split(' ')
    if data[0] == 'help':
        helper.default()
    elif data[0] == 'exit' or data == 'quit':
        exit()
    elif data[0] == 'echo':
        echo.startecho(data)
    elif data[0] == 'ls' or data[0] == 'dir':
        directories.show()
    else:
        print(f'The command: {data} was not found')
