import random
words=["glove","serve","stuck","block","haven","craft","hello","build","stone","apple"]
secrets_word=random.choice(words)
attempts=6
while attempts!=0:
    user_word=input()
    if len(user_word)!=5:
        print("error. word length is less than 5 ")
    else:
        attempts-=1