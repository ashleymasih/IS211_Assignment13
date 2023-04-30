def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
    
def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)
    
def compareTo(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 0
    elif len(s1) == 0:
        return -1
    elif len(s2) == 0:
        return 1
    else:
        if s1[0] < s2[0]:
            return -1
        elif s1[0] > s2[0]:
            return 1
        else:
            return compareTo(s1[1:], s2[1:])
        

print(fibonacci(0))   
print(fibonacci(1))   
print(fibonacci(5))   

print(gcd(10, 25))  
print(gcd(14, 28))   
print(gcd(50, 75))  
print(gcd(17, 31))  
print(compareTo("apple", "banana"))   
print(compareTo("apple", "Apple"))   
print(compareTo("apple", "apple"))   
print(compareTo("a", ""))     