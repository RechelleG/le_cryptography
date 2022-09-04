# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 15:21:18 2022

@author: Rechelle Govender
"""

import string

alphabetLower = list(string.ascii_lowercase)
# alphabet = str(alphabetLower)

print(alphabetLower)

key = 14

message = "Hi There"
nospaceMsg = message.replace(" ", "")
lowerMsg = nospaceMsg.lower()

print(list(message))

splitMsg = list(lowerMsg)

idxFnd = []

   
# for y in alphabetLower:
#     print(y)
    
for x in splitMsg:
    print(x)
    idxFnd.append(alphabetLower.index(x))
    
idxCipher = []

for i in idxFnd:
    newIdx = i+key
    if newIdx > 26:
        newIdx = newIdx - 26
        idxCipher.append(newIdx)
    else:
        idxCipher.append(newIdx)
        
newMsg = []
            
for j in idxCipher:
    newMsg.append(alphabetLower[j])
 
# newMsg = str(newMsg)
          
checkMsg = []

for k in idxFnd:
    checkMsg.append(alphabetLower[k])

# checkMsg = str(checkMsg)
            
        
    

        
        

