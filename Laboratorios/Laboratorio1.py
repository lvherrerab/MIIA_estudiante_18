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



#Largo de los estratos:.


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
    
    
    
    while len(check)<num_becas:
    
        beca_estr_1 = math.floor(est1*por_apli) + beca_estr_1
        beca_estr_2 = math.floor(est2*por_apli) + beca_estr_2
        beca_estr_3 = math.floor(est3*por_apli) + beca_estr_3
        beca_estr_4 = math.floor(est4*por_apli) + beca_estr_4
        beca_estr_5 = math.floor(est5*por_apli) + beca_estr_5
        
        
        for i in pruba_ordenada:
            check = becados_1 + becados_2 +becados_3 + becados_4 + becados_5
            if i[1][1]=='1':
                if i[0] in check:
                    continue
                if len(becados_1)<beca_estr_1 and len(check) < num_becas:
                    becados_1.append(i[0])
                    est1 -=1
                else:
                    break
        
        for i in pruba_ordenada:
            check = becados_1 + becados_2 +becados_3 + becados_4 + becados_5
            if i[1][1]=='2':
                if i[0] in check:
                    continue
                if len(becados_2)<beca_estr_2 and len(check) < num_becas:
                    becados_2.append(i[0])
                    est2 -=1
                else:
                    break
            
        for i in pruba_ordenada:
            check = becados_1 + becados_2 +becados_3 + becados_4 + becados_5
            if i[1][1]=='3':
                if i[0] in check:
                    continue
                if len(becados_3)<beca_estr_3 and len(check) < num_becas:
                    becados_3.append(i[0])
                    est3 -=1
                else:
                    break        
        
        for i in pruba_ordenada:
            check = becados_1 + becados_2 +becados_3 + becados_4 + becados_5
            if i[1][1]=='4':
                if i[0] in check:
                    continue
                if len(becados_4)<beca_estr_4 and len(check) < num_becas:
                    becados_4.append(i[0])
                    est4 -=1
                else:
                    break

        for i in pruba_ordenada:
            check = becados_1 + becados_2 +becados_3 + becados_4 + becados_5
            if i[1][1]=='5':
                if i[0] in check:
                    continue
                if len(becados_5)<beca_estr_5 and len(check) < num_becas:
                    becados_5.append(i[0])
                    est5 -=1
                else:
                    break
        check = becados_1 + becados_2 +becados_3 + becados_4 + becados_5
    return check


becas_estrato(num_becas,por_apli)
becas_estrato(40,0.03)
math.floor(num_est3*por_apli)

# El segundo grupo sugiere que los recibidores de becas deben estar igualmente distribuidos 
#entre las diferentes regiones y generos, considerando, por supuesto, que para cada una de 
#esas sub-poblaciones, las personas elegidas sean las de mejores promedios académicos.


# Toca hacerlo por pasos:
    
    # 1. Importar librerías:
        
import math 
import numpy as np

# Parametros que debo ingresar en mi función. 

becas_reg_gen(num_becas)
becas_reg_gen(200)

num_becas = 200  # Número de becas asignar

# # Poner indices al promedio, region y genero.

prt=promedio
prt = list(enumerate(prt))

reg=region
reg = list(enumerate(reg))

gen= genero
gen = list(enumerate(gen))


# Convertir tupla en diccionario

def conversion(tup, dict):
    for x, y in tup:
        dict.setdefault(x, []).append(y)
    return 

promedio_dic = {}
conversion(prt, promedio_dic)

region_dic = {}
conversion(reg, region_dic)

genero_dic = {}
conversion(gen, genero_dic)


dic_prom_reg_gen={key: promedio_dic[key] + region_dic[key]+ genero_dic [key] for key in promedio_dic}
     
# Aqui lo organizo el promedio de manera descendente. 
dic_prom_reg_gen_ord = sorted(dic_prom_reg_gen.items(), key=lambda x: x[1],reverse=True)

# calcular total de grupos.

