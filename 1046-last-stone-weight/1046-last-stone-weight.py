class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # min heap as python doesn't have a max heap
        
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        
        stones.append(0)

        return abs(stones[0])
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if len(stones) == 1:
#             return stones[0]
        
#         heap = collections.deque()
#         temp = collections.deque()
        
#         heaviest1 = max(stones[0], stones[1])
#         heap.append(heaviest1)
#         heaviest2 = min(stones[0], stones[1])
#         heap.append(heaviest2)
        
        
#         for stone in stones[2:]:
#             if stone > heaviest1:
#                 heap.appendleft(stone)
#                 heaviest2 = heaviest1
#                 heaviest1 = stone
#                 print(heap)
            
#             elif stone <= heaviest2:
#                 heap.append(stone)
            
#             else:
#                 temp.append(stone)
                
                