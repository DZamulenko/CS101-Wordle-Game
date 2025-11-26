import random
print("*** ВІТАЄМО У WORDLE ***")
print("У вас є 6 спроб, щоб вгадати слово з 5 літер.\n")
words=["glove","serve","stuck","block","haven","craft","hello","build","stone","apple"]
secrets_word=list(random.choice(words))
attempts=6
correct=True
while attempts>0:
    print(f"Спроба {7-attempts}/6")
    user_word=list(input("Введіть слово: "))
    correct=True
    if len(user_word)!=5:
        print("error. word length is don't equal 5 ")
    else:
        attempts-=1
        for i in range(5):
            if secrets_word[i]==user_word[i]:
                user_word[i]='['+user_word[i]+']'
            else:
                correct=False
                for j in range(i,5):
                    if secrets_word[i]==user_word[j]:
                        user_word[j]='('+user_word[j]+')'
                        break
        print("результат:",user_word)
        if correct:
            print("Вітаю ви вгадали")
            print("Загаданим словом було",end=" ")
            for i in user_word:
                print(i[1],end="")
            break
if not correct:
    print("Нажаль ви не вгадали, спробуйте знову")