Total_grupos= len(np.unique(genero)) * len(np.unique(region))

# Calcular número de becas por cada grupo

becas_grupo=  num_becas/Total_grupos

#Conteo de personas por grupo


andina_femenino= 0
andina_masculino=0
andina_nobinario=0
andina_otro=0
pacifica_femenino=0
pacifica_masculino=0
pacifico_nobinario=0
pacifica_otro=0
orinoquia_femenino=0
orinoquia_masculino=0
orinoquia_nobinario=0
orinoquia_otro=0
caribe_femenino=0
caribe_masculino=0
caribe_nobinario=0
caribe_otro=0
amazonia_femenino=0
amazonia_masculino=0
amazonia_nobinario=0
amazonia_otro=0


for i in dic_prom_reg_gen_ord: 
    if i[1][1]=="Andina" and i[1][2]=="femenino":
        andina_femenino+=1
    elif i[1][1]=="Andina" and i[1][2]=="masculino":
        andina_masculino+=1
    elif i[1][1]=="Andina" and i[1][2]=="no binario":
        andina_nobinario+=1    
    elif i[1][1]=="Andina" and i[1][2]=="otro":
        andina_otro+=1   
    elif i[1][1]=="Pacifica" and i[1][2]=="femenino":
        pacifica_femenino+=1
    elif i[1][1]=="Pacifica" and i[1][2]=="masculino":
        pacifica_masculino+=1
    elif i[1][1]=="Pacifica" and i[1][2]=="no binario":
        pacifico_nobinario+=1    
    elif i[1][1]=="Pacifica" and i[1][2]=="otro":
        pacifica_otro+=1  
    elif i[1][1]=="Orinoquia" and i[1][2]=="femenino":
        orinoquia_femenino+=1
    elif i[1][1]=="Orinoquia" and i[1][2]=="masculino":
        orinoquia_masculino+=1
    elif i[1][1]=="Orinoquia" and i[1][2]=="no binario":
        orinoquia_nobinario+=1    
    elif i[1][1]=="Orinoquia" and i[1][2]=="otro":
        orinoquia_otro+=1 
    elif i[1][1]=="Caribe" and i[1][2]=="femenino":
        caribe_femenino+=1
    elif i[1][1]=="Caribe" and i[1][2]=="masculino":
        caribe_masculino+=1
    elif i[1][1]=="Caribe" and i[1][2]=="no binario":
        caribe_nobinario+=1    
    elif i[1][1]=="Caribe" and i[1][2]=="otro":
        caribe_otro+=1 
    elif i[1][1]=="Amazonia" and i[1][2]=="femenino":
        amazonia_femenino+=1
    elif i[1][1]=="Amazonia" and i[1][2]=="masculino":
        amazonia_masculino+=1
    elif i[1][1]=="Amazonia" and i[1][2]=="no binario":
        amazonia_nobinario+=1    
    elif i[1][1]=="Amazonia" and i[1][2]=="otro":
        amazonia_otro+=1 

