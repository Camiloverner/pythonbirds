class Pessoa:

    def comprimentar(self):
        return (f'OLÁ {id(self)}')

if __name__ == '__main__':
    p= Pessoa()
    print(Pessoa.comprimentar(p))
    print(id(p))
    print(p.comprimentar())





