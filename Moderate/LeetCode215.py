class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def _parent(self, i):
        return (i - 1)//2

    def _left_child(self, i):
        return 2 * i + 1
    
    def _right_child(self, i):
        return 2 * i + 2

    def push(self, val):
        self.heap.append(val)
        self._shif_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap: return not
        if len(self.heap) == 1: return self.heap.pop()

        max_val = self.heap[0]
        self.heap[0] = self.he
    
    def _sift_up(self, index):
        while index > 0 and self.heap[index] > self.heap[self._parent(index)]:
            p_idx = self._parent(index)
            self.heap[index], self.heap[p_idx] = self.heap[p_idx], self.heap[index]
            index = p_idx
        
    def _shif_down(self, index):
        n = len(self.heap)
        while True:
            largest = index
            left = self._left_child(index)
            right = self._right_child(index)

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right
            
            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[len(nums) - k]
