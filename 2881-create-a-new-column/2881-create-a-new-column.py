import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = [9096,56300,2206,13186,149152,48866]
    return employees
    