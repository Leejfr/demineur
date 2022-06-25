import random

class Box:
    """
    Classe permettant de définir une case du jeu
    """
    def __init__(self) -> None:
        self.value = 0
        self.position = 0
        self.visible = False

    def __repr__(self) -> str:
        return f"{self.value}"

class Game:
    """
    Classe permettant de gerer le jeu
    """
    def __init__(self, nbLines, nbColumns) -> None:
        self.lines = nbLines
        self.columns = nbColumns
        
        # Creation de la grille
        self.matrix = [ [Box() for col in range(nbColumns)] for line in range(nbLines) ]

        # Creation des cellules avec des mines
        number_of_mines = nbLines * nbColumns / 8
        current_mines_set = 0
        while current_mines_set < number_of_mines:
            r = random.choice(random.choice(self.matrix))
            if r.value == 0:
                r.value = 1
                current_mines_set += 1
    
    def display(self):
        """
        Display matrix values
        """
        print(self.matrix)

    def getCellValue(self, line_index, col_index):
        """
        Retourne la valeur actuelle d'une cellule

        Args:
            line_index (int): ligne de la cellule
            col_index (int): colonne de la cellule

        Returns:
            int: 0 = pas de mine / 1 = mine
        """
        return self.matrix[line_index][col_index].value

    def getMinesNumberNearCell(self, cell_row, cell_col):
        """
        Retourne le nombre de mines a cote d'une cellule particuliere

        Args:
            cell_row (int): ligne de la cellule
            cell_col (int): colonne de la cellule
        """
        number_of_mines = 0
        for cell_to_check_row in (cell_row-1,cell_row,cell_row+1):
            for cell_to_check_col in (cell_col-1,cell_col,cell_col+1):
                if( cell_to_check_row < self.lines and cell_to_check_row >= 0 and cell_to_check_col < self.columns and cell_to_check_col >= 0 ):
                    if self.getCellValue(cell_to_check_row,cell_to_check_col) == 1: number_of_mines += 1
        
        return number_of_mines

    def getAdjacentCellsWithoutMines(self, cell_row, cell_col, list_cells=[]):
        """
        Retourne la liste des cellules adajcentes sans mine
        Si une cellule adjacente est a coté d'une ou plusieurs mines, retourne le nombre de mines

        Args:
            cell_row (int): ligne de la cellule
            cell_col (int): colonne de la cellule
        """
        number_of_mines_near_cell = self.getMinesNumberNearCell(cell_row,cell_col)
        if (cell_row,cell_col,number_of_mines_near_cell) not in list_cells:
            list_cells.append((cell_row,cell_col,number_of_mines_near_cell))
        
        if number_of_mines_near_cell == 0:
            for cell_to_check_row in (cell_row-1,cell_row,cell_row+1):
                for cell_to_check_col in (cell_col-1,cell_col,cell_col+1):
                    if cell_to_check_row < self.lines and cell_to_check_row >= 0 and cell_to_check_col < self.columns and cell_to_check_col >= 0 :
                        number_of_mines_near_cell = self.getMinesNumberNearCell(cell_to_check_row,cell_to_check_col)
                        if (cell_to_check_row,cell_to_check_col,number_of_mines_near_cell) not in list_cells:
                            list_cells.append((cell_to_check_row,cell_to_check_col,number_of_mines_near_cell))
                            
        return list_cells