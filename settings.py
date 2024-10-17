class Settings:
    def __init__(self):
        self.largura_tela = 1920
        self.altura_tela = 1080
        self.velocidade_nave = 10

        self.velocidade_missel = 20
        self.largura_missel = 8
        self.altura_missel = 20
        self.color_missel = (255, 255, 0)
        self.disparos_por_vez = 500  
        #Configuração do alien
        self.velocidade_alien = 15.0
        self.velocidade_frota = 0
        # direção da fila onde 1 representa direita; -1 representa esquerda.
        self.direcao_frota = 1