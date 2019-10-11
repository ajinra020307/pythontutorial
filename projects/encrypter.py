alphas=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

def encrypt(word):
    wordarray=list(word)
    encryptedarray=[]

    for alpha in wordarray:
        index=alphas.index(alpha)
        valueindex=index+3

        if valueindex>25:
            valueindex=valueindex-25
            encryptedarray.append(alphas[valueindex])
        else:
            encryptedarray.append(alphas[valueindex])
    return ''.join(encryptedarray)
    

word=input('Enter a word to encrypt \n >')
encryptedword=encrypt(word)
print(encryptedword)