# Manipulando String 

# positivos
text = 'João Pablo'
new_string = text[0:8]
new_string = text[0:]
new_string = text[:10]
new_string = text[0::3]

# negativos
new_string2 = text[-8:-2]

print(new_string)
print(new_string2)
print(len(text))

for letra in text:
    print(letra)