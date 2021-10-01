#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 08:10:00 2021

@author: LinaH
"""

def abrir_archivo(nom_archivo):
    ruta= "/Users/LinaH/Documents/GitHub/HCAD/Lab 1/Archivos/" + nom_archivo + ".txt"
    with open(ruta,"r") as archivo:
        archivo=archivo.read()
        globals()[nom_archivo]=archivo.splitlines()


for archivo in ('edad', 'genero', 'estado_civil', 'escolaridad', 'estrato', 'region', 'promedio' ):
    abrir_archivo(archivo)
    
    
    
import matplotlib.pyplot as plt



def tabla_df (nom_archivo):
    nom_archivo_un = {}
    for nombre in nom_archivo:
        if nombre in nom_archivo_un:
            nom_archivo_un[nombre]+=1 # pregunta si esta y empieza a contar
        else:
            nom_archivo_un[nombre]=1 # crea.  
    
    return nom_archivo_un

region_tbla=tabla_df (region)
print ("Región:Cantidad")
for valor in sorted (region_tbla):
    print (f'{valor}: {region_tbla[valor]}')
print ( "  ")


escolaridad_tbla=tabla_df (escolaridad)
print ("Escolaridad:Cantidad")
for valor in sorted (escolaridad_tbla):
    print (f'{valor}: {escolaridad_tbla[valor]}')
print ( "  ")

estado_civil_tbla=tabla_df (estado_civil)
print ("Estado_Civil:Cantidad")
for valor in sorted (estado_civil_tbla):
    print (f'{valor}: {estado_civil_tbla[valor]}')
print ( "  ")  


estrato_tbla=tabla_df (estrato)
print ("Estrato:Cantidad")
for valor in sorted (estrato_tbla):
    print (f'{valor}: {estrato_tbla[valor]}')   
print ( "  ")     
    
genero_tbla=tabla_df (genero)
print ("Género:Cantidad ")  
for valor in sorted (genero_tbla):
    print (f'{valor}: {genero_tbla[valor]}')
print ( "  ")  


# EDAD: 
    
import math

# Media
for i in range(0, len(edad)):
    edad[i] = int (edad[i])
    
    
media_edad = math.fsum(edad)/ len(edad)
print (media_edad)

#Mediana



# Este fue el ejemplo para poder hacer la tabla de frecuencias y ahi si poder hacer las graficas. 


region_un = {}

for nombre in region:
    if nombre in region_un:
        region_un[nombre]+=1
    else:
        region_un[nombre]=1
        
for valor in sorted (region_un):
    print (f'{valor}: {region_un[valor]}')
    

#Ahora hago los graficos con los diccionarios

# Escolaridad

import matplotlib.pyplot as plt


region = list(region_tbla.keys())
values = list(region_tbla.values())

#tick_label does the some work as plt.xticks()
plt.bar(range(len(region_tbla)),values,tick_label=region)
plt.title("REGIONES")
plt.show()


# Como enumerarlos

for i in range(0, len(edad)):
    edad[i] = int (edad[i])


edad = list(enumerate(edad))
print(edad)

edad.sort(key = lambda x: x[1])   #index 1 means second element



for i in range(0, len(promedio)):
    promedio[i] = float(promedio[i])

prt=promedio

prt = list(enumerate(prt))
#print(prt)

#prt.sort(key = lambda x: x[1],reverse=True)


etr=estrato

etr = list(enumerate(etr))

def conversion(tup, dict):
    for x, y in tup:
        dict.setdefault(x, []).append(y)
    return 

promedio_dic = {}
conversion(prt, promedio_dic)

estrato_dic = {}
conversion(etr, estrato_dic)

prueba={key: promedio_dic[key] + estrato_dic[key] for key in promedio_dic}
        
pruba_ordenada = sorted(prueba.items(), key=lambda x: x[1],reverse=True)

becados_1=[]
becados_2=[]
becados_3=[]
becados_4=[]
becados_5=[]
check=[]
num_becas =10



for i in pruba_ordenada:
    if i[1][1]=='1':
        if len(becados_1)<2:
            becados_1.append(i[0])
    if i[1][1]=='2':
        if len(becados_2)<4:
            becados_2.append(i[0])
    if i[1][1]=='3':
        if len(becados_3)<3:
            becados_3.append(i[0])
    if i[1][1]=='4':
        if len(becados_4)<1:
            becados_4.append(i[0])
    if i[1][1]=='5':
        if len(becados_5)<1:
            becados_5.append(i[0])
    check = becados_1 + becados_2 +becados_3 + becados_4 + becados_5
    if len(check) == num_becas:
        break


#Largo de los estratos:.

len_est1 = unique_list = sorted(list(dict.fromkeys(estrato)))

num_est1 = 0
num_est2 = 0
num_est3 = 0
num_est4 = 0
num_est5 = 0
 
for i in estrato:
    if i == "1":
        num_est1 +=1
    elif i == "2":
        num_est2 +=1
    elif i == "3":
        num_est3 +=1
    elif i == "4":
        num_est4 +=1       
    else:
        num_est5 +=1 
        

#parametrosa
num_becas =10     # Número de becas asignar
por_apli = 0.02   # Pocentaje asignado a cada subpoblación


# librerias
import math 



def becas_estrato(num_becas,por_apli):
 
    becados_1=[]
    becados_2=[]
    becados_3=[]
    becados_4=[]
    becados_5=[]
    check=[]
    indicadora =0
    beca_estr_1 = 0
    beca_estr_2 = 0
    beca_estr_3 = 0
    beca_estr_4 = 0
    beca_estr_5 = 0
    est1 = num_est1
    est2 = num_est2
    est3 = num_est3
    est4 = num_est4
    est5 = num_est5
    
    num_becas
    
    while num_becas>len(check):
    
        beca_estr_1 = math.floor(est1*por_apli) + beca_estr_1
        beca_estr_2 = math.floor(est2*por_apli) + beca_estr_2
        beca_estr_3 = math.floor(est3*por_apli) + beca_estr_3
        beca_estr_4 = math.floor(est4*por_apli) + beca_estr_4
        beca_estr_5 = math.floor(est5*por_apli) + beca_estr_5
            
        for i in pruba_ordenada:
            check = becados_1 + becados_2 +becados_3 + becados_4 + becados_5
            if i[1][1]=='1':
                if len (becados_1)<beca_estr_1 and len(check) < num_becas and i[0] not in check:
                    becados_1.append(i[0])
                    est1 -=1
                else:
                    break
        
        for i in pruba_ordenada:
            check = becados_1 + becados_2 +becados_3 + becados_4 + becados_5
            if i[1][1]=='2':
                if len (becados_2)<beca_estr_2 and len(check) < num_becas and i[0] not in check:
                    becados_2.append(i[0])
                    est2 -=1
                else:
                    break
            
        for i in pruba_ordenada:
            check = becados_1 + becados_2 +becados_3 + becados_4 + becados_5
            if i[1][1]=='3':
                if len (becados_3)<beca_estr_3 and len(check) < num_becas and i[0] not in check:
                    becados_3.append(i[0])
                    est3 -=1
                else:
                    break        
        
        for i in pruba_ordenada:
            check = becados_1 + becados_2 +becados_3 + becados_4 + becados_5
            if i[1][1]=='4':
                if len (becados_4)<beca_estr_4 and len(check) < num_becas and i[0] not in check:
                    becados_4.append(i[0])
                    est4 -=1
                else:
                    break

        for i in pruba_ordenada:
            check = becados_1 + becados_2 +becados_3 + becados_4 + becados_5
            if i[1][1]=='5':
                if len (becados_5)<beca_estr_5 and len(check) < num_becas and i[0] not in check:
                    becados_5.append(i[0])
                    est5 -=1
                else:
                    break
    return check


becas_estrato(num_becas,por_apli)
math.floor(num_est3*por_apli)
