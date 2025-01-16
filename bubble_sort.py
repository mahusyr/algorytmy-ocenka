def bubble_sort(tablica):
    for i in range(0, len(tablica)):                                # Wybiera piewrszy nieposortowany indeks
        
        for j in range(0, len(tablica)):                            # Wybiera każdy następny indeks
            if tablica[i] > tablica[j]:                             # Porównuje czy następne indeksy są mniejsze od pierwszego
                tablica[i], tablica[j] = tablica[j], tablica[i]     # Zamienia miejscami