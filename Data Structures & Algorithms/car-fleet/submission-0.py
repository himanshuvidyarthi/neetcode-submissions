class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        arr = [[p, s] for p,s in zip(position, speed)]
        arr = sorted(arr)
        for p,s in arr[::-1]: #Reverse sorted order

            stack.append((target - p)/s) 
            if len(stack)>=2 and stack[-1]<= stack[-2]:
                stack.pop() 
        return len(stack)





        
        