#import bibliotek
import aseegg as ag
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#pobranie danych
data = pd.read_csv('sub1trial14.csv', names=['0','1','2','3','4','liczba'])

#filtrowanie
przefiltrowany_sygnal= ag.pasmowoprzepustowy(ag.pasmowozaporowy(data['1'], 200, 49, 51), 200, 1, 50)

#wykrycie mrugnięcia oraz print wyniku (zdekodowanie informacji)
print([data['liczba'][i] for i in range(1,len(przefiltrowany_sygnal)) if przefiltrowany_sygnal[i]>=0.1 and przefiltrowany_sygnal[i-1]<0.1])
