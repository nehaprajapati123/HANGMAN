def hangman(list_of_words):
    name=input("please enter your name:-  ")
    print("๐",name," welcome to the  game  H A N G M A N =>")
    print("lets have some fun๐๐๐")
    print("---------------------------------------")
    import random
    word=random.choice(list_of_words)
    secret_list=list(word)
    print(word,"is secret word")
    print("you have to choose one word at a time from the given list:-")
    print("a b c d e f g h i j k l m n o p q r s t u v w x y z")
    print(len(word),"alphabets are there in the secret word:-")
    a="_ "
    blanck_fills=[]
    for i in range (len(word)):
        print(a,end="")
        blanck_fills.append(a)
    print()
    insert=0
    for chances in range(10,0,-1):
        print("you have",chances,"chances๐งฟ")
        alphabet=input("enter your alphabet:- ")
        if alphabet in blanck_fills:
            print("invalid! you already expose it,try another execpt this alphabet...")
            continue
        else:
            for j in range(len(secret_list)):
                if alphabet in secret_list:
                    if secret_list[j]==alphabet:
                        blanck_fills.pop(j)
                        blanck_fills.insert(j,alphabet)
                        insert=insert+1
                else:
                    if chances==10:
                        print('__')
                        print("you can do it,just be carefull!๐๐๐")
                    elif chances==9:
                        print("______")
                        print("dont give up๐ค๐ค๐ค")
                    elif chances==8:
                        print('_____')
                        print('|')
                        print('|')
                        print('|')
                        print('|')
                        print("please move carefully๐ฒ๐ฒ๐ฒ")
                    elif chances==7:
                        print('_________')
                        print('|')
                        print('|')
                        print('+++++++++')
                        print("๐ณ๐ณ๐ณ first think then type, okay!  ")
                    elif chances==6:
                        print('__________')
                        print('|      o       ')
                        print('|')
                        print('+++++++++++')
                        print("pitt jaoge thik se khello๐๐๐")
                    elif chances==5:
                        print('___________')
                        print('|       o       ')
                        print('|       |')
                        print('|      / \         ')
                        print('+++++++++++')
                        print("only 4 chances left now,ruk jao chappal tyar hai๐ฐ๐ฐ๐ฐ")
                    elif chances==4:
                        print('____________')
                        print('|       o       ')
                        print('|      /|\       ')
                        print('|      / \         ')
                        print('++++++++++++')
                        print("๐ตโ๐ซ๐ตโ๐ซ๐ตโ๐ซ mujhe chkkr aarhe hai")
                    elif chances==3:
                        print('____________')
                        print('|      o |       ')
                        print('|     /|\       ')
                        print('|     / \         ')
                        print('++++++++++++++')
                        print(" its going to die, please save him๐ฅบ๐ฅบ๐ฅบ ")
                    elif chances==2:
                        print('___________')
                        print('|      o  _|       ')
                        print('|     /|\       ')
                        print('|     / \         ')
                        print('++++++++++++++++')
                        print("ohh noo ab kya hoga๐ณ๐ณ๐ณ")
                    elif chances==1:
                        print('___________')
                        print('|      o__|       ')
                        print('|     /|\       ')
                        print('|     / \         ')
                        print('|++++++++++++++')
                        print("tumhari wjh se bechara mrr gya๐ !")
                    break
            print(blanck_fills)
            if insert==len(secret_list):
                if chances>0:
                    print("you won the game, you save a life๐ฅณ๐ฅณ๐ฅณ")
                    break
                else:
                    print("you loose, better luck next time๐๐๐")
            else:
                pass
hangman(["ritesh","neha","shresth","pagalora","yogesh","vishal","sanjeev","dipesh","dinesh","ajay","shiv","sahil"])

