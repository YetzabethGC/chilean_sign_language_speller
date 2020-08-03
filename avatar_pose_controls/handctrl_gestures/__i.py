import bpy

import sys
sys.path.append("/home/vpoblete/yetzabethg/New Folder/") #DIRECTORIO CON CÓDIGOS DE CONTROL
import handctrl as hc 

#####CONTROL DE LAS MANOS######

#Mano izquierda
hc.hLH(0)           #ALTURA(0= REPOSO, 1=ESTOMAGO, 2=PECHO, 3=CUELLO, 4=CARA, 5=CABEZA)
hc.dLH(0)           #DISTANCIA AL CUERPO(0= CENTRO, 1= ALEJADO)
hc.lhF(0,0,0,0,0)   #CONTROL DEDOS(1=PULGAR, 2=INDICE, 3=MEDIO, 4=ANULAR, 5=MEÑIQUE) VALORES DEL 0(ABIERTO) A 6(CERRADO)

       

#####CONTROL DE LAS MANOS######
#Mano derecha
hc.hRH(3)           #ALTURA(0= REPOSO, 1=ESTOMAGO, 2=PECHO, 3=CUELLO, 4=CARA, 5=CABEZA)
hc.dRH(0)           #DISTANCIA AL CUERPO(0= CENTRO, 1= ALEJADO, 2= CONTRARIO)
hc.rhF(6,6,6,6,0)   #CONTROL DEDOS(1=PULGAR, 2=INDICE, 3=MEDIO, 4=ANULAR, 5=MEÑIQUE) VALORES DEL 0(ABIERTO) A 6(CERRADO)
hc.detRF(2,0,0)
hc.detRF(1,0,0)
hc.rotRH(0,0)
