#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TESTE DE BACKEND NIVEL 1 - GRUPO PEGAZUS

#Faça o teste abaixo 100% sozinho, sem a ajuda de CHAT GPT, amigos, familiares, professores ou etc.. conseguimos facilmente identificar

#lembre-se de detalhar as respostas, assim conseguimos analisar ainda mais o seu conhecimento tecnico

#caso prefira, pode fazer o desafio em outro arquivo separado, e só colar a solução completa abaixo de cada exercicio
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


#1- usando o json abaixo, retire somente os produtos em que o preço seja maior do que 30 Reais 
#Explique detalhadamente por que voce decidiu essa solução e não outra
response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]

# Solução: 

produtos_acima_30 = [] # Lista para guargar os produtos acima de 30 reais 
for loja in response: # Laço para percorrer cada dicionário na lista 'response'
    for produto in loja['produtos']: # Laço para percorrer os produtos no dicionários
        if produto['preço'] > 30: #Condição para verificar se o preço dos produtos é maior que 30 reais
            produtos_acima_30.append([produto['nome'], produto['preço']]) #Se for, o nome do produto e seu preço será adicionado a lista 'produtos_acima_30'

print(produtos_acima_30) #Mostra quais foram os produtos
#Utilizei esta solução pois utilizava menos linhas de código e é fácil de entender.




#2-Use o JSON abaixo para capturar o preço do produto B
#explique detalhadamente por que escolheu essa solução e não outra

responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

#Solução
for produto in responsejson['produtos']: # Cria um laço para a lista de produtos dentro do dicionário
    if produto['nome'] == 'Produto B': # Verifica se o nome do produto atual é igual o nome do produto que se deseja extrair o preço
        print(produto['nome'],':',produto['preço']) # Se for igual, o nome e o preço serão capturados.
#Utilizei esta solução com laços para facilitar a escolhar de qualquer outro produto, basta apenas mudar o nome do produto que se deseja extrair o preço.



#3- Ordene a lista abaixo em ordem crescente
#explique detalhadamente por que escolheu essa solução e não outra

lista = [5,8,3,0,8,1,9,10,20,30]

# Solução
lista.sort() # Método específico para organizar elementos de uma lista em ordem crescente.
print(lista) # Devolve a lista reorganizada
# Utilizei esta solução pois já existia um método nativo para organizar listas em ordem crescente.



#4-Retire todos os espaços em branco, crie uma nova lista e adicione esses itens nela

lista = ["   joao   ","   maria   ","  joana  "]

# Solução
lista_sem_espacos = [] # Cria uma nova lista onde serão armazenado os nomes sem espaços.

for nome in lista: # Cria um laço para percorrer cada nome na lista
    nome_sem_espaco = nome.strip() # A variável 'nome_sem_espaco' recebe o nome da lista junto do método nativo strip() que serve justamente para retirar espaços no início e no fim de strings.
    lista_sem_espacos.append(nome_sem_espaco) # a lista de nomes sem espaço recebe o novo nome sem espaços no início e no fim.

print(lista_sem_espacos) # Mostra a nova lista de nome sem espaço.
# Utilizei novamente uma solução com laços pois é a maneira mais eficiente de retirar os espaços dos nomes na lista, já que em ocasiões em que há uma maior quantidade de nome, seria util.



#5-Retire o segundo item dessa lista e imprima ela:

lista = [1,2,3,4,5,6]

# Solução
del(lista[1]) # Método para excluir um elemento de uma lista utilizando seu índice
print(lista)


#6-substitua todos os "joao" da lista por "maria"

lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]

# Solução
i = 0 # Cria um índice
for i in range(len(lista)): # Faz uma laço para percorrer os índices la lista partindo de 0 e terminando até o último índice
    if lista[i] == 'joao': # Caso o valor do índice seja igual a 'joao'
        lista[i] = 'maria' # O valor do índice será substituído por 'maria'
print(lista)



#7-criar um loop while em Python que itera sobre os itens de uma lista e imprime os itens enquanto o valor de uma variável é menor ou igual a 5. Após imprimir cada item, o valor da variável é incrementado em 1
#explique detalhadamente por que escolheu essa solução e não outra

# Solução
lista = [1,2,3,4,5,6,7,8,9,10] # Cria uma lista com valores 

var = 5 # Inicializo uma variavel de valor 5
i = 0 # Inicializo um índice de valor 0
while var != 0: # Cria um laço que se repete enquanto o valor da variavel é diferente de zero
    print(lista[i]) # Imprime o item da lista correspondente ao índice
    i+=1 # Aumenta o valor do índice para passar para o próximo item
    var -=1 # Diminui o valor da variavel em 1



