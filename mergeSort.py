def merge (left, right, array, reverse):
    l = 0
    r = 0
    a = 0

    if reverse:
        while l < len(left) and r < len(right):

            if left[l] > right[r]:
                array[a] = left[l]
                l += 1

            else:
                array[a] = right[r]
                r += 1

            a += 1

        while l < len(left):
            array[a] = left[l]
            l += 1
            a += 1

        while r < len(right):
            array[a] = right[r]
            r += 1
            a += 1

    else:
        while l < len(left) and r < len(right):

            if left[l] < right[r]:
                 array[a] = left[l]
                 l += 1

            else:
                array[a] = right[r]
                r += 1

            a += 1

        while l < len(left):
            array[a] = left[l]
            l += 1
            a += 1

        while r < len(right):
            array[a] = right[r]
            r += 1
            a += 1


def merge_sort(array, reverse=False):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left, reverse)
        merge_sort(right, reverse)

        merge(left, right, array, reverse)


li = [1, 5, 8, 2, 67, 89, 235, 326, 23, 62, 7632, 72, 372, 73, 27]
merge_sort(li)
print(li)
merge_sort(li, True)
print(li)











