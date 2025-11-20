import random
words=["glove","serve","stuck","block","haven","craft","hello","build","stone","apple"]
secrets_word=random.choice(words)
attempts=6
while attempts!=0:
    correct_letters=[-1,-1,-1,-1,-1]
    user_word=input()
    if len(user_word)!=5:
        print("error. word length is less than 5 ")
    else:
        attempts-=1
        for i in range(5):
            if user_word[i]==secrets_word[i]:
                correct_letters[i]=1
            else:
                for j in range(i,5):
                    if user_word[j]==secrets_word[j]:
                        correct_letters[j]=0
                        break
                break