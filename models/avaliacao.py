class Avaliacao:
    def __init__(self,  cliente, nota):
        """
        Essa função é um construtor da classe que é chamado automaticamente assim que a classe é instanciada. Assim
        que a classe é instanciada, é definido as propriedades: cliente, nota.
        Inputs:
            - cliente: Nome do cliente
            - nota: Nota do cliente
        """

        self._cliente = cliente
        self._nota = nota
