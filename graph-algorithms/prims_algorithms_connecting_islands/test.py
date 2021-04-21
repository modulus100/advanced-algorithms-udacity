from pyparsing import nums


def getMinimumCost(k, c):
    c.sort(reverse=True)
    cost = 0
    previous_purchase = 0
    for i in range(len(c)):
        cost += (previous_purchase + 1) * c[i]
        if (i + 1) % k == 0:
            previous_purchase += 1
    return cost


def sherlock_and_anargams(s):
    d = {}
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = ''.join(sorted(s[i:j + 1]))
            d.setdefault(substring, 0)
            d[substring] += 1
            print(substring)
    print("")


def candies(n, arr):
    res = [1] * n

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            res[i] = res[i - 1] + 1

    for i in range(len(arr) - 1, 0, -1):
        print(i)
        if (arr[i - 1] > arr[i]) and (res[i - 1] <= res[i]):
            res[i - 1] = res[i] + 1
    return sum(res)


# print(candies(10, [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]))

# print(sherlock_and_anargams("abba"))
# print(getMinimumCost(3, [1, 3, 5, 7, 9]))

class Node:
    def __init__(self, total_sum=0, p_sum=0, is_leaf=False, is_delivery_node=False):
        self.total_sum = total_sum
        self.p_sum = p_sum
        self.is_leaf = is_leaf
        self.is_delivery_node = is_delivery_node

    def get_p_sum(self):
        if self.total_sum > self.p_sum:
            return self.total_sum

        return self.p_sum if self.total_sum > 0 else self.total_sum


'''Helper Function - Find the max crossing sum w.r.t. middle index'''


def maxCrossingSum(arr, start, mid, stop):
    '''LEFT PHASE - Traverse the Left part starting from mid element'''
    leftSum = arr[mid]  # Denotes the sum of left part from mid element to the current element
    leftMaxSum = arr[mid]  # Keep track of maximum sum

    # Traverse in reverse direction from (mid-1) to start
    for i in range(mid - 1, start - 1, -1):  # The second argument of range is not inclusive. Third argument is the step size.
        leftSum = leftSum + arr[i]
        if (leftSum > leftMaxSum):  # Update leftMaxSum
            leftMaxSum = leftSum

    '''RIGHT PHASE - Traverse the Right part, starting from (mid+1)'''
    rightSum = arr[mid + 1]  # Denotes the sum of right part from (mid+1) element to the current element
    rightMaxSum = arr[mid + 1]  # Keep track of maximum sum

    # Traverse in forward direction from (mid+2) to stop
    for j in range(mid + 2, stop + 1):  # The second argument of range is not inclusive
        rightSum = rightSum + arr[j]
        if (rightSum > rightMaxSum):  # Update rightMaxSum
            rightMaxSum = rightSum

    '''Both rightMaxSum and lefttMaxSum each would contain value of atleast one element from the arr'''

    return Node(leftMaxSum + rightMaxSum)


'''Recursive function'''


def maxSubArrayRecursive(arr, start, stop):  # start and stop are the indices
    # Base case
    if start == stop:
        return Node(arr[start], 0, True)

    if start < stop:
        mid = (start + stop) // 2  # Get the middle index
        L = maxSubArrayRecursive(arr, start, mid)  # Recurse on the Left part
        R = maxSubArrayRecursive(arr, mid + 1, stop)  # Recurse on the Right part
        C = maxCrossingSum(arr, start, mid, stop)  # Find the max crossing sum w.r.t. middle index

        subSeqSum = 0
        if L.is_leaf and L.total_sum > 0:
            subSeqSum += L.total_sum
        if R.is_leaf and R.total_sum > 0:
            subSeqSum += R.total_sum
        if C.is_leaf and C.total_sum > 0:
            subSeqSum += C.total_sum

        delivery_sum = 0
        if L.is_delivery_node:
            delivery_sum += L.p_sum
        if R.is_delivery_node:
            delivery_sum += R.p_sum
        if C.is_delivery_node:
            delivery_sum += C.p_sum

        max_sum = max(C.total_sum, max(L.total_sum, R.total_sum))  # Return the maximum of (L,R,C)

        if max_sum == L.total_sum:
            return Node(L.total_sum, delivery_sum + subSeqSum, False, True)
        if max_sum == R.total_sum:
            return Node(R.total_sum, delivery_sum + subSeqSum, False, True)
        return Node(C.total_sum, delivery_sum + subSeqSum, False, True)

    else:  # If ever start > stop. Not feasible.
        return Node(nums[start])


def maxSubArray(arr):
    start = 0  # staring index of original array
    stop = len(arr) - 1  # ending index of original array
    return maxSubArrayRecursive(arr, start, stop)


# arr = [-1, 2, 3, -4, 5, 10]
# arr = [-1, -1, -1, -1]
# arr = [1, 2, 3, 4]
# arr = [2, -1, 2, 3, 4, -5]
# arr = [1]
# arr = [-1, -2, -3, -4, -5, -6]
# arr = [1, -2]
# arr = [1, 2, 3]
# arr = [-10]
# arr = [1, -1, -1, -1, -1, 5]
arr = [2, -1, 2, 3, 4, -5]
node = maxSubArray(arr)
print("Max1 = ", node.total_sum, " Max2 = ", node.get_p_sum())
