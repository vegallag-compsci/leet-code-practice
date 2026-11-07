from collections import Counter, deque
import heapq

class Functions:
    def testing(self, param: list[str], n: int) -> int:
        # dq = deque(["A" "B" "C" "D"])
        dq = deque(param)

        # dq[0] access front  //  dq[-1] access end
        print(f"(Front: {dq[0]}), (End: {dq[-1]})")

        # append() -> append to end
        dq.append("H")

        # appendleft() -> append to left end of deque
        dq.appendleft("C")

        # extend() -> add multiple elements to right end of deque 
        dq.extend(["I", "J"])

        # extendleft() -> add multiple elements to left end of deque
        dq.extendleft(reversed(["A", "B"]))
        print(f"(deque: {dq})")

        # remove() -> remove first occurrence of specific value
        dq.remove("A")
        print(f"(deque: {dq})")

        # pop() -> remove and return element from right end
        # popleft() -> remove and return element from left end
        poppedItem = dq.pop()
        print(f"(poppedItem: {poppedItem}), (deque: {dq})")

        # clear() -> removes all elements from the deque
        # len() -> total number of elems in the deque
        # count() -> returns how many times a specific element appears in deque
        print(f"(Count of B: {dq.count("B")})")

        # rotate() -> rotates elements of deque
        # [10 20 30 40] -> rotate(1) -> [40 10 20 30]

        # reverse() -> reverses order of elements in deque
        # [10 20 30 40] -> reverse() -> [40 30 20 10]

        # Cleanup
        dq.appendleft("A")
        dq.append("J")
        print(f"(Cleaned deque: {dq})")
        
        return 1

func = Functions()
result = func.testing(["D", "E", "F", "G"], n = 2)
print(f"Result: {result}")