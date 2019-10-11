alphas=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')


def decrypt(word):
    wordarray=list(word)
    decryptedarray=[]

    for alpha in wordarray:
        index=alphas.index(alpha)
        valueindex=index-3

        if valueindex>25:
            valueindex=valueindex-25
        decryptedarray.append(alphas[valueindex])
        
    return ''.join(decryptedarray)


word=input('Enter a word to decrypt \n >')
decryptedword=decrypt(word)
print(decryptedword)