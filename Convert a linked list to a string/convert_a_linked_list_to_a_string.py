from collections import deque
class FrontMiddleBackQueue:

    def __init__(self):
        self.data=deque()

    def pushFront(self, val: int) -> None:
        self.data.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        self.data.insert(len(self.data)//2,val)

    def pushBack(self, val: int) -> None:
        self.data.append(val)

    def popFront(self) -> int:
        return self.data.popleft()


    def popMiddle(self) -> int:
        self.data.rotate(len(self.data)//2)
        a=self.data.pop()
        self.data.rotate(-len(self.data)//2)
        return a

    def popBack(self) ->    int:
        pass


# Your FrontMiddleBackQueue object will be instantiated and called as such:
obj = FrontMiddleBackQueue()
obj.pushFront(5)
obj.pushBack(1)
print(obj.data)
obj.pushMiddle(12)
print(obj.data)
obj.pushBack(1)
print(obj.popMiddle())
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()