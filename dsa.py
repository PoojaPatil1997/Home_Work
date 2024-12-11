'''
        *
       **
      ***
     ****
'''
'''n=4
i=1
while i<=n:
    j=1
    bg=''
    while j<n+1-i:
        bg+=' '
        j+=1
    j=1
    while j<=i:
        bg+=str('*')
        j+=1
    print(bg)
    i+=1'''

'''
   *
  ***
 *****
*******
'''
'''n=4
i=1
while i<=n:
    j=1
    bg=''
    while j<n+1-i:
        bg+=' '
        j+=1
    j=1
    while j<=i*2-1:
        bg+=str('*')
        j+=1
    print(bg)
    i+=1'''

'''def sum_even_odd_digites(number):
    rem=0
    odd=0
    even=0
    while number>0:
        rem = number%10
        if rem%2==0:
            even=even+rem
        else:
            odd=odd+rem
        number = number//10 
    if number==0:
        print("Sum of even & odd digites is:",even,"&",odd)
        
num = int (input("Enter number to calculate sum of odd&even digites:"))
sum_even_odd_digites(num)'''


'''12345678910
123456789
12345678
1234567
123456
12345
1234
123
12
1'''


'''
AAAA
BBBB
CCCC
DDDD'''

'''n=4
i=1
C=65
while i<=n:
    j=1
    bg =''
    while j<=n:
        bg+=chr(C)
        j+=1
    C+=1
    print(bg)
    i+=1'''

'''
A
BB
CCC
DDDD

n=4
i=1
C=65
while i<=n:
    j=1
    bg =''
    while j<=i:
        bg+=chr(C)
        j+=1
    C+=1
    print(bg)
    i+=1'''


'''A
AB
ABC
ABCD'''

'''n=4
i=1

while i<=n:
    j=1
    bg =''
    C=65
    while j<=i:
        bg+=chr(C)
        j+=1
        C+=1
    print(bg)
    i+=1'''
#print prime numbers from 2 to n
n=10
i=2
while i<n:
    j=2
    flag=False

    if i%j==0:
            flag = True
    else:
            j+=1
    if flag != True:
        print(i,"is a prime no")
    i+=1