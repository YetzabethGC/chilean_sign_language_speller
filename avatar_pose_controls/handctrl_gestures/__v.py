import bpy

import sys
sys.path.append("/home/vpoblete/yetzabethg/New Folder/") #DIRECTORIO CON CÓDIGOS DE CONTROL
import handctrl as hc 

#####CONTROL DE LAS MANOS######

#Mano derecha
hc.hRH(3)           #ALTURA(0= REPOSO, 1=ESTOMAGO, 2=PECHO, 3=CUELLO, 4=CARA, 5=CABEZA)
hc.dRH(0)           #DISTANCIA HORIZONTAL AL CUERPO RESPECTO A PUNTO ANTERIOR(0= CENTRO, 1= ALEJADO)
hc.rhF(6,0,0,6,6)   #CONTROL DEDOS(1=PULGAR, 2=INDICE, 3=MEDIO, 4=ANULAR, 5=MEÑIQUE) VALORES DEL 0(ABIERTO) A 6(CERRADO)
hc.detRF(1,-1,1)
hc.detRF(2,0,0)
hc.detRF(3,0,0)
hc.detRF(4,0,0)
hc.detRF(5,0,0)
hc.rotRH(0,0) 