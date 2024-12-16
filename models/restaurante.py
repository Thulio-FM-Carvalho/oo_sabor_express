from models.avaliacao import Avaliacao


class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        """
        Essa função é um construtor da classe que é chamado automaticamente assim que a classe é instanciada. Assim
        que a classe é instanciada, é definido as propriedades: _nome, _categoria, _ativo e _avaliacao.

        Inputs:
            - nome: nome do restaurante
            - categoria: categoria do restaurante
        """

        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """
        Função que retorna a representação do objeto "amigável" em forma de string. No momento em que é feito o print()
        do da instância do objeto, a função __str__ é chamada automaticamente.

        Outputs:
            - nome: Nome do restaurante
            - categoria: Categoria do restaurante
        """

        return f'{self._nome} | {self._categoria}'

    @property
    def ativo(self):
        """
        @property torna essa função um "getter". No entanto, essa é uma maneira de acessar um atributo privado sem
        precisar acessá-lo diretamente.

        Função que retorna o status do restaurante (ativo ou não ativo). Essa função é chamada automaticamente quando
        o atributo ativo é acessado, ex: restaurante.ativo
        Outputs:
            - _ativo: Status do restaurante (ativo ou não ativo)
        """

        return '✅' if self._ativo else '❌'

    @classmethod
    def listar_restaurantes(cls):
        """
        @classmethod indica que podemos acessar a função sem instanciar a classe. Podemos acessar a função colocando o
        nome da classe primeiro, ex: Restaurante.listar_restaurantes()

        Função responsável por listar os restaurantes e imprimir no terminal
        Outputs:
            - _nome: Nome do restaurante
            - _categoria: Categoria do restaurante
            - media_avaliacoes: Média de avaliação do restaurante
            - ativo: Status do restaurante(ativo ou não ativo)
        """

        print(f'{'Nome do restaurante'.ljust(25)} | {'Categora'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'} ')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    def alternar_estado(self):
        """Função responsável por alterar o status do restaurante (ativo ou não ativo)"""

        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Inputs:
            - cliente: Nome do cliente que fez a avaliação
            - nota: Nota que o cliente deu na avaliação
        Outputs:
            - avaliacao: Instancia da avaliação na lista _avaliacao da classe
        """

        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """
        @property torna essa função um "getter". No entanto, essa é uma maneira de acessar um atributo privado sem
        precisar acessá-lo diretamente.
        Função responsável por retornar uma média das avaliações de cada restaurante
        Outputs:
            - media: valor exato da média da avaliação de cada restaurante
        """

        if not self._avaliacao:
            return '-'

        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media