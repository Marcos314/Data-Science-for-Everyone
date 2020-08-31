# Python Data Science Toolbox (Part 1)

## Escrevendo suas próprias funções

- Definindo uma função (sem parâmetros)

    ```python
    def square():

        resultado = 4 ** 2
        print(resultado)

    square()

    Output: 16
    ```

- Definindo uma função (com parâmetros)


    ```python
    def square(value):

        resultado = value ** 2
        print(resultado)

    square(4)

    Output: 16

    ```

- Docstrings

    Pode ser entendido como uma forma de documentar como uma determinada função funciona.

    ```python
    def square(value):
    """ Retorna o quadrado do valor passado como parâmetro """
        resultado = value ** 2
        return resultado

    print(square(4))
    Output: 16
    ```

- **Multiplos parâmetros e retornando valores**

    Para retornarmos múltiplos valores em uma função, podemos passar uma tupla ao return: return (x,y)

    ```python
    # Define shout_all with parameters word1 and word2
    def shout_all(word1,word2):
        
        # Concatenate word1 with '!!!': shout1
        shout1 = word1 + '!!!'
        
        # Concatenate word2 with '!!!': shout2
        shout2 = word2 + '!!!'
        
        # Construct a tuple with shout1 and shout2: shout_words
        shout_words = (shout1, shout2)

        # Return shout_words
        return shout_words
    
    Output:
    congratulations!!!
    you!!!
    ```
## Argumentos padrão, argumentos de comprimento variável e escopo de funções

- **Funçoes com argumentos padrão**

    No capítulo anterior, você aprendeu a definir funções com mais de um parâmetro e a chamar essas funções passando o número necessário de argumentos. No último vídeo, Hugo construiu essa ideia, mostrando como definir funções com argumentos padrão. Você praticará essa habilidade neste exercício escrevendo uma função que usa um argumento padrão e, em seguida, chamando a função algumas vezes.


    ```python
    # Define shout_echo
    def shout_echo(word1,echo = 1):
        """Concatenate echo copies of word1 and three
        exclamation marks at the end of the string."""

        # Concatenate echo copies of word1 using *: echo_word
        echo_word = echo * word1

        # Concatenate '!!!' to echo_word: shout_word
        shout_word = echo_word + '!!!'

        # Return shout_word
        return shout_word

    # Call shout_echo() with "Hey": no_echo
    no_echo = shout_echo('Hey')

    # Call shout_echo() with "Hey" and echo=5: with_echo
    with_echo = shout_echo("Hey",echo=5)

    # Print no_echo and with_echo
    print(no_echo)
    print(with_echo)

    Output:
    Hey!!!
    HeyHeyHeyHeyHey!!!
    ```

* **Funções com parâmetros variáveis**
  
  * ***args**
  
  Os argumentos flexíveis permitem que você passe um número variável de argumentos para uma função. Neste exercício, você praticará a definição de uma função que aceita um número variável de argumentos de string.

  A função que você definirá é gibberish () que pode aceitar um número variável de valores de string. Seu valor de retorno é uma única string composta de todos os argumentos da string concatenados juntos na ordem em que foram passados para a chamada de função. Você chamará a função com um único argumento de string e verá como a saída muda com outra chamada usando mais de um argumento de string. Lembre-se do vídeo anterior que, dentro da definição da função, args é uma tupla.
  
  
  
  
  
  * ****kwargs**
  
  Vamos prosseguir com o que você aprendeu sobre argumentos flexíveis - você usou * args, agora vai usar ** kwargs! O que torna ** kwargs diferente é que ele permite que você passe um número variável de argumentos de palavras-chave para funções. Lembre-se do vídeo anterior que, dentro da definição de função, kwargs é um dicionário.


    ```python
    # Define gibberish
    def gibberish(*args):
        """Concatenate strings in *args together."""

        # Initialize an empty string: hodgepodge
        hodgepodge = ''

        # Concatenate the strings in args
        for word in args:
            hodgepodge += word

        # Return hodgepodge
        return hodgepodge

    # Call gibberish() with one string: one_word
    one_word = gibberish('luke')

    # Call gibberish() with five strings: many_words
    many_words = gibberish("luke", "leia", "han", "obi", "darth")

    # Print one_word and many_words
    print(one_word)
    print(many_words)
    ```


  Para entender melhor essa ideia, você usará ** kwargs neste exercício para definir uma função que aceita um número variável de argumentos de palavras-chave. A função simula um sistema simples de relatório de status que imprime o status de um personagem em um filme. 

    <div align="center">
        <img src="../Images/anakin.png">
        <img src="../Images/darthvader.png">
        <img src="../Images/luke.png">
    
    </div>

    ```python
    
    # Define report_status
    def report_status(**kwargs):
        """Print out the status of a movie character."""

        print("\nBEGIN: REPORT\n")

        # Iterate over the key-value pairs of kwargs
        for key, value in kwargs.items():
            # Print out the keys and values, separated by a colon ':'
            print(key + ": " + value)

        print("\nEND REPORT")

    # First call to report_status()
    report_status(name='luke',affiliation='jedi', status='missing')

    # Second call to report_status()
    report_status(name='anakin', affiliation='sith lord', status='deceased')
    
    Output:

     BEGIN: REPORT
    
    name: luke
    affiliation: jedi
    status: missing
    
    END REPORT
    
    BEGIN: REPORT
    
    name: anakin
    affiliation: sith lord
    status: deceased
    
    END REPORT
    ```

## Funções Lambda e tratamento de erros

Aprenda sobre as funções lambda permitem escrever funções de maneira rápida e dinâmica. Você também vai estudar como lidar com erros em suas funções, o que é uma habilidade essencial. Em seguida, aplique suas novas habilidades para responder às perguntas da ciência de dados.

