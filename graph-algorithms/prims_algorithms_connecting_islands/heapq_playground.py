import heapq

# initialize an empty list
#heappush
minHeap = list()

# insert 5 into heap
heapq.heappush(minHeap, 6)
# insert 6 into heap
heapq.heappush(minHeap, 6)
# insert 2 into heap
heapq.heappush(minHeap, 2)
# insert 1 into heap
heapq.heappush(minHeap, 1)
# insert 9 into heap
heapq.heappush(minHeap, 9)

print("After pushing, heap looks like: {}".format(minHeap))


#heappop
# pop and return smallest element from the heap
smallest = heapq.heappop(minHeap)
print("Smallest element in the original list was: {}".format(smallest))
print("After popping, heap looks like: {}".format(minHeap))


# heappush and heappop for items with multiple entries
# Note: If you insert a tuple inside the heap, the element at 0th index of the tuple is used for comparision

minHeap = list()
heapq.heappush(minHeap, (0, 1))
heapq.heappush(minHeap, (-1, 5))
heapq.heappush(minHeap, (2, 0))
heapq.heappush(minHeap, (5, -1))

print("After pushing, now heap looks like: {}".format(minHeap))


# pop and return smallest element from the heap
smallest = heapq.heappop(minHeap)
print("Smallest element in the original list was: {}".format(smallest))
print("After popping, heap looks like: {}".format(minHeap))




