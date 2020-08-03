import bpy

import sys
sys.path.append("/home/vpoblete/yetzabethg/New Folder/") #DIRECTORIO CON CÓDIGOS DE CONTROL
import handctrl as hc 

def detRF(f,m,r): #mov dedos especificos
   
    y1='thumb.01.R'
    y2='f_index.01.R'
    y3='f_middle.01.R'
    y4='f_ring.01.R'
    y5='f_pinky.01.R'
           
    if f==0:
        m=0
        r=0  
    elif f==1:
        d=bpy.context.object.pose.bones[y1]
    elif f==2:
        d=bpy.context.object.pose.bones[y2]
    elif f==3:
        d=bpy.context.object.pose.bones[y3]
    elif f==4:
        d=bpy.context.object.pose.bones[y4]
    elif f==5:
        d=bpy.context.object.pose.bones[y5]
    else:
        print ('error')
                          
    ##EXTENSIoN DE LA MANO
    if m==0:
        mov=0
    elif m==1:   #alejar el dedo
         mov= -0.1 
    elif m==-1:  #acercar el dedo
        mov= 0.1
        if f==1 or f==5:
            mov=0.2
        elif f==4:
            mov=0.03    
    else:
        print('error')   
    if f>0 and f<=2:
        d.rotation_quaternion[3]=mov
    elif f>3 and f<=5:
        d.rotation_quaternion[3]=-mov          
    else:
        print ('error')
        
 ##ANGULO DE LA MANO
    if r==1:
        if f==1:
            d.rotation_quaternion[1]=0.4
        else:
             d.rotation_quaternion[1]=0.7
    elif r==0:
          d.rotation_quaternion[1]=0       
           
        

def rotRH(t,r):  #rotacion mano derecha
    wik=bpy.context.object.pose.bones["hand.ik.R"]
    wfk=bpy.context.object.pose.bones["hand.fk.R"]
    if r==0: #rot muneca
       
        wik.rotation_quaternion[0]=wik.rotation_quaternion[0]
        wik.rotation_quaternion[1]=wik.rotation_quaternion[1]
        wik.rotation_quaternion[2]=wik.rotation_quaternion[2]
        wik.rotation_quaternion[3]=wik.rotation_quaternion[3]
    elif r==-1:
        a=2
        b=0.05
        if wik.location[2]<0.1 and wik.location[2]>=0.05:
            a=9
            b=-4
        if wik.location[2]<0.05:
            a=9
            b=-2
        bpy.ops.mhx2.snap_fk_ik(data="MhaArmIk_R 18 19 18")
        wfk.rotation_quaternion[0]=a
        wfk.rotation_quaternion[1]=b
        bpy.ops.mhx2.snap_ik_fk(data="MhaArmIk_R 18 19 18")
       
    elif r==1:
        a=2
        b=0.05
        if wik.location[2]<0.1 and wik.location[2]>=0.05:
            a=4
            b=1
        if wik.location[2]<0.05:
            a=9
            b=-2
        bpy.ops.mhx2.snap_fk_ik(data="MhaArmIk_R 18 19 18")
        wfk.rotation_quaternion[0]=a
        wfk.rotation_quaternion[1]=b
        bpy.ops.mhx2.snap_ik_fk(data="MhaArmIk_R 18 19 18")
    elif r==2:
        a=0
        b=1
        bpy.ops.mhx2.snap_fk_ik(data="MhaArmIk_R 18 19 18")
        wfk.rotation_quaternion[1]=a
        wfk.rotation_quaternion[2]=b
        bpy.ops.mhx2.snap_ik_fk(data="MhaArmIk_R 18 19 18")
    else:
        print('error')
        
    if t==0:
        r=0
    elif t==-1:
        bpy.ops.mhx2.snap_fk_ik(data="MhaArmIk_R 18 19 18")
        wfk.rotation_quaternion[1]=0
        wfk.rotation_quaternion[3]=0.9
        bpy.ops.mhx2.snap_ik_fk(data="MhaArmIk_R 18 19 18")    
    elif t==1:
        bpy.ops.mhx2.snap_fk_ik(data="MhaArmIk_R 18 19 18")
        wfk.rotation_quaternion[1]=1
        wfk.rotation_quaternion[3]=0.5
        bpy.ops.mhx2.snap_ik_fk(data="MhaArmIk_R 18 19 18")
                   
 
#####CONTROL DE LAS MANOS######

#Mano derecha
hc.hRH(3)           #ALTURA(0= REPOSO, 1=ESTOMAGO, 2=PECHO, 3=CUELLO, 4=CARA, 5=CABEZA)
hc.dRH(1)           #DISTANCIA HORIZONTAL AL CUERPO RESPECTO A PUNTO ANTERIOR(0= CENTRO, 1= ALEJADO)
hc.rhF(0,4,5,5,5)   #CONTROL DEDOS(1=PULGAR, 2=INDICE, 3=MEDIO, 4=ANULAR, 5=MEÑIQUE) VALORES DEL 0(ABIERTO) A 6(CERRADO)
detRF(1,1,1)
detRF(2,-1,0)
detRF(4,-1,0)
detRF(5,-1,0)
rotRH(-1,0) 