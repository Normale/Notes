'''
Task:
Given list of strings, print the one, that has the largest number of unique characters. 
Print this number.
'''

plik = ['AZ', 'AZ', 'AZ', 'AZ', 'ZAZ', 'ZAZD', '','AAAAAAAAAAAAAAAAAA', 'Z', 'AZ', 'AZ', 'AZ']
result = ('', 0)
for word in plik:
    if (temp_unique := len(set(word))) > result[1]:
        result = (word, temp_unique)

print(*result)
