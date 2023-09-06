mylist = [1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99, 106, 113, 120, 127, 134, 141, 148, 155, 162, 169,
          176, 183, 190, 197, 204, 211, 218, 225, 232, 239, 246, 253, 260, 267, 274, 281, 288, 295, 302, 309, 316, 323,
          330, 337, 344, 351, 358, 365, 372, 379, 386, 393, 400, 407, 414, 421, 428, 435, 442, 449, 456, 463, 470, 477,
          484, 491, 498]

low = 0
high = len(mylist)
num = int(input("What number are you looking for: "))


def search(low, high):
    if high < low:
        return "is not found..."
    mid = int((low + high) / 2)

    if mylist[mid] > num:
        return search(low, mid - 1)
    elif mylist[mid] < num:
        return search(mid + 1, high)
    else:
        return mid


print(num, "is at position", search(low, high))
