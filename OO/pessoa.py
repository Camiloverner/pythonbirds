class Pessoa:
    def __init__(self):
        self.nome = None

    def comprimentar(self):
        return (f'OLÁ {id(self)}')

if __name__ == '__main__':
    p= Pessoa()
    print(Pessoa.comprimentar(p))
    print(id(p))
    print(p.comprimentar())
    print(p.nome)
    p.nome= 'Camilo'
    print(p.nome)




