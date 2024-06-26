# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 15:33:43 2022

@author: sinan
"""

# =============================================================================
# Y = w1x1 + w2x2 + w3x3 + w4x4 + w5x5 + w6x6
# Girdi değerleri (x1,x2,x3,x4,x5,x6)=(4,–2,7,5,11,1)
# Bu denklemi maksimize eden parametreleri (ağırlıkları) bulmaya çalışıyoruz. 
# Pozitif giriş, olası en büyük pozitif sayı ile çarpılacak ve 
# negatif sayı, mümkün olan en küçük negatif sayı ile çarpılacaktır.
# GA, pozitif girdilerle pozitif ağırlıkları ve negatif girdilerle 
# negatif ağırlıkları kullanmanın daha iyi olduğunu bilmelidir.
# =============================================================================
"""
from PyQt5 import uic

with open('Anasayfa.py','w',encoding="utf-8") as fout:
    uic.compileUi('Anasayfa.ui',fout)
"""

import sys
import numpy
import GA
import Anasayfa
from distutils.core import setup
from PyQt5 import QtWidgets, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from Anasayfa import *

Uygulama=QApplication(sys.argv)
penAna=QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(penAna)
penAna.show()



def EKLE():
    girdiler=ui.Girdiler.text()
    agirlik=ui.Agirlik.text()
    populasyon=ui.Populasyon.text()
    minAralik=ui.MinAralik.text()
    maxAralik=ui.MaxAralik.text()
    iterasyon=ui.Iterasyon.text()
    bireySayisi=ui.BireSayisi.text()
    
    equation_inputs = numpy.fromstring(girdiler, dtype=float, sep=',')  #girdiler
    num_weights = int(agirlik)#Ağırlıkların sayısı, 
    sol_per_pop = int(populasyon) #Popülasyon başına çözüm 
    num_generations = int(iterasyon)
    num_parents_mating = int(bireySayisi) #eşleşme havuzundaki birey sayısı
    
 
    pop_size = (sol_per_pop,num_weights) #Herbiri x adet genden oluşan y  kromozom

   #Başlangıç popülasyonunun numpy.random.uniform ile random oluşturulması
    new_population = numpy.random.uniform(low=float(minAralik), high=float(maxAralik), size=pop_size)
    
    for generation in range(num_generations):
        print("Generation : ", generation)
        # Popülasyondaki her kromozom için uygunluk değerini hesapla
        fitness = GA.cal_pop_fitness(equation_inputs, new_population)
        #eşleşme havuzundaki en iyi bireylerin seçimi
        parents = GA.select_mating_pool(new_population, fitness, num_parents_mating)
        
        #Çaprazlama ile yeni birey üretimi
        offspring_crossover = GA.crossover(parents,
                                           offspring_size=(pop_size[0]-parents.shape[0], num_weights))
        #Mutasyon uygulanması
        offspring_mutation = GA.mutation(offspring_crossover)
        
        #Yeni popülasyon oluşturulması
        new_population[0:parents.shape[0], :] = parents
        new_population[parents.shape[0]:, :] = offspring_mutation
        
        #Geçerli iterasyondaki en iyi sonuç
        print("Best result : ", numpy.max(numpy.sum(new_population*equation_inputs, axis=1)))
        #Tüm nesilleri bitirmeyi yineledikten sonra en iyi çözümü elde etmek için 
        #İlk olarak, son nesildeki her bir çözüm için uygunluk hesaplanır.
        fitness = GA.cal_pop_fitness(equation_inputs, new_population)
        
        #Ardından, bu çözümün en iyi uygunluğa karşılık gelen indeksini döndürün.
        best_match_idx = numpy.where(fitness == numpy.max(fitness))
        print("Best solution : ", new_population[best_match_idx, :])
        print("Best solution fitness : ", fitness[best_match_idx])
        ui.tableWidget.setRowCount(generation+1)
        ui.tableWidget.setItem(generation, 0, QTableWidgetItem(str(generation+1)))
        ui.tableWidget.setItem(generation, 1, QTableWidgetItem(str(numpy.max(numpy.sum(new_population*equation_inputs, axis=1)))))
        ui.tableWidget.setItem(generation, 2, QTableWidgetItem(str(new_population[best_match_idx, :])))
        ui.tableWidget.setItem(generation, 3, QTableWidgetItem(str(fitness[best_match_idx])))
  
    
ui.HesaplaButon.clicked.connect(EKLE)
sys.exit(Uygulama.exec_())





