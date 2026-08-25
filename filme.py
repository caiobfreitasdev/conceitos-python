class FilmeNovo:
    def __init__(self, titulo: str, diretor: str, ano: int, duracao_min: int):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano
        self.duracao_min = duracao_min
        self.assistido = False

    def marcar_assistido(self):
        self.assistido = True
    def converter_minuto_em_hora(self):
        horas, minutos = divmod(self.duracao_min, 60)
        return f"{horas}h{minutos}"
        
    def __str__(self):
        if self.marcar_assistido:
            marcar = "[X]"
        else:
            marcar = "[ ]"
        return f"{marcar} Filme: {self.titulo}\nDiretor: {self.diretor}\nEstreou em {self.ano}, com {self.converter_minuto_em_hora()}"

filme = FilmeNovo("Cidade de Deus", "José Padilla", 2002, 200 )       



print(filme) 
filme.marcar_assistido()
print(filme) 

