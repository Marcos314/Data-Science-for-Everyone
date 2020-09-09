## Data Merging Basics

Uma junção interna retornará apenas as linhas correspondentes em ambas as tabelas.


<div align='center'>
<img src="./../Images/innerJoin.png" height="250px">
</div>

- **Relação de um-para-um e um-para-muitos**

Em uma relação **um-para-um**, cada linha de uma tabela está relacionada a apenas uma linha de outra tabela.
<div align='center'>
<img src="./../Images/one-to-one.png">
</div>

Em uma relação **um-para-muitos**, cada linha da tabela a esquerda, está relacionada a uma ou mais linhas da tabela a direita.

<div align='center'>
<img src="./../Images/one-to-many.png">
</div>

- **Juntando Dataframes**

Outra operação  relacionada a DataFrames é a operação de fusão. Dois DataFrames podem conter diferentes tipos de informações sobre a mesma entidade(registro) e vinculados por algum recurso (coluna em comum). Para se juntar estas DataFrames, pandas fornece múltiplas funções, como concat(), merge(), join(), etc. Nesta seção, você irá praticar o uso merge()da função de pandas.

Você pode associar DataFrames df(que você criou concatenando df1 e df2 ao longo da linha) e df3 na coluna comum. Para fazer isso, passe os nomes dos DataFrames e um argumento adicional *on* como o nome da coluna comum, aqui id, para a merge()função:


```python
df_merge = pd.merge(df, df1, on='id')
```


O argumento *on* pode receber uma lista e isso permite usar várias colunas em comum entre os dataframes na mesclagem.

```python
ridership_cal = ridership.merge(cal, on=['year','month','day'])
```

## Merging Tables With Different Join Types



