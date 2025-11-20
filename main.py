import random
print("*** ВІТАЄМО У WORDLE ***")
print("У вас є 6 спроб, щоб вгадати слово з 5 літер.")
words=["glove","serve","stuck","block","haven","craft","hello","build","stone","apple"]
secrets_word=random.choice(words)
attempts=6
while attempts>0:
    print(f"Спроба {7-attempts}/6")
    correct_letters=[-1,-1,-1,-1,-1]
    user_word=input("Введіть слово: ")
    if len(user_word)!=5:
        print("error. word length is don't equal 5 ")
    else:
        attempts-=1
        for i in range(5):
            if user_word[i]==secrets_word[i]:
                correct_letters[i]=1
            else:
                for j in range(5):
                    if user_word[i]==secrets_word[j]:
                        correct_letters[i]=0
                        break
        print("результат:",end=" ")
        for i in range(5):
            if correct_letters[i]==1:
                print(f"[{user_word[i]}]",end=" ")
            elif correct_letters[i]==0:
                print(f"({user_word[i]})",end=" ")
            else:
                print(f"{user_word[i]}", end=" ")
        print("\n")