check=[]

    
becas_andina_femenino =[]
becas_andina_masculino=[]
becas_andina_nobinario=[]
becas_andina_otro=[]
becas_pacifica_femenino=[]
becas_pacifica_masculino=[]
becas_pacifico_nobinario=[]
becas_pacifica_otro=[]
becas_orinoquia_femenino=[]
becas_orinoquia_masculino=[]
becas_orinoquia_nobinario=[]
becas_orinoquia_otro=[]
becas_caribe_femenino=[]
becas_caribe_masculino=[]
becas_caribe_nobinario=[]
becas_caribe_otro=[]
becas_amazonia_femenino=[]
becas_amazonia_masculino=[]
becas_amazonia_nobinario=[]
becas_amazonia_otro=[]
andina_fem=0
andina_mas=0
andina_no=0
andina_otr=0
pacifica_fem=0
pacifica_mas=0
pacifica_no=0
pacifica_otr=0
orinoquia_fem=0
orinoquia_mas=0
orinoquia_no=0
orinoquia_otr=0
caribe_fem=0
caribe_mas=0
caribe_no=0
caribe_otr=0
amazonia_fem=0
amazonia_mas=0
amazonia_no=0
amazonia_otr=0
     
        
# Región Andina


        for i in dic_prom_reg_gen_ord:
            if andina_femenino>=becas_grupo and andina_fem<becas_grupo:
                if i[1][1]=="Andina" and i[1][2]=="femenino":
                    if i[0] in check: 
                            continue
                    if len (becas_andina_femenino)<becas_grupo and len(check)<num_becas:
                                becas_andina_femenino.append(i[0])
                                andina_fem+=1 # mover arriba aca
                    else:
                        break
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro
            
        
        for i in dic_prom_reg_gen_ord:
            if andina_masculino>=becas_grupo and andina_mas<becas_grupo:
                if i[1][1]=="Andina" and i[1][2]=="masculino":
                    if i[0] in check: 
                        continue
                if len (becas_andina_masculino)<becas_grupo and len(check)<num_becas:
                            becas_andina_masculino.append(i[0])  # aqui mirar indices    
                            andina_mas+=1
                else:
                    break
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro
            
    
        for i in dic_prom_reg_gen_ord:
            if andina_nobinario>=becas_grupo and andina_no<becas_grupo:
                if i[1][1]=="Andina" and i[1][2]=="nobinario":
                    if i[0] in check: 
                        continue
                if len (becas_andina_nobinario)<becas_grupo and len(check)<num_becas:
                            becas_andina_nobinario.append(i[0])
                            andina_no+=1
                else:
                    break
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro       
        
        for i in dic_prom_reg_gen_ord:
            if andina_otro>=becas_grupo and andina_otr<becas_grupo:
                if i[1][1]=="Andina" and i[1][2]=="otro":
                    if i[0] in check: 
                        continue
                if len (becas_andina_otro)<becas_grupo and len(check)<num_becas:
                            becas_andina_otro.append(i[0])  
                            andina_otr+=1
                else:
                    break
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro

# Región Pacifico

        for i in dic_prom_reg_gen_ord:
            if pacifica_femenino>=becas_grupo and pacifica_fem< becas_grupo:
                if i[1][1]=="Pacifica" and i[1][2]=="femenino":
                    if i[0] in check: 
                        continue
                if len (becas_pacifica_femenino)<becas_grupo and len(check)<num_becas:
                            becas_pacifica_femenino.append(i[0])
                            pacifica_fem+=1
                else:
                    break
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro
        
        for i in dic_prom_reg_gen_ord:
            if pacifica_masculino>=becas_grupo and pacifica_mas<becas_grupo:
                if i[1][1]=="Pacifica" and i[1][2]=="masculino":
                    if i[0] in check: 
                        continue
                if len (becas_pacifica_masculino)<becas_grupo and len(check)<num_becas:
                            becas_pacifica_masculino.append(i[0])
                            pacifica_mas+=1
                else:
                    break  
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro   
        
        for i in dic_prom_reg_gen_ord:
            if pacifico_nobinario>=becas_grupo and pacifica_no<becas_grupo:
                if i[1][1]=="Pacifica" and i[1][2]=="nobinario":
                    if i[0] in check: 
                        continue
                if len (becas_pacifico_nobinario)<becas_grupo and len(check)<num_becas:
                            becas_pacifico_nobinario.append(i[0])
                            pacifica_no +=1               
                else:
                    break   
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro
       
        for i in dic_prom_reg_gen_ord:
            if pacifica_otro>=becas_grupo and pacifica_otr<becas_grupo:
                if i[1][1]=="Pacifica" and i[1][2]=="otro":
                    if i[0] in check: 
                        continue
                if len (becas_pacifica_otro)<becas_grupo and len(check)<num_becas:
                            becas_pacifica_otro.append(i[0])
                            pacifica_otr+=1
                else:
                    break   
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro

