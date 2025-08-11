"""
Exercício para trabalhar conversão de tipos de dados e formatação .2f
valor = float(input("Valor do produto: "));
print(f"R$ {valor*1.10:.2f}");
"""

"""
Exercício para trabalhar múltiplas entradas no input e trabalhar com métodos string
Posso utilizar o método upper direto no print {nome.upper()}

dados = input("Digite seu nome, idade e altura: ").split()
nome = dados[0].upper()
idade = dados[1]
altura = dados[2]

print(f'Meu nome é {nome}, tenho {idade} anos de idade e {altura}cm de altura')
"""

"""
Operadores de comparação 

a = 10
b = 20
print(a == b) #false
print(a != b) #true
print(a > b) #false
print(a < b) #true
print(a >= b) #false
print(a <= b) #true
"""

"""
Exercício para trabalhar condições

idade = int(input("Digite a sua idade: "))

#if idade >= 18 and idade < 60:
if 18 <= idade < 60:
    print("adulto")
elif idade < 18:
    print("menor de idade")
else:
    print("idoso")
"""

"""
Exercício de temperatura

temp = int(input("digite a temperatura: "))

if temp<10:
    print("muito frio")
elif 10 <= temp <= 20:
    print("esta fresco")
else:
    print("está quente")
"""

"""
Exercício saudações

horas = int(input("Informe as horas: "))

if horas < 12:
    print("Bom dia")
elif 12 <= horas < 18:
    print("Boa tarde")
else:
    print("Boa noite")
"""

"""
Exercício de desconto

valor = float(input("digite o valor do produto: R$ "))

if 100 < valor < 200:
    print(f"O valor final é R${valor-(valor*0.1)}")
elif valor > 200:
    print(f"O valor final é R${valor-(valor*0.2)}")
else: 
    print(f"O valor final é R${valor-(valor*0.05)}")
"""

"""
Exercício de login

Username = 'admin'
Password = '123456'

username = input('Digite o username: ')
password = input('Digite a password: ')

if Username==username and Password == password:
    print('Login OK')

else:
    print('username or password wrong')
"""

"""
nota = float(input("Digite a nota: "))

if nota >= 9:
    print("Você tirou um A")
elif 7 <= nota < 9:
  e  print("Você tirou um B")
elif 5 <= nota < 7:
    print("Você tirou um C, da pra melhorar")
else:
    print("Você reprovou")
"""

"""
Exercício com string

mensagem = 'eu vou me matar'

print(mensagem.find('e'))
"""

"""
Exercício Lista

tarefas = []

tarefas.append('Estudar Python')
tarefas.append('Academia')
tarefas.append('Ler livro')
print('Tarefas de hoje:\n')
for tarefa in tarefas:
    print(f'- {tarefa}')
"""

"""
Exercício For

for i in range(6):
    print(i)
"""

"""
Exercício While

i = 0
while i <= 10:
    print (i)
    i+=1
"""

"""
Exercício Tuple

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril')
print(meses)
"""

"""
Exercícios Dicionário

usuario = {
        'nome': 'meli',
        'idade': 18,
        'departamento': 'TI'
    }

print(usuario)
print(usuario['nome']) # Para buscar somente um campo, retorna: meli

usuario['idade'] = 19 # Para alterar uma informação
print(usuario['idade']) # 19

Exercício 2 utilizando input
aluno={
    'nome': input('Digite o nome do aluno: '),
    'idade': input('Digite a idade do aluno: '),
    'nota': input('Digite a nota do aluno: ')  
}

print(f"{aluno['nome']} tem {aluno['idade']} anos de idade e tirou a nota {aluno['nota']}")
"""

"""
Exercícios de função

def saudacao(nome):
    return 'Oieee '+nome

def soma(n1, n2):
    return n1 + n2

def desconto(preco, desconto):
    return preco - (preco*desconto/100)

def verificar_idade(idade):
    if idade < 18:
        return 'Menor de idade'
    
    elif 18<= idade < 60:
        return 'Adulto'
    
    else:
        return 'Idoso'
        
main.py

from lista import *

print(saudacao('meli'))
print(desconto(soma(50,50), 20))
minha_idade = int(input('Qual a sua idade? '))
print(verificar_idade(minha_idade))
"""

# Praticar função que calcula média de uma lista
"""
# Função
def calc_media(lista):
    return sum(lista)/len(lista) # Somo tudo da lista e divido pelo número de itens

notas=[5, 3, 8] # Passo a lista
media = calc_media(notas) # Chamo a função e salvo a resposta na variavel 'media'
print(f"Média: {media:.2f}")
"""

"""# Função que calcula o maior valor de uma lista
valores = [2, 20, 5, 18] # Retornar 20 que é o maior valor

def maior_valor(lista):
    return max(lista)

print(maior_valor(valores))
"""

"""
# Utilizando for
valores = [2, 20, 5, 18]

def maior_valor(lista):
    maior = 0
    for i in range(len(lista)):
        #'lista[maior]' imagino q vai percorrer o index
        if lista[i] > maior:
            maior = lista[i]     
    return maior

print(maior_valor(valores))
"""

"""
# Versão For Correta
valores = [2, 20, 5, 18]

def maior_valor(lista):
    maior = lista[0] # Começar com um valor da lista 
    for i in range(1, len(lista)): #Começar a percorrer a partir do segundo valor, pois o primeiro ja está salvo
        if lista[i] > maior: 
            maior = lista[i]     
    return maior

print(maior_valor(valores))
"""