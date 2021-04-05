from heapq import *


def find_closest_elements(arr, K, X):
    # Time: O(N)
    # Space: O(K)
    result = []
    heap = []
    for i in range(K):
        if i < len(arr):
            heappush(heap, (-abs(X - arr[i]), arr[i]))

    for i in range(K, len(arr)):
        if -abs(X - arr[i]) >= heap[0][0]:
            heappop(heap)
            heappush(heap, (-abs(X - arr[i]), arr[i]))

    while heap:
        result.append(heappop(heap)[1])

    return sorted(result)


def main():
    print(
        "'K' closest numbers to 'X' are: "
        + str(find_closest_elements([5, 6, 7, 8, 9], 3, 7))
    )
    print(
        "'K' closest numbers to 'X' are: "
        + str(find_closest_elements([2, 4, 5, 6, 9], 3, 6))
    )
    print(
        "'K' closest numbers to 'X' are: "
        + str(find_closest_elements([2, 4, 5, 6, 9], 3, 10))
    )


main()
