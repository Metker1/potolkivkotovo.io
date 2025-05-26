# Пирамидальный
import random
import time

def heapify(arr, n, i):
    largest = i # Инициализируем корень как самый большой элемент
    left = 2 * i + 1 # левый дочерний элемент
    right = 2 * i + 2 # правый дочерний элемент

    if left < n and arr[left] > arr[largest]:
        largest=left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # Построение кучи (перегруппировка массива)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]

    # Перемещаем текущий корень в конец
        heapify(arr, i, 0) # Вызываем heapify на уменьшение кучи

arr = []
for i in range(10000):
    arr.append(random.randint(1,10000))

start_time = time.time()
heap_sort(arr)
end_time = time.time()
elapsed = end_time - start_time


print(arr)
print(f'Затраченное время: {elapsed:.4f}')