# Región orinoquia

        for i in dic_prom_reg_gen_ord:
            if orinoquia_femenino>=becas_grupo and orinoquia_fem<becas_grupo:
                if i[1][1]=="Orinoquia" and i[1][2]=="femenino":
                    if i[0] in check: 
                        continue
                if len (becas_orinoquia_femenino)<becas_grupo and len(check)<num_becas:
                            becas_orinoquia_femenino.append(i[0])  
                            orinoquia_fem +=1
                else:
                    break
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro
                
        for i in dic_prom_reg_gen_ord:
            if orinoquia_masculino>=becas_grupo and orinoquia_mas<becas_grupo:
                if i[1][1]=="Orinoquia" and i[1][2]=="masculino":
                    if i[0] in check: 
                        continue
                if len (becas_orinoquia_masculino)<becas_grupo and len(check)<num_becas:
                            becas_orinoquia_masculino.append(i[0])
                            orinoquia_mas+=1
                else:
                    break
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro
        
        for i in dic_prom_reg_gen_ord:
            if orinoquia_nobinario>=becas_grupo and orinoquia_no<becas_grupo:
                if i[1][1]=="Orinoquia" and i[1][2]=="nobinario":
                    if i[0] in check: 
                        continue
                if len (becas_orinoquia_nobinario)<becas_grupo and len(check)<num_becas:
                            becas_orinoquia_nobinario.append(i[0])  # aqui mirar indices  
                            orinoquia_no +=1
                else:
                    break
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro    
        
        for i in dic_prom_reg_gen_ord:
            if orinoquia_otro>=becas_grupo and orinoquia_otr<becas_grupo:
                if i[1][1]=="Orinoquia" and i[1][2]=="otro":
                    if i[0] in check: 
                        continue
                if len (becas_orinoquia_otro)<becas_grupo and len(check)<num_becas:
                            becas_orinoquia_otro.append(i[0]) 
                            orinoquia_otr +=1
                else:
                    break
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro  

# Región Caribe

        for i in dic_prom_reg_gen_ord:
            if caribe_femenino>=becas_grupo and caribe_fem<becas_grupo:
                if i[1][1]=="Caribe" and i[1][2]=="femenino":
                    if i[0] in check: 
                        continue
                if len (becas_caribe_femenino)<becas_grupo and len(check)<num_becas:
                            becas_caribe_femenino.append(i[0])  # aqui mirar indices
                            caribe_fem+=1
                else:
                    break
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro
       
        
       
        for i in dic_prom_reg_gen_ord:
            if caribe_masculino>=becas_grupo and caribe_mas<becas_grupo:
                if i[1][1]=="Caribe" and i[1][2]=="masculino":
                    if i[0] in check: 
                        continue
                if len (becas_caribe_masculino)<becas_grupo and len(check)<num_becas:
                            becas_caribe_masculino.append(i[0])  # aqui mirar indices  
                            caribe_mas+=1
                else:
                    break
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro   
       
        
        for i in dic_prom_reg_gen_ord:
           if caribe_nobinario>=becas_grupo and caribe_no<becas_grupo:
                if i[1][1]=="Caribe" and i[1][2]=="nobinario":
                    if i[0] in check: 
                        continue
                if len (becas_caribe_nobinario)<becas_grupo and len(check)<num_becas:
                            becas_caribe_nobinario.append(i[0])  # aqui mirar indices  
                            caribe_no+=1          
                else:
                    break       
                check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro

        for i in dic_prom_reg_gen_ord:
            if caribe_otro>=becas_grupo and caribe_otr<becas_grupo:
                if i[1][1]=="Caribe" and i[1][2]=="otro":
                    if i[0] in check: 
                        continue
                if len (becas_caribe_otro)<becas_grupo and len(check)<num_becas:
                            becas_caribe_otro.append(i[0])  # aqui mirar indices  
                            caribe_otr+=1
                else:
                    break    
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro

