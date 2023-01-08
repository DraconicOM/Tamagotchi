class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.food = 20
        self.health = 80
        self.age = 1
    def ChangeName(self, newName):
        self.name = newName
    def ChangeFood(self, valorF):
        self.food += valorF
        if self.food > 100:
            self.food = 100
        elif self.food < 0:
            self.food = 0
    def ChangeHealth(self, valorS):
        self.health += valorS
        if self.health > 100:
            self.health = 100
        elif self.health < 0:
            self.health = 0
    def ChangeAge(self):
        self.age += 1
    def ReturnName(self):
        return self.name
    def ReturnFood(self):
        return self.food
    def ReturnHealth(self):
        return self.health
    def ReturnAge(self):
        return self.age
    def ReturnMood(self):
        mood = self.health + self.food 
        return mood

nomeB = input('Qual o name que deseja colocar no seu bichinho? ')
Bichinho = Tamagotchi(name = nomeB)
while (Bichinho.health > 0) and (Bichinho.food < 100):
    Bichinho.ChangeFood(+2)
    Bichinho.ChangeHealth(-2)
    Bichinho.ChangeAge()
    resposta = input(f"""\n------------------------------------------\n __         __
/  \.-" "-./  \.
\    -   -    /
 |   o   o   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`
     \nOlá meu nome é {Bichinho.name}. O que você deseja fazer comigo agora? \n1- Alimentar (-10 de fome)\n2- Dormir (+10 de saúde)\n3- Mudar meu nome\n4- Visualizar humor\n5- Visualizar idade\n6- Visualizar fome\n7- Visualizar saúde\nResposta: """)
    print('\n')
    if resposta == '1':
        Bichinho.ChangeFood(-10)
        print("-10 de fome! Obrigado!")
    elif resposta == '2':
        Bichinho.ChangeHealth(+10)
        print("+10 de saúde! Obrigado!")
    elif resposta == '3':
        nome2 = input('Qual nome deseja colocar? \n')
        Bichinho.ChangeName(nome2)
    elif resposta == '4':
        print("Humor: ", Bichinho.ReturnMood())
    elif resposta == '5':
        print("Idade: ", Bichinho.ReturnAge())
    elif resposta == '6':
        print("Fome: ", Bichinho.ReturnFood())
    elif resposta == '7':
        print("Vida: ", Bichinho.ReturnHealth())
    else:
        print('Escolha um número válido!')
else:
    print("""\n------------------------------------------\n __         __
/  \.-" "-./  \.
\    -   -    /
 |   X   X   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`\nVocê me deixou morrer!\n""")