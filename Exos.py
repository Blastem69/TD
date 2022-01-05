""" 
1. Faire une fonction qui prend en argument un nombre et 
qui retourne le double de ce nombre

2. Une fonction qui prend en argument un nombre et qui 
retourne true si il est paire et false si il est impair

3. Une fonction qui prend en argument une list de nombres et 
qui retourne le premier nombre de la list

4. Une fonction qui prend en argument une list de nombres et 
qui retourne le dernier nombre de la list

5. Une fonction qui prend en argument une list de nombres et 
qui retourne la somme de tous les nombres de la list

6. Une fonction qui prend en argument une list de nombres et 
qui retourne le plus grand nombre de la list
"""



def double(number):
    
    return number * 2

print(double(3))
print(double(5))

def exo2(number):
   paire = [0, 2, 4, 6, 8 ]
   number_as_string = str(number)
   print(number_as_string)
   last_position = len(number_as_string) - 1
   print(last_position)
   last_chr = number_as_string[last_position]
   last_digit = int(last_chr)
   print(last_digit)
   if last_digit in paire  :
       return True
   else:
        return False
print("Numero 0") 
print(exo2(45643))
print("Numero 3 ")
print(exo2(9))

def first(list):
    return list[0]
print(first([1, 2, 3, 4, 5, 6 ,78 ,9 ]))
print(first([999, 2, 3, 4, 5, 6 ,78 ,9 ]))

def last(list):
    return list[-1]
print(last([1, 2, 3, 4, 5, 6, 7 , 8, 9, 7, 8,9 ,7 ,63613451]))


def somme(liste):
    result = 0
    position_max = len(liste)
    listeee = range(0, position_max)
    print(list(listeee))
    for i in listeee:
          result = result + liste[i] 
    return result
        
    
   
print(somme([1 ,2 ,3 ,4 ,5 ]))
print(somme([1 ,2 ,3 ,4 ,5 ,6 ]))

def tall_number(liste):
    result = 0
    for number in liste:
        if result <= number:
            result = number

    return result

print(tall_number([36, 68,25]))
print(tall_number([158, 4546, 15488]))