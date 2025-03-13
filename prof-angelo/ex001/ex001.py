class Livro:
    def __init__(self, titulo, autor, ano_de_lancamento, paginas, disponibilidade):
        self.titulo = titulo
        self.autor = autor
        self.ano_de_lancamento = ano_de_lancamento
        self.paginas = paginas
        self.disponibilidade = True
    def emprestar(self):
        if self.disponibilidade:
            self.disponibilidade = False
            print('O livro {self.titulo} não está disponivel para emprestimo')
        else:
            print('Emprestimo realizado com sucesso!')
class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.livros_emprestados = []
    def emprestar_livro(self, livro):
        if livro.disponibilidade == True:
            self.livros_emprestados.append(livro)
            livro.emprestar()
        else:
            print('Livro indisponivel para emprestimo')
    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.disponibilidade = True
            print('Livro devolvido com sucesso!')
        else:
            print('Você não possui este livro emprestado')
    def exibirdetalhes(self):
        for livro in self.livros_emprestados:
            livro.exibirdetalhes()
class Emprestimo:
    def __init__(self, usuario, livro, data_emprestimo, data_devolucao):
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
    def exibir_detalhes_emprestimo(self):
        print('Livro: {self.livro.titulo}, Usuário: {self.usuario.nome} id{self.usuario.cpf}, Data de emprestimo: {self.data_emprestimo}, Data de devolução: {self.data_devolucao}')
        
