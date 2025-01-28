def notas(*n, sit=False):
    dic = {}
    dic['Total'] = len(n)
    dic['Maior'] = max(n)
    dic['Menor'] = min(n)
    dic['Media'] = sum(n) / len(n)
    if sit:
        if dic['Media'] < 5:
            dic["Situação"] = 'Ruim'
        else:
            dic["Situação"] = 'Boa'
    return dic

resp = notas(4, 1, 2, 3)
print(resp)