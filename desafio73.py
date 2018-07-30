"""
    Tuplas com Times de Futebol:

    Crie uma tupla preenchida com os 20 primeiros colocados da Tabela
     do Campeonato Brasileiro de Futebol, na ordem de colocação.
     Depois mostre:

    A) Os 5 primeiros.
    B) Os últimos 4 colocados.
    C) Times em ordem alfabética.
    D) Em que posição está o time da Chapecoense.

"""
times = ( 'Flamengo', 'São Paulo', 'Internacional', 'Cruzeiro', 'Atletico', 'Palmeiras', 'Gremio', 'Corinthians', 'Vasco', 'Sport', 'Fluminense', 'Botafogo', 'Bahia', 'Chapecoense', 'Santos', 'Vitoria', 'America', 'Paraná', 'Atletico-PR', 'Ceará' )
print('-=-'*70)
print(f'Lista de times do brasileirão: {times}')
print('-=-'*70)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=-'*70)
print(f'Os 4 ultimos são: {times[-4:]}')
print('-=-'*70)
print(f'Os times em ordem alfabetica são: {sorted(times)}')
print('-=-'*70)
print(f'O time da chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('-=-'*70)
