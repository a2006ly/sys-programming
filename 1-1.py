def fb(n):
    s = ('FizzBuzz', '', '', 'Fizz', '', 
         'Buzz', 'Fizz', '', '','Fizz', 
         'Buzz', '', 'Fizz', '', '')
    return s[n % 15]

i = 1
while i <= 20:
    print(i, fb(i))
    i = i + 1