from numpy.random import normal
import faker

fake = faker.Faker('pt_BR')
nomes = [fake.name() for _ in range(90)]

for i in range(3):
    notas = normal(loc=5, scale=1, size = [10,90]).transpose()
    faltas = normal(loc=5, scale=1, size = [10,90])

    notas_str = [','.join([f"{notas[i][j]:.2f}" for j in range(10)]) for i in range(90)]
    
    header = ','.join(["Nome"] + [f"disc{i:02}" for i in range(1,11)])

    arquivo_notas = f"notas{i}.csv"

    with open(arquivo_notas,'w') as f:
        f.write(header+'\n')
        for i in range(90):
            f.write(nomes[i]+','+notas_str[i]+'\n')
        

    arquivo_faltas = f"faltas{i}.csv"

    with open(arquivo_faltas,'w') as f:
        f.write(header+'\n')
