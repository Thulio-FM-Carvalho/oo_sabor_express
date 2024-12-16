from models.restaurante import Restaurante

restaurante1 = Restaurante('Bifão', 'Almoço')
restaurante1.alternar_estado()
restaurante1.receber_avaliacao('Jonas', 4)
restaurante1.receber_avaliacao('Eduardo', 2)

restaurante2 = Restaurante('Caju', 'Bar e Petiscaria')
restaurante2.alternar_estado()
restaurante2.receber_avaliacao('Jonas', 4)
restaurante2.receber_avaliacao('Eduardo', 2)


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
