import pandas as pd

class School:
    '''
    Class to maintain a school roster of students by name and grade.  Roster is
    sorted internally only when required.
    '''
    COLUMNS = ['grade', 'name']  # specified in order for multi-level sort
    
    def __init__(self):
        self.school = pd.DataFrame(columns=School.COLUMNS)
        self.sorted_flag = True
    
    def sort_school(self):
        if not self.sorted_flag:
            self.school.sort_values(by=School.COLUMNS, inplace=True)
        self.sorted_flag = True

    def add_student(self, name, grade):
        student = pd.DataFrame([[grade, name]], columns=School.COLUMNS)
        self.school = self.school.append(student, ignore_index=True)
        self.sorted_flag = False

    def roster(self):
        self.sort_school()
        return list(self.school['name'])

    def grade(self, grade_number):
        self.sort_school()
        return list(self.school[self.school['grade'] == grade_number]['name'])
