# Python

Linguagem de programação de alto nível, enfatizando a legibilidade do código e uma sintaxe clara e direta.

## f-string
Colocar texto junto das variáveis
```python
print(f' Meu nome é {nome} e tenho {idade} anos')
```

## Métodos String
- Upper - tudo maiúsculo
- Lower - tudo minúsculo
- Strip - retira espaços
- Replace - substitui uma palavra por outra
- Split - separa palavra por palavra

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

```python
entradas = input("Digite os números separados por espaço: ").split()
print(entradas) # ['10', '20', '30']
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

