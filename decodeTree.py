text = "0000101111"
sembol = ["a", "b", "c", "d", "e", "f"]
temp = ""

sozluk = {}
i = 0
j = 0

for i in range(len(text)):
    if(text[i] == "0"):
        temp += "0"  
    else:
        sozluk[sembol[j]] = temp
        j += 1
        x = temp[len(temp) - 1]
        temp = temp[:-1]
        while(x == "1"):
            x = temp[len(temp) - 1]
            temp = temp[:-1]
        temp += "1"
        

temp = temp[:-1]
temp += "1"
sozluk[sembol[j]] = temp
print sozluk
