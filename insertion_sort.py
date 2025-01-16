def insertionSort(tablica):
    if len(tablica) <= 1:
        return
 
    for i in range(1, len(tablica)):
        key = tablica[i]
        j = i-1
        while j >= 0 and key < tablica[j]:
            tablica[j+1] = tablica[j]
            j -= 1
        tablica[j+1] = key