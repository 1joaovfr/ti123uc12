import pickle

class Pessoa:

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def __str__(self):
        return f"Pessoa(nome='{self.nome}',sobrenome='{self.sobrenome}')"

p = Pessoa("Rodrigo","Santos")
print(p)

file = open("pessoa.pkl", "wb")
pickle.dump(p, file)
file.close()

del p

with open("pessoa.pkl", "rb") as file:
    p = pickle.load(file)
    print(p)
