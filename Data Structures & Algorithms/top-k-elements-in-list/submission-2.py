class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # index = frequency, value = list of numbers with that frequency
        buckets = [[] for i in range(len(nums) + 1)]
        
        # 1. Count occurrences
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # 2. Map frequency to bucket index
        for n, freq in count.items():
            buckets[freq].append(n)
        
        # 3. Collect the top k from the end of buckets
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res