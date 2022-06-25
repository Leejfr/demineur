"""
Jeu classique du démineur
"""
import pygame
from game import *
import gameConfig

def show_box(cell_line, cell_column, number_of_mines_near_current_cell):
    game_window.blit(gameConfig.NO_MINE, (cell_column*30, cell_line*30))
    number_color = (0,0,255)
    if number_of_mines_near_current_cell > 1: number_color = (69,139,0)
    if number_of_mines_near_current_cell > 2: number_color = (255,48,48)
    game_window.blit(pygame.font.SysFont("monospace", 16, bold=True).render(str(number_of_mines_near_current_cell), 1, number_color), (cell_column*30+10, cell_line*30+5))
    shown.append((cell_line, cell_column))

          
def show_empty_box(cell_line, cell_column):
    list_cell_to_show = g.getAdjacentCellsWithoutMines(cell_line, cell_column)
    empty_boxes = []
    for (cell_to_show_line, cell_to_show_column, nb_mines) in list_cell_to_show : 
        game_window.blit(gameConfig.NO_MINE, (cell_to_show_column*30, cell_to_show_line*30))
        shown.append((cell_to_show_line, cell_to_show_column))
        if nb_mines > 0:
            number_color = (0,0,255)
            if nb_mines > 1: number_color = (69,139,0)
            if nb_mines > 2: number_color = (255,48,48)
            game_window.blit(pygame.font.SysFont("monospace", 16, bold=True).render(str(nb_mines), 1, number_color), (cell_to_show_column*30+10, cell_to_show_line*30+5))          
        else:
            if cell_to_show_line != cell_line or cell_to_show_column != cell_column:
                empty_boxes.append((cell_to_show_line, cell_to_show_column))
            else :
                toshow.append((cell_to_show_line,cell_to_show_column))

    for (row, col) in empty_boxes:
        if (row, col) not in toshow : show_empty_box(row, col)
        
def playGame():
    pygame.display.flip()
    loose = False

    while True:
        ev = pygame.event.wait()
        if ev.type == pygame.QUIT:
            pygame.display.quit()
            break
        elif ev.type == pygame.MOUSEBUTTONDOWN and not loose:
            (x,y) = pygame.mouse.get_pos()
            cell_line = y//30
            cell_column = x//30

            cell_value = g.getCellValue(cell_line, cell_column)
            
            if ev.button == 1: #click gauche
                if cell_value == 1:
                    game_window.blit(gameConfig.MINE_RED_BOX, (cell_column*30, cell_line*30))
                    pygame.display.flip()
                    loose = True
                else:
                    # on verifie s'il y a des mines a cote
                    # si oui on affiche le nombre de mine a cote
                    # sinon on affiche toutes les cellules adjacentes n'ayant pas de mine
                    number_of_mines_near_current_cell = g.getMinesNumberNearCell(cell_line, cell_column)

                    if number_of_mines_near_current_cell == 0:
                        toshow = []
                        show_empty_box(cell_line, cell_column)
                    else:
                        show_box(cell_line, cell_column,number_of_mines_near_current_cell)
            elif ev.button == 3: #click droit
                if (cell_line, cell_column) not in shown:
                    game_window.blit(gameConfig.FLAG_BOX, (cell_column*30, cell_line*30))
                    
        pygame.display.flip()
        

"""
Lance le jeu
"""
g = Game(10,10)
#g.display()

# initialisation de la grille
pygame.init()
game_window = pygame.display.set_mode((10*30,10*30))
game_window.fill(pygame.Color("grey"))
pygame.display.set_caption("Démineur")

# affichage de la grille initiale
for row in range(10):
    for col in range(10):
        game_window.blit(gameConfig.EMPTY_BOX, (row*30, col*30))

toshow = []
shown = []
playGame()

