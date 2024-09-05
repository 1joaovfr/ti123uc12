import pickle

class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    def __str__(self):
        return f"Pessoa(nome='{self.nome}')"

p = Pessoa("Rodrigo")
print(p)

file = open("pessoa.pkl", "wb")
pickle.dump(p, file)
file.close()

del p

with open("pessoa.pkl", "rb") as file:
    p = pickle.load(file)
    print(p)
