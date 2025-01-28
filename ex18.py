brasileirao = ('Palmeiras', 'Gremio', 'Atlético-MG','Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional',
               'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')

print(70 * '=')

print(f"Os 5 primeiro colocados são: {brasileirao[:5]}")
print(f"Os 4 últimos colocados são: {brasileirao[16:]}")
print(f"Times em ordem alfabética: {sorted(brasileirao)}")
print(f'São Paulo está na posição {brasileirao.index("São Paulo")+1}')