# Región Amazonia

        for i in dic_prom_reg_gen_ord:
            if amazonia_femenino>=becas_grupo and amazonia_fem<becas_grupo:
                if i[1][1]=="Amazonia" and i[1][2]=="femenino":
                    if i[0] in check: 
                        continue
                if len (becas_amazonia_femenino)<becas_grupo and len(check)<num_becas:
                            becas_amazonia_femenino.append(i[0])  # aqui mirar indices   
                            amazonia_fem+=1
                else:
                    break
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro
        
        for i in dic_prom_reg_gen_ord:
            if amazonia_masculino>=becas_grupo and amazonia_mas<becas_grupo:
                if i[1][1]=="Amazonia" and i[1][2]=="masculino":
                    if i[0] in check: 
                        continue
                if len (becas_amazonia_masculino)<becas_grupo and len(check)<num_becas:
                            becas_amazonia_masculino.append(i[0]) 
                            amazonia_mas+=1    
                else:
                    break
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro
                
        for i in dic_prom_reg_gen_ord:
            if amazonia_nobinario>=becas_grupo and amazonia_no<becas_grupo:
                if i[1][1]=="Amazonia" and i[1][2]=="nobinario":
                    if i[0] in check: 
                        continue
                if len (becas_amazonia_nobinario)<becas_grupo and len(check)<num_becas:
                            becas_amazonia_nobinario.append(i[0])  # aqui mirar indices   
                            amazonia_no+=1
                else:
                    break
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro
                
        for i in dic_prom_reg_gen_ord:
            if amazonia_otro>=becas_grupo and amazonia_otr<becas_grupo:
                if i[1][1]=="Amazonia" and i[1][2]=="otro":
                    if i[0] in check: 
                        continue
                if len (becas_amazonia_otro)<becas_grupo and len(check)<num_becas:
                            becas_amazonia_otro.append(i[0])  # aqui mirar indices
                            amazonia_otr+=1
                else:
                    break
            else:
                break
            check = becas_andina_femenino + becas_andina_masculino + becas_andina_nobinario+becas_andina_otro+becas_pacifica_femenino+becas_pacifica_masculino+ becas_pacifico_nobinario+becas_pacifica_otro+becas_orinoquia_femenino+becas_orinoquia_masculino+becas_orinoquia_nobinario+becas_orinoquia_otro+becas_caribe_femenino+becas_caribe_masculino+becas_caribe_nobinario+becas_caribe_otro+becas_amazonia_femenino+becas_amazonia_masculino+becas_amazonia_nobinario+becas_amazonia_otro



############################################

#Se debe poder elegir el rango de edad de los aspirantes.
# proporción de las becas se asigna a cada género, a cada estrato, o a cada región
# # Poner indices a todas las variables

prt=promedio
prt = list(enumerate(prt))

reg=region
reg = list(enumerate(reg))

gen= genero
gen = list(enumerate(gen))

estr= estrato
estr= list(enumerate(estr))

eda=edad
eda= list(enumerate(eda))


# Convertir tupla en diccionario

def conversion(tup, dict):
    for x, y in tup:
        dict.setdefault(x, []).append(y)
    return 

promedio_dic = {}
conversion(prt, promedio_dic)

region_dic = {}
conversion(reg, region_dic)

genero_dic = {}
conversion(gen, genero_dic)

edad_dic = {}
conversion(eda, edad_dic)

estrato_dic = {}
conversion(estr, estrato_dic)

dic_prom_reg_gen_edad={key: promedio_dic[key] + region_dic[key]+ genero_dic [key] + edad_dic [key] + estrato_dic [key] for key in promedio_dic}
     
# Aqui lo organizo el promedio de manera descendente. 
dic_prom_reg_gen_edad_ord = sorted(dic_prom_reg_gen_edad.items(), key=lambda x: x[1],reverse=True)

# Hacer el conteo de personas por genero, región y estrato

# Estrato:
        
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
# Resgión




#Genero




lim_inf_edad= 20
lim_sup_edad= 40
num_becas=100
porc_apl=0.05




