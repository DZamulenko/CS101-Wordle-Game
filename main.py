import random
print("*** ВІТАЄМО У WORDLE ***")
print("У вас є 6 спроб, щоб вгадати слово з 5 літер.\n")
words=["glove","serve","stuck","block","haven","craft","hello","build","stone","apple"]
secrets_word=random.choice(words)
attempts=6
sum_cor_let=0
while attempts>0:
    print(f"Спроба {7-attempts}/6")
    #на почату значення всіх елементів масиву -1 і ми вважаємо що слова взагалі не схожі
    correct_letters=[-1,-1,-1,-1,-1]
    user_word=input("Введіть слово: ")
    #валідація
    if len(user_word)!=5:
        print("error. word length is don't equal 5 ")
    else:
        attempts-=1
        #перевіряємо літери на відповідність
        for i in range(5):
            if user_word[i]==secrets_word[i]:
                correct_letters[i]=1
            else:
                #у випадку не відповідності перевіряємо літеру на наявність у масиві
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
        sum_cor_let=sum(correct_letters)
        if sum_cor_let==5:
            print(f"ВІТАЄМО! Ви вгадали слово {secrets_word} на {6-attempts} раз!")
            break
#якщо цикл завершився і сумма правильних літер дорівнює 5 значит повідомлення про перемогу
#вивелось, інакше виведеться повідомлення про програш
if sum_cor_let!=5 :
    print("На жаль ви програли. Пощастить наступного разу")