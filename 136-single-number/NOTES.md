https://realpython.com/python-bitwise-operators/#bitwise-logical-operators
​
```
def xor(a, b):
return (a and not b) or (not a and b)
```
​
Xor of any two num gives the difference of bit as 1 and same bit as 0.
```
nums = [4,2,4,1,1]
xor = 0
for n in nums:
xor ^= n
print(xor)
# output: 4 6 2 3 2
```
​
​
https://thepythonguru.com/python-builtin-functions/reduce/
​
The reduce() function accepts a function and a sequence and returns a single value calculated as follows:
Initially, the function is called with the first two items from the sequence and the result is returned.
The function is then called again with the result obtained in step 1 and the next value in the sequence. This process keeps repeating until there are items in the sequence.