class Solution:
    def fib(self, n: int) -> int:
           
        fk0, fk1 = 0, 1
        
        for _ in range(n):
            fk0, fk1 = fk1, fk0 + fk1
        
        return fk0
        
        # WHY CAN'T USE GENERATOR????
#         def fibGen():
#             fk0, fk1 = 0, 1
#             while True:
#                 yield fk0
#                 fk2 = fk0 + fk1
#                 fk0, fk1 = fk1, fk2

#         fn = 0
#         for i in range(n):
#             fn = next(fibGen())        
#         return fn
        
        
        