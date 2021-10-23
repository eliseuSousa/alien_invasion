import pygame.font

class Button():
    def __init__(self, ai_setings, screen, msg):
        """Inicializa os atributos do botão."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Define as dimensões e as propriedades do botaõ
        self.width, self.height = 200, 50
        self.button_color = (255,87,34)
        self.text_color = (245, 245, 245)
        self.font = pygame.font.SysFont(None, 48)

        # Contrói o objeto rect do botão e o centeliza 
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # As mensagens do botão deve ser preparada apenas uma vez
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Transforma msg em imagem redenrzada e centraliza o texto no botão."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Desenha o botão em branco e, em seguida, desenha a mensagem
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)