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

  Para entender melhor essa ideia, você usará ** kwargs neste exercício para definir uma função que aceita um número variável de argumentos de palavras-chave. A função simula um sistema simples de relatório de status que imprime o status de um personagem em um filme. 