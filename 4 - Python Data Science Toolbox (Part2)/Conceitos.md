## Usando iteradores em PythonLand

Você aprenderá tudo sobre iteradores e iteráveis, com os quais já trabalhou ao escrever loops for. Você aprenderá algumas funções úteis que permitirão trabalhar efetivamente com iteradores. E você terminará o capítulo com um caso de uso pertinente ao mundo da ciência de dados e que lida com grandes quantidades de dados - neste caso, dados do Twitter que você carregará em blocos usando iteradores.

- **Usando enumerate(**)

    O enumerate() retorna um objeto enumerate que produz uma sequência de tuplas, e cada uma das tuplas é um par índice-valor. No exemplo, temos uma lista de strings *mutantes* e vamos praticar o uso do enumerate() nela, imprimindo uma lista de tuplas e descompactando-as usando um loop for.

- **Usando zip()**

    Outra função interessante  é a zip(), que pega qualquer número de iteráveis e retorna um objeto zip que é um iterador de tuplas. Se você quiser imprimir os valores de um objeto zip, poderá convertê-lo em uma lista e depois imprimi-lo. Imprimir apenas um objeto zip não retornará os valores, a menos que você o descompacte primeiro. Neste exemplo, você vai explorar isso.

    Três listas de strings são pré-carregadas: mutants, aliases e powers. Primeiro, você usará list() e zip() nessas listas para gerar uma lista de tuplas. Em seguida, você criará um objeto zip usando zip(). Finalmente, você descompactará este objeto zip em um loop for para imprimir os valores em cada tupla. Observe a saída diferente gerada imprimindo a lista de tuplas, depois o objeto zip e, finalmente, os valores da tupla no loop for.

    ```python
    # Create a list of tuples: mutant_data
        mutant_data = list(zip(mutants,aliases,powers))

        # Print the list of tuples
        print(mutant_data)

        # Create a zip object using the three lists: mutant_zip
        mutant_zip = zip(mutants,aliases,powers)

        # Print the zip object
        print(mutant_zip)

        # Unpack the zip object and print the tuple values
        for value1,value2,value3 in mutant_zip:
            print(value1, value2, value3)
    
    Output:
    [('charles xavier', 'prof x', 'telepathy'), ('bobby drake', 'iceman', 'thermokinesis'), ('kurt wagner', 'nightcrawler', 'teleportation'), ('max eisenhardt', 'magneto', 'magnetokinesis'), ('kitty pryde', 'shadowcat', 'intangibility')]

    <zip object at 0x7fcc653ef388>

    charles xavier prof x telepathy
    bobby drake iceman thermokinesis
    kurt wagner nightcrawler teleportation
    max eisenhardt magneto magnetokinesis
    kitty pryde shadowcat intangibility
    ```
    Uma forma mais simples de descompactar um objeto zip() é usando o operador *. Exemplo:

    
    ```python
    # Create a zip object from mutants and powers: z1
    z1 = zip(mutants,powers)

    # Print the tuples in z1 by unpacking with *
    print(* z1)

    Output:
    ('charles xavier', 'telepathy') ('bobby drake', 'thermokinesis') ('kurt wagner', 'teleportation') ('max eisenhardt', 'magnetokinesis') ('kitty pryde', 'intangibility')
    ```
## Compreensões de lista

Neste capítulo, você desenvolverá seu conhecimento sobre iteradores e será apresentado a compreensões de listas, que permitem criar listas complicadas - e listas de listas - em uma linha de código! As compreensões de lista podem simplificar drasticamente seu código e torná-lo mais eficiente, e se tornarão uma parte vital de sua caixa de ferramentas de ciência de dados Python.

- **Compreensão de Listas / List of Comprehension**
  
    É  uma forma concisa de criar e manipular listas.

    Componentes necessários:

    * Iterável

    * Variável de iterador (representa membros de iterável)

    * Expressão de saída
    
    Exemplo 1:
    
    ```python
    # Criar lista de compreensão: quadrados
    squares = [i**2 for i in range(0,10)]
    print(squares)

    Output:
    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    ```

    Exemplo 2:

    
    ```python
    # Crie uma matriz 5 x 5 usando uma lista de listas: matriz
    matrix = [[col for col in range(0,5)] for row in range(0,5)]

    # Imprima a matriz
    for row in matrix:
        print(row)

    Output:
    [0, 1, 2, 3, 4]
    [0, 1, 2, 3, 4]
    [0, 1, 2, 3, 4]
    [0, 1, 2, 3, 4]
    [0, 1, 2, 3, 4]
    ```



- **Condicionais em listas de compreensão**
    
    * Condicional no interável
    
    Exemplo: 
    
    ```python
        # Create a list of strings: fellowship
        fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

        # Create list comprehension: new_fellowship
        new_fellowship = [member for member in fellowship if len(member) >= 7]

        # Print the new list
        print(new_fellowship)
        Output: 
        ['samwise', 'aragorn', 'legolas', 'boromir']
    ```



    * Condicional na expressão de saída

    Exemplo:
    ```python
    # Create a list of strings: fellowship
            fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

            # Create list comprehension: new_fellowship
            new_fellowship = [members if len(members) >=7 else '' for members in fellowship]

            # Print the new list
            print(new_fellowship)
            Output: 
            ['', 'samwise', '', 'aragorn', 'legolas', 'boromir', '']
    ```
