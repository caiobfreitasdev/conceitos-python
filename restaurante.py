

class Restaurantes:
    nome = ""
    categoria = ""
    ativo = False
    
restaurante_praca = Restaurantes()
restaurante_praca.nome = "praça"
restaurante_praca.categoria = "Gourmet"
restaurante_pizza = Restaurantes()

lista_restaurantes = [
    restaurante_pizza,
    restaurante_praca
]

print(vars(restaurante_praca))