#8-usando a biblioteca requests, faça uma requisição http para o endpoint https://jsonplaceholder.typicode.com/todos. cada objeto dentro do json possui a chave "completed". que indica se a task foi completada ou não. Faça uma função que trate a resposta e retorne a quantidade de tasks completadas, e a quantidade de tasks pendentes
#explique detalhadamente por que escolheu essa solução e não outra

# Solução
import requests # Importação da biblioteca 'requests'


def retorna_tasks(): # Criação da função que retorna o status das tasks
    response = requests.get('https://jsonplaceholder.typicode.com/todos') # Método para fazer a requisição http ao endpoint
    

    tasks = response.json() # Converte a resposta para json

    completas = 0 # Inicializa a quantidade de tasks completas
    pendentes = 0 # Inicializa a quantidade de tasks pendentes

    for task in tasks: # Cria um laço para percorrer cada task
        if task['completed'] == True: # Se o valor da chave 'completed' for igual a True, o contador de completas aumenta em 1
            completas +=1
        else:
            pendentes +=1 # Caso o valor da chave seja falso, o contador de pendentes aumenta em 1
    return completas, pendentes # Retorna a quantidade de completas e pendentes

completas, pendentes = retorna_tasks() # Variáveis pegam esses valores e armazenam 

print(f'Completas: {completas}') # Imprime a quantidade de tasks completas
print(f'Pendentes: {pendentes}') # Imprime a quantidade de tasks pendentes



#9-faça uma requisição em uma API  https://jsonplaceholder.typicode.com/users e com os dados retornados 
# faça um parsing de dados e retire  o nome, username, email, rua, numero
#explique detalhadamente por que escolheu essa solução e não outra


# Solução
import requests # Importação da biblioteca 'requests'


lista_usuarios = [] # Cria uma lista para armazenar os usuarios
def retorna_dados(): # Cria função 
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    usuarios = response.json()

    for usuario in usuarios:
        dados = [usuario['name'],usuario['username'],usuario['email'],usuario['address']['street'], usuario['address']['zipcode']]
        lista_usuarios.append(dados)
    return lista_usuarios
 

lista_usuarios = retorna_dados()
for usuario in lista_usuarios:
    print(f'Nome: {usuario[0]}')
    print(f'Username: {usuario[1]}')
    print(f'Email: {usuario[2]}')
    print(f'Endereço: {usuario[3]}')
    print(f'Número: {usuario[4]}')
    print('-'*20)

# Optei por utilizar uma lista para armazenar os dados dos usuários mas poderia ser facilmente substituida por um dicionário


#10-crie uma lista e adicione um item novo a ela utilizando a metodologia FIFO

fila = [1,2,3,4,5]
fila.append(6)

#11-crie uma lista e adicione um item novo a ela utilizando a metodologia LIFO

pilha = [3,7,2,5]  # Criando uma lista qualquer com valores aleatórios
pilha.insert(0,30) # Adicionando um novo valor com o método insert(), sendo o primeiro argumento a posição do elemento, e o segundo o valor
print(pilha)

#DESAFIO!!

#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta

class Banco:
    id = 0

    def __init__(self,nome,cpf,saldo=0):
        self.id = Banco.id
        Banco.id +=1
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo
    
    def saque(self,x):
        if self.saldo < x:
            print('Saldo insuficiente')
        else:
            self.saldo -= x
            print(f'Saldo realizao com sucesso. Saldo atual: {self.saldo}')

    def deposito(self,x):
        self.saldo += x
        print(f'Depósito realizado com sucesso. Saldo atual: {self.saldo}')

    def ver_saldo(self):
        print(f'Seu saldo atual é: R${self.saldo}')

contas = []

while True:
    print()
    print('1. Criação de conta')
    print('2. Realizar depósito')
    print('3. Realizar saque')
    print('4. Ver saldo atual')
    print('5. Sair')
    opcao = int(input('Digite qual opção você deseja: '))
    print()

    if opcao == 1:
        nome = input('Digite seu nome: ')
        cpf = input('Digite seu CPF: ')
        conta = Banco(nome,cpf)
        contas.append(conta)
        print(f'Conta criada com sucesso! Nome: {conta.nome} CPF: {conta.cpf} ')

    elif opcao == 2:
        deposito = float(input('Digite o valor do depósito: '))
        conta.deposito(deposito)
    
    elif opcao == 3:
        saque = float(input('Digite o valor do depósito: '))
        conta.saque(saque)
    
    elif opcao == 4:
        conta.ver_saldo()

    elif opcao == 5:
        break

    else: 
        print('Digite uma opção válida!')