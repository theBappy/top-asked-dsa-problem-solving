import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        temp = head
        while temp:
            self.arr.append(temp.val)
            temp = temp.next

    def getRandom(self) -> int:
        n = len(self.arr)
        random_index = random.randint(0, n - 1)
        return self.arr[random_index]
