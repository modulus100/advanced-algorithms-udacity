from pyparsing import nums


def getMinimumCost(k, c):
    c.sort(reverse=True)
    cost = 0
    previous_purchase = 0
    for i in range(len(c)):
        cost += (previous_purchase +1) * c[i]
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
    def __init__(self, total_sum=0, p_sum=0):
        self.total_sum = total_sum
        self.p_sum = p_sum

    def get_p_sum(self):
        return self.p_sum if self.total_sum > 0 else self.total_sum


'''Helper Function - Find the max crossing sum w.r.t. middle index'''
def maxCrossingSum(arr, start, mid, stop):
    '''LEFT PHASE - Traverse the Left part starting from mid element'''
    leftSum = arr[mid]  # Denotes the sum of left part from mid element to the current element
    leftMaxSum = arr[mid]  # Keep track of maximum sum
    pLeftSum = arr[mid] if arr[mid] > 0 else 0

    # Traverse in reverse direction from (mid-1) to start
    for i in range(mid - 1, start - 1, -1):  # The second argument of range is not inclusive. Third argument is the step size.
        leftSum = leftSum + arr[i]
        if (arr[i] > 0):
            pLeftSum += arr[i]
        if (leftSum > leftMaxSum):  # Update leftMaxSum
            leftMaxSum = leftSum

    '''RIGHT PHASE - Traverse the Right part, starting from (mid+1)'''
    rightSum = arr[mid + 1]  # Denotes the sum of right part from (mid+1) element to the current element
    rightMaxSum = arr[mid + 1]  # Keep track of maximum sum
    pRightSum = arr[mid + 1] if arr[mid + 1] > 0 else 0

    # Traverse in forward direction from (mid+2) to stop
    for j in range(mid + 2, stop + 1):  # The second argument of range is not inclusive
        rightSum = rightSum + arr[j]
        if (arr[j] > 0):
            pRightSum += arr[j]

        if (rightSum > rightMaxSum):  # Update rightMaxSum
            rightMaxSum = rightSum

    '''Both rightMaxSum and lefttMaxSum each would contain value of atleast one element from the arr'''

    return Node(leftMaxSum + rightMaxSum, pRightSum + pLeftSum)


'''Recursive function'''

def maxSubArrayRecursive(arr, start, stop):  # start and stop are the indices
    # Base case
    if start == stop:
        return Node(arr[start])

    if start < stop:
        mid = (start + stop) // 2  # Get the middle index
        L1 = maxSubArrayRecursive(arr, start, mid)  # Recurse on the Left part
        R1 = maxSubArrayRecursive(arr, mid + 1, stop)  # Recurse on the Right part
        C1 = maxCrossingSum(arr, start, mid, stop)  # Find the max crossing sum w.r.t. middle index

        max_sum = max(C1.total_sum, max(L1.total_sum, R1.total_sum)) # Return the maximum of (L,R,C)
        if max_sum == L1.total_sum:
            return L1
        if max_sum == R1.total_sum:
            return R1
        return C1

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
arr = [-2, -3, -1, -4, -6]
node = maxSubArray(arr)
print("Max1 = ", node.total_sum, " Max2 = ", node.get_p_sum())