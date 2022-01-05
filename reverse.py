def reverse(string):
    result = "" 
   
    for position in range(len(string)-1 , -1 ,-1):
        
        result = result + string[position]
        
    return result




print(reverse("abc"))
print(reverse("123456789"))

exemple = "justin"

#print(exemple[1])
#print(len(exemple))  
print(reverse(exemple)) 
print(reverse("seb"))

