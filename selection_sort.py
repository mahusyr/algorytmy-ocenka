def selection_sort(tablica):
    for i in range(len(tablica)):                                           # Wybiera pierwszy nieposortowany indeks
        min_index = i                                                       # Tworzy slota na minimalny indeks i przypisuje domyślnie pierwszy indeks
 
        for j in range(i + 1, len(tablica)):                                # Iteruje po każdym następnym indeksie
            if tablica[j] > tablica[min_index]:                             # Porównuje czy następne indeksy są mniejsze od pierwszego
                min_index = j                                               # Podmienia slota min_index na 'j'

        tablica[i], tablica[min_index] = tablica[min_index], tablica[i]     # Zamienia miejscami 