### Funções Lambda
- Modelo de uma função lambda        
    ```python
    nome_da_funcao = lambda x,y : x*y

        x,y: são os argumentos da função
        x*y: o que será retornado
    ```
- **Função map()**

    A função map() aplica uma função a um determinado objeto, como uma lista por exemplo.

    ```python
    # Create a list of strings: spells
    spells = ["protego", "accio", "expecto patronum", "legilimens"]

    # Use map() to apply a lambda function over spells: shout_spells
    shout_spells = map(lambda item: item + "!!!", spells)

    # Convert shout_spells to a list: shout_spells_list
    shout_spells_list = list(shout_spells)

    # Print the result
    print(shout_spells_list)
    Output:
    ['protego!!!', 'accio!!!', 'expecto patronum!!!', 'legilimens!!!']
    ```
    Obs: O retorno de uma função map() é outro objeto do tipo <class 'map'>

- **Função filter()**

    A função filter () oferece uma maneira de filtrar elementos de uma lista que não satisfazem certos critérios.



    ```python
    # Create a list of strings: fellowship
    fellowship = ['frodo', 'samwise', 'merry', 'pippin', 'aragorn', 'boromir', 'legolas', 'gimli', 'gandalf']

    # Use filter() to apply a lambda function over fellowship: result
    result = filter(lambda member: len(member) > 6, fellowship) # a função lambda retorna as strings da lista que tem comprimento maior que 6.

    # Convert result to a list: result_list
    result_list = list(result)
    # Print result_list
    print(result_list)

    Output:
    ['samwise', 'aragorn', 'boromir', 'legolas', 'gandalf']
    ```
    Obs: O retorno de uma função map() é outro objeto do tipo <class 'filter'>

- **Reduce()**

    A função reduce() é útil para realizar alguns cálculos em uma lista e, ao contrário de map() e filtro(), retorna um único valor como resultado. Para usar reduce(), você deve importá-lo do módulo functools.


    ```python
    # Import reduce from functools
    from functools import reduce

    # Create a list of strings: stark
    stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

    # Use reduce() to apply a lambda function over stark: result
    result = reduce(lambda item1, item2: item1+" "+ item2, stark)

    # Print the result
    print(result)

    Output:
    robb sansa arya brandon rickon
    ```

### Juntando tudo (1)

Isso é incrível! Agora você aprendeu como escrever funções anônimas usando lambda, como passar funções lambda como argumentos para outras funções, como map (), filter () e reduce (), bem como como escrever erros e enviar mensagens de erro personalizadas dentro suas funções. Agora você colocará esses aprendizados em um bom uso, trabalhando com um conjunto de dados do Twitter. Antes de praticar suas novas habilidades de tratamento de erros, neste exercício, você escreverá uma função lambda e usará filter () para selecionar retuítes, ou seja, tweets que começam com a string 'RT'.  Para ajudá-lo a fazer isso, os dados do Twitter foram importados para o DataFrame, tweets_df. Vá em frente!

- Instruções

    * Na chamada filter (), passe uma função lambda e a sequência de tweets como strings, tweets_df ['text']. A função lambda deve verificar se os primeiros 2 caracteres em um tweet x são 'RT'. Atribua o objeto de filtro resultante ao resultado. Para obter os primeiros 2 caracteres em um tweet x, use x [0: 2]. Para verificar a igualdade, use um filtro booleano com ==.
    * Converta o resultado em uma lista e imprima a lista.

    ```python
    # Select retweets from the Twitter DataFrame: result
    result = filter(lambda x : x[0:2] == 'RT'  , tweets_df['text']) 

    # Create list from filter object result: res_list
    res_list = list(result)

    # Print all retweets in res_list
    for tweet in res_list:
        print(tweet)
    ```
### Juntando tudo (2)

Às vezes, cometemos erros ao chamar funções - mesmo aqueles que você mesmo cometeu. Mas não se preocupe! Neste exercício, você irá aprimorar seu trabalho anterior com a função count_entries () no último capítulo, adicionando um bloco try-except a ela. Isso permitirá que sua função forneça uma mensagem útil quando o usuário chamar sua função count_entries (), mas fornecer um nome de coluna que não está no DataFrame.

Mais uma vez, para sua conveniência, o pandas foi importado como pd e o arquivo 'tweets.csv' foi importado para o DataFrame tweets_df. Partes do código de seu trabalho anterior também são fornecidas.

- Instruções

    * Adicione um bloco try para que, quando a função for chamada com os argumentos corretos, ela processe o DataFrame e retorne um dicionário de resultados.
    * Adicione um bloco except para que quando a função for chamada incorretamente, ela exiba a seguinte mensagem de erro: 'O DataFrame não tem uma coluna' + nome_col + '.'


    ```python
    # Define count_entries()
    def count_entries(df, col_name='lang'):
        """Return a dictionary with counts of
        occurrences as value for each key."""

        # Initialize an empty dictionary: cols_count
        cols_count = {}

        # Add try block
        try:
            # Extract column from DataFrame: col
            col = df[col_name]
            
            # Iterate over the column in dataframe
            for entry in col:
        
                # If entry is in cols_count, add 1
                if entry in cols_count.keys():
                    cols_count[entry] += 1
                # Else add the entry to cols_count, set the value to 1
                else:
                    cols_count[entry] = 1
        
            # Return the cols_count dictionary
            return cols_count

        # Add except block
        except:
            print('The DataFrame does not have a ' + col_name + ' column.')

    # Call count_entries(): result1
    result1 = count_entries(tweets_df, 'lang')

    # Print result1
    print(result1)
    ```
