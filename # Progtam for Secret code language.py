# Progtam for Secret code language
# import random, string
# def randomword(length):
#     letters = string.ascii_lowercase
#     return ''.join(random.choice(letters) for i in range(length))

import random_string
st = input("Enter message to be encrypted :")
words = st.split(" ")
coding = input("Enter 1 for coding or 0 for the decoding: ")
coding = True if(coding=="1") else False
if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = random_string.randomwords(3)
            r2 = random_string.randomwords(3)
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
    
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
        
else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
    
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
            
