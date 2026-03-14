def ispalindromo(parola):
 
    if parola == parola[::-1]: return True
    else: return False
    
print(ispalindromo("itopinonavevanonipoti"))