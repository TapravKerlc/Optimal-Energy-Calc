# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:28:41 2020

@author: Taprav Kerlc
"""

import matplotlib.pyplot as plt

#Uran ua je atomsko, uz pa masno
uz=92
ua=235
#Barij
baz=56
#Kripton
krz=36

#masi nevtrona in protona v MeV
massn=939.57
massp=938.27
#začetna ugodna energija, že v prvi iteraciji bo spremenjeno
minenergy = 100000000 #random velika cifra, placeholder

#izračunamo energijo urana
energyu= -15.6*ua+17.3*ua**(2/3)+0.7*uz*(uz-1)/ua**(1/3)+23.3*((ua-2*uz)**2)/ua+33.5*0 #SEMF
massu = energyu +uz*massp+(ua-uz)*massn #tista enačba za maso
print("Uran v Gev")
print(massu/1000) #deljeno s 1000 da so GeV, bolj pregledno

yos = [] #definiramo array točk za graf
xos = list(range(131, 143))

#izračunamo možne energije barija
for i in range (131, 143): #to nam pove A(tomsko) od barija, 143 namesto 142 zato ker v pythonu 3 je drugo število eksplicitno
    
    if((i-baz) % 2 == 0): #ali je sodo-sodo
        energyba = -15.6*i+17.3*i**(2/3)+0.7*baz*(baz-1)/i**(1/3)+23.3*((i-2*baz)**2)/i+33.5*(-1)/i**(3/4) #SEMF
    else:           #drugače je sodo-liho
        energyba = -15.6*i+17.3*i**(2/3)+0.7*baz*(baz-1)/i**(1/3)+23.3*((i-2*baz)**2)/i+33.5*0 #SEMF
        
    massba = energyba +baz*massp+(i-baz)*massn
    print("Barij v GeV")
    print(massba/1000) #deljeno s 1000 da so GeV, bolj pregledno
    
    kra = 235-2-i #atomsko število kriptona
    #izračunamo energijo kriptona
	if((kra) % 2 == 0): #ali je sodo-sodo
		energykr= -15.6*kra+17.3*kra**(2/3)+0.7*krz*(krz-1)/kra**(1/3)+23.3*((kra-2*krz)**2)/kra+33.5*(-1)/kra**(3/4) #SEMF
	else:           #drugače je sodo-liho
		energykr= -15.6*kra+17.3*kra**(2/3)+0.7*krz*(krz-1)/kra**(1/3)+23.3*((kra-2*krz)**2)/kra+33.5*0 #SEMF
    masskr = energykr +krz*massp+(kra-krz)*massn
    print("Kripton v GeV")
    print(masskr/1000) #deljeno s 1000 da so GeV, bolj pregledno
    
    releasedenergy = massu -massba - masskr - 2*massn
    print("sproščena energija:")
    print(releasedenergy)
    yos.append(releasedenergy) #rišemo na graf
    if(releasedenergy < minenergy): #preverimo če je bolj ugodna energija kot tista, ki smo jo prej izračunali za najbolj ugodno
        minenergy=releasedenergy
        
plt.scatter(xos,yos, color ='purple', label='Sproščena energija v MeV')
plt.legend()
plt.show() #nariši graf!
print("Ugodna sproščena energija v MeV:")
print(minenergy)