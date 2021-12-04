import pygame, sys, random
from pygame.locals import *
from pygame.math import Vector2

class VIVORA:
    def __init__(self):
        self.cuerpo = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direccion = Vector2(0, 0)
        self.crece = False

    def dibujar(self):
        color = pygame.Color('salmon')
        for block in self.cuerpo:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
            pygame.draw.rect(ventana, color, block_rect)

    def mover(self):
        if self.crece == True:
            body_copy = self.cuerpo[:]
            body_copy.insert(0, body_copy[0] + self.direccion)
            self.cuerpo = body_copy[:]
            self.crece = False
        else:
            body_copy = self.cuerpo[:-1]
            body_copy.insert(0, body_copy[0] + self.direccion)
            self.cuerpo = body_copy[:]

    def crecer(self):
        self.crece = True
    def reinicia(self):
        self.cuerpo = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direccion = Vector2(0, 0)

class FRUTA:
    def __init__(self):
        self.posiciona()

    def dibujar(self):
        x_pos = int(self.pos.x * cell_size)
        y_pos = int(self.pos.y * cell_size)
        color = pygame.Color('red')
        fruta = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        pygame.draw.rect(ventana, color, fruta)

    def posiciona(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.vivora = VIVORA()
        self.fruta = FRUTA()

    def actualiza(self):
        self.vivora.mover()
        self.revisa_comer()
        self.revisa_fallo()

    def dibuja_componentes(self):
        self.dibuja_pasto()
        self.fruta.dibujar()
        self.vivora.dibujar()
        self.pinta_record()

    def revisa_comer(self):
        if self.fruta.pos == self.vivora.cuerpo[0]:
            self.fruta.posiciona()
            self.vivora.crecer()

    def revisa_fallo(self):
        if not 0<=self.vivora.cuerpo[0].x<cell_number or not 0<=self.vivora.cuerpo[0].y<cell_number:
            self.termina_juego()

        for block in self.vivora.cuerpo[1:]:
            if block==self.vivora.cuerpo[0]:
                self.termina_juego()

    def dibuja_pasto(self):
        color_pasto=pygame.Color(0, 220, 100)
        for reng in range(cell_number):
            if reng%2==0:
                for col in range(cell_number):
                    if col%2==0:
                        pasto_cuadro = pygame.Rect(col*cell_size,reng*cell_size,cell_size,cell_size)
                        pygame.draw.rect(ventana,color_pasto,pasto_cuadro)
            else:
                for col in range(cell_number):
                    if col%2!=0:
                        pasto_cuadro = pygame.Rect(col*cell_size,reng*cell_size,cell_size,cell_size)
                        pygame.draw.rect(ventana,color_pasto,pasto_cuadro)

    def pinta_record(self):
        score_text='Score '+str(len(self.vivora.cuerpo)-3)
        score_superficie=letra.render(score_text,True,(56,74,12))
        score_x=int(cell_size*cell_number-80)
        score_y = int(cell_size * cell_number - 40)
        score_rect=score_superficie.get_rect(center=(score_x,score_y))
        ventana.blit(score_superficie,score_rect)
        
    def termina_juego(self):
        self.vivora.reinicia()

pygame.init()  # inicializa el ambiente
cell_size = 15
cell_number = 40
ventana = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))  # crea la ventana
reloj = pygame.time.Clock()  # obtiene el objeto reloj
letra=pygame.font.Font(None,25)

pygame.display.set_caption('Vivorita')
color_lienzo = pygame.Color(0, 200, 100)

ventana_actualiza = pygame.USEREVENT
pygame.time.set_timer(ventana_actualiza, 150)

juego = MAIN()

# loop de ejecucion
while True:
    # detecta los eventos
    for evento in pygame.event.get():
        # valida el cierre de la ventana
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == ventana_actualiza:
            juego.actualiza()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                if juego.vivora.direccion.y!=1:
                    juego.vivora.direccion = Vector2(0, -1)
            if evento.key == pygame.K_RIGHT:
                if juego.vivora.direccion.x != -1:
                    juego.vivora.direccion = Vector2(1, 0)
            if evento.key == pygame.K_DOWN:
                if juego.vivora.direccion.y != -1:
                    juego.vivora.direccion = Vector2(0, 1)
            if evento.key == pygame.K_LEFT:
                if juego.vivora.direccion.x != 1:
                    juego.vivora.direccion = Vector2(-1, 0)

    ventana.fill(color_lienzo)
    juego.dibuja_componentes()
    # actualiza la ventana
    pygame.display.update()
    reloj.tick(60)  # controla la velocidad del juego
