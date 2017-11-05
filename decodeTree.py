import string 

sembol = list(string.ascii_lowercase)
text = "0000101111"
temp = ""

sozluk = {}
i = 0
j = 0

for i in range(len(text)):
    if(text[i] == "1"):
        sozluk[sembol[j]] = temp
        j += 1
        x = temp[len(temp) - 1]
        temp = temp[:-1]
        while(x == "1"):
            x = temp[len(temp) - 1]
            temp = temp[:-1]
    temp += text[i]
        

temp = temp[:-1]
temp += "1"
sozluk[sembol[j]] = temp
print sozluk
