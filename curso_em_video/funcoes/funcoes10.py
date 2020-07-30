"""
    Desafio 105
    Programa para ler notas e devolver a média do aluno
    com preferência de expor sua situação ou não.
"""
def notas(*n, sit=False):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Media'] = sum(n)/len(n)
    if sit:
        if r['Media'] >= 7:
            r['Situação'] = 'Boa'
        elif r['Media'] >= 5:
            r['Situação'] = 'Razoável'
        else:
            r['Situação'] = 'Ruim'
    return r

resp = notas(10,10,10,sit= True)
print(resp)