class FilmeNovo:
    def __init__(self, titulo: str, diretor: str, ano: int, duracao_min: int):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano
        self.duracao_min = duracao_min
        self.assistido = False
    def __str__(self):
        return f"""Filme: {self.titulo}\nDiretor: {self.diretor}\nEstreou em {self.ano}, com {self.duracao_min} minutos"""
    def marcar_assistido(self):
        self.assistido = True
        
filme = FilmeNovo("Cidade de Deus", "José Padilla", "2002", "200" )       

print(filme) 