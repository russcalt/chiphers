import math
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "qwertyuiopmnbvcxzghfjdklsa"
keyword = "keyword"
text = "Fiction"
trans_key = 8
matrix = []
result = ""
for i in text:
    if i.lower() in alphabet:
        result += key[alphabet.find(i.lower())]
    else:
        result += i
print(result)       

def encryptMessage(result):
    cipher = " "
    key_index = 0
    res_len = float(len(result))
    res_lst = list(result)
    keyword_lst = sorted(list(keyword))
    
    col = len(keyword)
    #row = int(math.ceil(res_len / col))
    
    matrix = [res_lst[i: i + col]
              for i in range(0, len(res_lst), col)]
    
    for i in range(col):
        indx = keyword.index(keyword_lst[key_index])
        cipher += ''.join([row[indx]
                       for row in matrix])
        key_index += 1
    return cipher 

print(encryptMessage(result))    
        
        