def politica (num_becas,lim_inf_edad,lim_sup_edad,porc_apl,variable_asi):
    
    
    #crear una tupla solo con las personas en ese rango. 
            
    filtrado = [] # la lista que contendrá los elementos filtrados

    for elemento in dic_prom_reg_gen_edad_ord:
        if int(elemento[1][3])>=lim_inf_edad and int(elemento[1][3])<=lim_sup_edad:
            filtrado.append(elemento)
    
    
    if variable_asi == "region":
        
    
        
        # Primero haga un conteo de el número de personas en cada región. 
        
        num_amazonia = 0
        num_pacifico = 0
        num_orinoquia = 0
        num_caribe = 0
        num_andina = 0
     
    
        for i in filtrado:
            if i[1][1] == "Amazonia":
                num_amazonia +=1
            elif i[1][1] == "Pacifica":
                num_pacifico +=1
            elif i[1][1] == "Orinoquia":
                num_orinoquia +=1
            elif i[1][1] == "Caribe":
                num_caribe +=1       
            else:
                num_andina +=1 
        
        becados_amazonia=[]
        becados_pacifica=[]
        becados_orinoquia=[]
        becados_caribe=[]
        becados_andina=[]
        check=[]
        beca_amazonia = 0
        beca_pacifica = 0
        beca_orinoquia = 0
        beca_caribe = 0
        beca_andina = 0
        amazonia = num_amazonia
        pacifico = num_pacifico
        orinoquia = num_orinoquia
        caribe = num_caribe
        andina = num_andina
            
        while len(check)<num_becas: # mIENTRAS LA LISTA DE CHEQUEO ES MENOR A NUM DE BECAS ENTRE,  SI NO TERMINE
        
            beca_amazonia = math.floor(amazonia*porc_apl) + beca_amazonia
            beca_pacifica = math.floor(pacifico*porc_apl) + beca_pacifica
            beca_orinoquia = math.floor(orinoquia*porc_apl) + beca_orinoquia
            beca_caribe = math.floor(caribe*porc_apl) + beca_caribe
            beca_andina = math.floor(andina*porc_apl) + beca_andina
            
            
            for i in filtrado:
                check = becados_amazonia + becados_pacifica +becados_orinoquia + becados_caribe + becados_andina
                if i[1][1]=='Amazonia':
                    if i[0] in check: # No tener en cuenta los asignados de las rondas anteriores. 
                        continue
                    if len(becados_amazonia)<beca_amazonia and len(check) < num_becas:
                        becados_amazonia.append(i[0])
                        amazonia -=1
                    else:
                        break
    
            for i in filtrado:
                check = becados_amazonia + becados_pacifica +becados_orinoquia + becados_caribe + becados_andina
                if i[1][1]=='Pacifica':
                    if i[0] in check: # No tener en cuenta los asignados de las rondas anteriores. 
                        continue
                    if len(becados_pacifica)<beca_pacifica and len(check) < num_becas:
                        becados_pacifica.append(i[0])
                        pacifico -=1
                    else:
                        break
    
            for i in filtrado:
                check = becados_amazonia + becados_pacifica +becados_orinoquia + becados_caribe + becados_andina
                if i[1][1]=='Orinoquia':
                    if i[0] in check: # No tener en cuenta los asignados de las rondas anteriores. 
                        continue
                    if len(becados_orinoquia)<beca_orinoquia and len(check) < num_becas:
                        becados_orinoquia.append(i[0])
                        orinoquia -=1
                    else:
                        break
    
            for i in filtrado:
                check = becados_amazonia + becados_pacifica +becados_orinoquia + becados_caribe + becados_andina
                if i[1][1]=='Caribe':
                    if i[0] in check: # No tener en cuenta los asignados de las rondas anteriores. 
                        continue
                    if len(becados_caribe)<beca_caribe and len(check) < num_becas:
                        becados_caribe.append(i[0])
                        caribe -=1
                    else:
                        break
                    
    
            for i in filtrado:
                check = becados_amazonia + becados_pacifica +becados_orinoquia + becados_caribe + becados_andina
                if i[1][1]=='Andina':
                    if i[0] in check: # No tener en cuenta los asignados de las rondas anteriores. 
                        continue
                    if len(becados_andina)<beca_andina and len(check) < num_becas:
                        becados_andina.append(i[0])
                        andina -=1
                    else:
                        break
            
            check = becados_amazonia + becados_pacifica +becados_orinoquia + becados_caribe + becados_andina  
    elif variable_asi == "genero":
        
    
        
        # Primero haga un conteo de el número de personas en cada región. 
        
        num_femenino = 0
        num_masculino = 0
        num_nobinario = 0
        num_otro = 0
     
    
        for i in filtrado:
            if i[1][2] == "femenino":
                num_femenino +=1
            elif i[1][2] == "masculino":
                num_masculino +=1
            elif i[1][2] == "no binario":
                num_nobinario +=1  
            else:
                num_otro +=1 
        
        becados_femenino=[]
        becados_masculino=[]
        becados_nobinario=[]
        becados_otro=[]
        check=[]
        beca_femenino = 0
        beca_masculino = 0
        beca_nobinario = 0
        beca_otro = 0
        femenino = num_femenino
        masculino = num_masculino
        nobinario = num_nobinario
        otro = num_otro
        
            
        while len(check)<num_becas: # mIENTRAS LA LISTA DE CHEQUEO ES MENOR A NUM DE BECAS ENTRE,  SI NO TERMINE
        
            beca_femenino = math.floor(femenino*porc_apl) + beca_femenino
            beca_masculino = math.floor(masculino*porc_apl) + beca_masculino
            beca_nobinario = math.floor(nobinario*porc_apl) + beca_nobinario
            beca_otro = math.floor(otro*porc_apl) + beca_otro
           
            
            for i in filtrado:
                check = becados_femenino + becados_masculino +becados_nobinario + becados_otro
                if i[1][2]=='femenino':
                    if i[0] in check: # No tener en cuenta los asignados de las rondas anteriores. 
                        continue
                    if len(becados_femenino)<beca_femenino and len(check) < num_becas:
                        becados_femenino.append(i[0])
                        femenino -=1
                    else:
                        break
    
            for i in filtrado:
                check = becados_femenino + becados_masculino +becados_nobinario + becados_otro
                if i[1][2]=='masculino':
                    if i[0] in check: # No tener en cuenta los asignados de las rondas anteriores. 
                        continue
                    if len(becados_masculino)<beca_masculino and len(check) < num_becas:
                        becados_masculino.append(i[0])
                        masculino -=1
                    else:
                        break
    
            for i in filtrado:
                check = becados_femenino + becados_masculino +becados_nobinario + becados_otro
                if i[1][2]=='no binario':
                    if i[0] in check: # No tener en cuenta los asignados de las rondas anteriores. 
                        continue
                    if len(becados_nobinario)<beca_nobinario and len(check) < num_becas:
                        becados_nobinario.append(i[0])
                        nobinario -=1
                    else:
                        break
    
            for i in filtrado:
                check = becados_femenino + becados_masculino +becados_nobinario + becados_otro
                if i[1][2]=='otro':
                    if i[0] in check: # No tener en cuenta los asignados de las rondas anteriores. 
                        continue
                    if len(becados_otro)<beca_otro and len(check) < num_becas:
                        becados_otro.append(i[0])
                        otro-=1
                    else:
                        break
                    
            check = becados_femenino + becados_masculino +becados_nobinario + becados_otro
    return check

print (check)
  

    else:
        
    num_est1 = 0
    num_est2 = 0
    num_est3 = 0
    num_est4 = 0
    num_est5 = 0
     
    for i in filtrado:
        if i[1][2] == "femenino":
                num_femenino +=1
            elif i[1][2] == "masculino":
                num_masculino +=1
            elif i[1][2] == "no binario":
                num_nobinario +=1  
            else:
                num_otro +=1  
