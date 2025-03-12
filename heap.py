
"""
V Pythonu lze pracovat s haldou pomoci modulu heapq. Halda je reprezentovana jako seznam s korenem v prvnim prvku.
- prevod seznamu na haldu heapify(heap)
- pridani prvku do haldy -> heappush(heap, item)
- odebrani nejmensio pryku z haldy heappop(heap)
"""

from heapq import heappush, heappop, heapify

moje_halda = []

heappush(moje_halda, 5)
heappush(moje_halda, 4)
heappush(moje_halda, 8)
heappush(moje_halda, 9)
heappush(moje_halda, 7)
heappush(moje_halda, 1)
heappush(moje_halda, 2)

print(moje_halda)
print(heappop(moje_halda))
print(moje_halda)
# print(moje_halda)
print(heappop(moje_halda))
print(moje_halda)
print(heappop(moje_halda))
print(heappop(moje_halda))
print(moje_halda)

print(heappop(moje_halda))
print(heappop(moje_halda))
print(heappop(moje_halda))
print(moje_halda)

arr2 = [7, 6, 8, 9, 0, 1, 3, 2, 4, 5]
heapify(arr2)
print(arr2)

def heap_sort(arr):
    # TODO: vytvor prazdnou haldu
    new_heap = []

    # TODO: do haldy vloz prvky z arr (heappush)
    for element in arr:
        heappush(new_heap, element)

    # TODO: vytvor promennou sorted_list = []
    sorted_list = []

    # TODO: Do sorted list postupne vkladej serazene prvky z haldy (heappop)
    #while len(new_heap) > 0:
    while new_heap:
        sorted_list.append(heappop(new_heap))
    return sorted_list

arr3 = [7, 6, 8, 9, 0, 1, 3, 2, 4, 5]
arr4 = [7, 2, 5, 3, 8, 4, 1, 6]
arr5 = [1, 3, 2, 4, 5, 7, 6, 8, 9, 0]

print(heap_sort(arr3))
print(heap_sort(arr4))
print(heap_sort(arr5))