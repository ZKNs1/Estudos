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

## Função Input
Permitir que um usuário digite e armazenar essa informação.

Exemplo: 
```python
Nome= input('Qual seu nome')
print(f'Oii {Nome}! Bem-vindo')
```