import random
import numpy as np
import faker

fake = faker.Faker()

nota01 = list(np.random.normal(loc=5, scale=1, size = 30))
faltas01 = list(np.random.normal(loc=5, scale=1, size = 30))
nota02 = list(np.random.normal(loc=5, scale=1, size = 30))
faltas02 = list(np.random.normal(loc=5, scale=1, size = 30))
nota03 = list(np.random.normal(loc=5, scale=1, size = 30))
faltas03 = list(np.random.normal(loc=5, scale=1, size = 30))
nota04 = list(np.random.normal(loc=5, scale=1, size = 30))
faltas04 = list(np.random.normal(loc=5, scale=1, size = 30))
nota05 = list(np.random.normal(loc=5, scale=1, size = 30))
faltas05 = list(np.random.normal(loc=5, scale=1, size = 30))
nota06 = list(np.random.normal(loc=5, scale=1, size = 30))
faltas06 = list(np.random.normal(loc=5, scale=1, size = 30))
nota07 = list(np.random.normal(loc=5, scale=1, size = 30))
faltas07 = list(np.random.normal(loc=5, scale=1, size = 30))
nota08 = list(np.random.normal(loc=5, scale=1, size = 30))
faltas08 = list(np.random.normal(loc=5, scale=1, size = 30))
nota09 = list(np.random.normal(loc=5, scale=1, size = 30))
faltas09 = list(np.random.normal(loc=5, scale=1, size = 30))
nota10 = list(np.random.normal(loc=5, scale=1, size = 30))
faltas10 = list(np.random.normal(loc=5, scale=1, size = 30))
nomes = [fake.name() for i in range(30)]

notas = input()

with open(notas,'w') as f:
    f.write('Nome,disciplina01.disciplina02,disciplina03,disciplina04,disciplina05,disciplina06,disciplina07,disciplina08,disciplina09,disciplina10,')
    for i in range(30):
        f.write(nomes[i]+','+
            str(nota01[i])+','+
            str(nota02[i])+','+
            str(nota03[i])+','+
            str(nota04[i])+','+
            str(nota05[i])+','+
            str(nota06[i])+','+
            str(nota07[i])+','+
            str(nota08[i])+','+
            str(nota09[i])+','+
            str(nota10[i])+'\n')
