# Python

Linguagem de programação de alto nível, enfatizando a legibilidade do código e uma sintaxe clara e direta.

## f-string
Colocar texto junto das variáveis
```python
print(f' Meu nome é {nome} e tenho {idade} anos')
```

## Métodos String
- `upper`: tudo maiúsculo;
- `lower`: tudo minúsculo;
- `strip`: retira espaços;
- `replace`: substitui uma palavra por outra;
- `split`: separa palavra por palavra;
- `capitalize`: a primeira letra fica maiúscula;
- `find`: achar uma letra, uma palavra ou até uma frase, retorna a primeira ocorrência;

## Escape Sequence
O `\n` quebra linha, já o `\t` forma a coluna.

Exemplo: 
```python
print('Nome:\tMelina\nIdade:\t19\nEstado:\tSão Paulo')

Return:
Nome: Melina
Idade: 19
Estado: São Paulo
```

Quando quiser utilizar normalmente a \ é só colocar duas que ela mostrará uma, pois não vai ser identificada como escape.

Pra colocar aspas no meio do texto basta colocar \, exemplo: 
```python
print('Oi \'Thomas\', tudo bem?')
Return: Oi 'Thomas', tudo bem?
```

## Caracteres Unicode
Código de algum caractere especial, exemplo: `Coração: \u2764`.

## Funções
### Input
Permitir que um usuário digite e armazenar essa informação.

Exemplo: 
```python
Nome= input('Qual seu nome')
print(f'Oii {Nome}! Bem-vindo')
```

**Multiplas entradas num mesmo input**
Para inserir multiplas entradas, a solução é utilizar o método Split para separar as respostas, porém se formos printar a variável que as armazenou ele retornará como uma lista.

```python
entradas = input("Digite os números separados por espaço: ").split()
print(entradas) # ['10', '20', '30']

dados = input("Digite seu nome e idade: ").split()
# Como será uma lista cada dado sera armazenado numa posição
nome = dados[0]
idade = dados [1]
```

### Type
Retorna o tipo de dado de uma variável.

Exemplo: 
```python
x = 10
print(type(x))  # <class 'int'>
```

Quando estamos trabalhando com o Input o type irá retornar string, para receber o tipo certo da variável deveremos converter a string para o tipo correto. 

### Conversão de Dados

- `int`: converte dados para inteiro;
- `float`: converte dados para float;
- `bool`: converte dados para booleano;
- `str`: converte dados para string.

Exemplo: o input armazena a informação em string, o int converte essa informação para um valor inteiro
```python
idade = int(input('digite sua idade')) 
print(type(idade)) # <class 'int'>
```

## Operadores de Comparação
Retorna em booleano
- `==`: igual a, exemplo: `x == y`;
- `!=`: diferente de, exemplo: `x != y`;
- `>`: maior que, exemplo: `x > y`;
- `<`: menor que, exemplo: `x < y`;
- `>=`: maior ou igual a, exemplo: `x >= y`;
- `<=`: maior ou igual a, exemplo: `x <= y`.

## Condições
- `if`: se (true);
- `elif`: ou;
- `else`: senão (false).

## Slice
É uma forma de acessar partes de sequências.

Sintaxe:
```python
sequencia[início:fim:passo]
```
- `início`: onde começa (inclusivo);
- `fim`: índice onde termina (exclusivo);
- `passo`: de quantos em quantos pula.

Exemplos:
```python
s = "python"
print(s[0:4])    # 'pyth' → começa no índice 0, vai até 3
print(s[:])      # 'python' → cópia completa
print(s[::-1])   # 'nohtyp' → inverte a string
print(s[:3])     # 'pyt' → início padrão = 0
print(s[3:])     # 'hon' → fim padrão = final da string
print(s[::2])    # 'pto' → pega de 2 em 2

lista = [10, 20, 30, 40, 50]
print(lista[1:4])     # [20, 30, 40]
print(lista[::-1])    # [50, 40, 30, 20, 10]
```
