class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None
        self.value = None

class MyHashMap:

    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)]
        

    def put(self, key: int, value: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = ListNode(key)
        cur.next.value = value
        

    def get(self, key: int) -> int:
        index = key % len(self.set)
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        index = key % len(self.set)
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        




# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)