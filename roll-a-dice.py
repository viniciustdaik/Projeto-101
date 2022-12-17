import random

response = "y"

while response == "y":
    no = random.randint(1, 6)
    # if no == 1:
    print("[-----]")
    print("[     ]")
    print("[  "+str(no)+"  ]")  # "[  0  ]"
    print("[     ]")
    print("[-----]")

    response = input("Quer jogar o dado novamente?(y/n): ")
    #"Pressione y para jogar novamente e n para sair:"
