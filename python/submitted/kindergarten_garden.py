import pandas as pd

PLANTS = ["Violets", "Clover", "Radishes", "Grass"]
PLANT_ABBREV = {plant[0].upper():plant for plant in PLANTS}
STUDENTS = ['Alice', 'Bob', 'Charlie', 'David',
            'Eve', 'Fred', 'Ginny', 'Harriet',
            'Ileana', 'Joseph', 'Kincaid', 'Larry']
GARDEN_COLS_PER_STUDENT = 2
GARDEN_NUM_ROWS = 2

class Garden(object):
    """
    Given a diagram, determine which plants each child in the kindergarten 
    class is responsible for.
    """
    def __init__(self, diagram='', students=STUDENTS):
        self.students = sorted(students)
        
        gardenindex = pd.MultiIndex.from_product(
                [self.students, range(GARDEN_COLS_PER_STUDENT)])
        self.garden = pd.DataFrame('', index=range(GARDEN_NUM_ROWS),
                                   columns=gardenindex)
        
        diagram_lists = [list(row) for row in diagram.split('\n')]
        
        # the diagram always starts filling in the garden at the "top left"
        if diagram_lists:
            self.garden.iloc[:len(diagram_lists), 
                             :len(diagram_lists[0])] = diagram_lists

    def plants(self, student):
        plant_df = self.garden[student]
        return [PLANT_ABBREV.get(plant, 'Unknown Plant')
                for plant in plant_df.to_numpy().flatten()
                if plant.strip()]
