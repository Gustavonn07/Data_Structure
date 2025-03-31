principal_string = 'Hello World'
principal_string_notTrim = '  Hello World   '

print(principal_string.capitalize())
print(principal_string.upper())
print(principal_string.lower())
print(principal_string.replace('Hello', 'Bye'))
print(principal_string.find('e'))
print(principal_string.find('World'))
#Metade da palavra
print(principal_string[0:len(principal_string)//2 + 1])

print(principal_string_notTrim.strip())