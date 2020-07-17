import urllib
import urllib.request
import os
github= "https://github.com/ViniciusBacelar"
try:
    site = urllib.request.urlopen(f'{github}')
except urllib.error.URLError:
    print(f'O site nao esta acessivel')
else:
    print("Consegui acessar o site com sucesso")
    os.system(f'python3 -m webbrowser -t {github}')