# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = '/home/marcos/Desktop/Cursos_DataScience/DataCamp/Data-Science-for-Everyone/Files/file1.xlsx'

# Carregando o arquivo excel: xls
xls = pd.ExcelFile(file)

# Mostrando o nome das planilhas
print(xls.sheet_names)

print('Carregando os dados da planilha para um dataframe:')


# Carregando a planilha para um dataframe: df1
df1 = xls.parse('Planilha2')
print(df1.head())

# Carregando a planilha usando o index: df2
df2 = xls.parse(0)
print(df2.head())
