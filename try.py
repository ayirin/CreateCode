def currencyexchange(eur):
    if eur<0:
        print("you entered a negative number, please delete the minus and try again")    
    else:
        chf=int(eur*1.1)
        texta=" EUR is "
        textb=" CHF"
        return str(eur)+texta+str(chf)+textb
    

print currencyexchange(50)
