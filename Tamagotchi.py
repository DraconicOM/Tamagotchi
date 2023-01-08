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

nomePet = input('Qual o name que deseja colocar no seu Pet? ')
Pet = Tamagotchi(name = nomePet)
while (Pet.health > 0) and (Pet.food < 100):
    Pet.ChangeFood(+2)
    Pet.ChangeHealth(-2)
    Pet.ChangeAge()
    resposta = input(f"""\n------------------------------------------\n __         __
/  \.-" "-./  \.
\    -   -    /
 |   o   o   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`
     \nOlá meu nome é {Pet.name}. O que você deseja fazer comigo agora? \n1- Alimentar (-10 de fome)\n2- Dormir (+10 de saúde)\n3- Mudar meu nome\n4- Visualizar humor\n5- Visualizar idade\n6- Visualizar fome\n7- Visualizar saúde\nResposta: """)
    print('\n')
    if resposta == '1':
        Pet.ChangeFood(-10)
        print("-10 de fome! Obrigado!")
    elif resposta == '2':
        Pet.ChangeHealth(+10)
        print("+10 de saúde! Obrigado!")
    elif resposta == '3':
        nome2 = input('Qual nome deseja colocar? \n')
        Pet.ChangeName(nome2)
    elif resposta == '4':
        print("Humor: ", Pet.ReturnMood())
    elif resposta == '5':
        print("Idade: ", Pet.ReturnAge())
    elif resposta == '6':
        print("Fome: ", Pet.ReturnFood())
    elif resposta == '7':
        print("Vida: ", Pet.ReturnHealth())
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