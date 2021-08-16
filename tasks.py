import pandas as pd

#task_2
def change(workbook_name):
    games = pd.read_excel(workbook_name, sheet_name = 'Sheet1')
    df = pd.DataFrame(games)
    df = df[df['Platform'] != 'Wii'].rename(columns={'Platform': 'New Platform', 'Name': 'New Name', 'Genre': 'New Genre'}).fillna(0)
    df.to_excel("task_1_output.xlsx")

    print('Success')

# task_3
def entered(workbook_name):
    students = pd.read_excel(workbook_name)
    df = pd.DataFrame(students)
    df['T'] = ((df.Point > 75) & (df.City != "TARAZ")).replace({True: 'Поступил', False: 'Не поступил'})
    df.to_excel("task_2_output.xlsx")
    print("Success")

# task_4
def group_by(workbook_name):
    things = pd.read_excel(workbook_name)
    df = pd.DataFrame(things)
    sum = df.groupby(['City'], as_index=False)['Point'].sum()
    sum.to_excel("task_3_1_output.xlsx", index=False)

    max = df.groupby(['Name'], as_index=False)['Point'].max()
    max.to_excel("task_3_2_output.xlsx", index=False)
    print("Success")


if __name__ == "__main__":
    task_name = int(input("Enter task number: "))
    workbook_name = str(input("Enter xlsx filename with xlsx: "))
    if task_name == 1:
        change(workbook_name)
    elif task_name == 2:
        entered(workbook_name)
    else:
        group_by(workbook_name)