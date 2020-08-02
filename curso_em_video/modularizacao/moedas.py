def dividir(n,format=False):
    return n/2 if format is False else moedas(n/2)

def dobrar(n,format=False):
    return n*2 if format is False else moedas(n*2)

def aumentar(n, x, format=False):
    return n + (n/x) if format is False else moedas(n + (n/x))

def reduzir(n, x ,format=False):
    return n - (n/x) if format is False else moedas(n - (n/x))

def moedas(n=0, moeda="R$"):
    return f'{moeda}{n:>.2f}'.replace('.',',')