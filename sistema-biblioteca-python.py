class Livro:
  def __init__(self, titulo, autor, ano):
    self.titulo = titulo
    self.autor = autor
    self.ano = ano

class Biblioteca:
  def __init__(self):
    self.livros = []

  def adicionar_livro(self, livro):
    self.livros.append(livro)

  def listar_livros(self):
    print("Livros disponíveis:")
    for livro in self.livros:
      print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano}")

  def buscar_livro_por_titulo(self, titulo_buscado):
    for livro in self.livros:
      if livro.titulo.lower() == titulo_buscado.lower(): # Busca case-insensitive
        return livro
    return None

# Criando os Livros
livro1 = Livro("Quarto do despejo" , "Carolina Maria de Jesus" , 1986)
livro2 = Livro("O Pequeno Príncipe" , "Antoine de Saint-Exupéry" , 1943)
livro3 = Livro("Dom Casmurro" , "Machado de Assis" , 1899)
livro4 = Livro("A Menina que Roubava Livros" , "Markus Zusak" , 2005)
livro5 = Livro("Harry Potter e a Pedra Filosofal" , "J.K.Rowling" , 1997)

# Adicionar livros à biblioteca
biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)

biblioteca.adicionar_livro(livro2)

biblioteca.adicionar_livro(livro3)

biblioteca.adicionar_livro(livro4)

biblioteca.adicionar_livro(livro5)

# Mensagem de boas vindas

print("Olá meu nome é Lucas, eu sou bibliotecario hoje.")

# Mostrar livros disponiveis

biblioteca.listar_livros()

# O código foi modificado para permitir que o usuário digite o título do livro
escolha_usuario = input("Essas são as nossas opções, qual você quer? Digite o título do livro: ")

livro_selecionado = biblioteca.buscar_livro_por_titulo(escolha_usuario)

if livro_selecionado:
    print(f"Você escolheu: {livro_selecionado.titulo} de {livro_selecionado.autor}")
    print("Aqui está. Foi uma excelente escolha!")
else:
    print(f"Desculpe, o livro '{escolha_usuario}' não foi encontrado na nossa biblioteca. Por favor, verifique a ortografia e tente novamente.")
