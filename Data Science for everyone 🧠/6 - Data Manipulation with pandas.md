## Transformação de dados

Obs: O pandas foi construído com base em dois pacotes essenciais: Numpy e Matplotlib.


- **Introdução aos dataframes**

    Método *head()* retorna as primeiras linhas do dataframe
        
        meu_dataframe.head()

    O método *.info()* exibe o nome das colunas, os tipos de dados que elas contêm e se têm algum valor ausente.

        meu_dataframe.info()
    
    O atributo *shape* retorna uma tupla com o número de linhas e colunas respectivamente do dataframe.

        meu_dataframe.shape


    O método *describe()* calcula algumas estatísticas de resumo para colunas numéricas, como media e mediana.

        meu_dataframe.describe()

- **Classificação e subdivisão**

- **Novas colunas**