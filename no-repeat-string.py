plik = ['AZ', 'AZ', 'AZ', 'AZ', 'ZAZ', 'ZAZD', '','AAAAAAAAAAAAAAAAAA', 'Z', 'AZ', 'AZ', 'AZ']
result = ('', 0)
for word in plik:
    if (temp_unique := len(set(char for char in word))) > result[1]:
        result = (word, temp_unique)

print(*result)
