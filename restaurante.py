class Restaurantes:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    
    def __str__(self):
        return f"{self.nome} | {self.categoria}"
    
restaurante_praca = Restaurantes("praça", "gourmet")
restaurante_pizza = Restaurantes("pizza", "italiano")

lista_restaurantes = [
    restaurante_pizza,
    restaurante_praca
]

print(restaurante_praca)
print(restaurante_pizza)


    