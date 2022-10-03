# This is a sample Python script.
import arcpy
import pandas as pd
from arcpy import management

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

fc = r'c:/hh/ll'

print(arcpy.management.GetCount(fc))
where_clause = f""""""


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

df = pd.DataFrame({'C1':['a','b','c'],'C2':[2,4,6]})
df.info()
