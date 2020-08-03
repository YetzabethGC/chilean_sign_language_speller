import bpy

import sys
sys.path.append("/home/vpoblete/yetzabethg/New Folder/") #DIRECTORIO CON CÓDIGOS DE CONTROL
import handctrl as hc 
   

def rotRH(t,r):  #rotacion mano derecha
    wik=bpy.context.object.pose.bones["hand.ik.R"]
    wfk=bpy.context.object.pose.bones["hand.fk.R"]
    if r==0: #rot muneca
       
        wik.rotation_quaternion[0]=wik.rotation_quaternion[0]
        wik.rotation_quaternion[1]=wik.rotation_quaternion[1]
        wik.rotation_quaternion[2]=wik.rotation_quaternion[2]
        wik.rotation_quaternion[3]=wik.rotation_quaternion[3]
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
        a=-0.4
        b=1
        c=-0.2
        bpy.ops.mhx2.snap_fk_ik(data="MhaArmIk_R 18 19 18")
        wfk.rotation_quaternion[1]=a
        wfk.rotation_quaternion[2]=b
        wfk.rotation_quaternion[3]=c
        bpy.ops.mhx2.snap_ik_fk(data="MhaArmIk_R 18 19 18")
    else:
        print('error')
        
    if t==0:
        r=0
    elif t==1:
        bpy.ops.mhx2.snap_fk_ik(data="MhaArmIk_R 18 19 18")
        wfk.rotation_quaternion[1]=1
        wfk.rotation_quaternion[3]=0.4
        bpy.ops.mhx2.snap_ik_fk(data="MhaArmIk_R 18 19 18")
                   
 
n=10
bpy.context.scene.frame_current=bpy.context.scene.frame_current
#####CONTROL DE LAS MANOS######
#Mano derecha
hc.hRH(3)           #ALTURA(0= REPOSO, 1=ESTOMAGO, 2=PECHO, 3=CUELLO, 4=CARA, 5=CABEZA)
hc.dRH(0)           #DISTANCIA HORIZONTAL AL CUERPO RESPECTO A PUNTO ANTERIOR(0= CENTRO, 1= ALEJADO)
hc.rhF(6,6,6,6,0)   #CONTROL DEDOS(1=PULGAR, 2=INDICE, 3=MEDIO, 4=ANULAR, 5=MEÑIQUE) VALORES DEL 0(ABIERTO) A 6(CERRADO)
hc.detRF(1,0,1)
hc.detRF(2,0,0)
hc.detRF(3,0,0)
hc.detRF(4,0,0)
hc.detRF(5,0,0)
rotRH(0,0)
bpy.ops.anim.keyframe_insert_menu(type='WholeCharacter')
bpy.context.scene.frame_current=bpy.context.scene.frame_current+n
rotRH(1,0)
bpy.ops.anim.keyframe_insert_menu(type='WholeCharacter')
bpy.context.scene.frame_current=bpy.context.scene.frame_current+n
rotRH(0,2)
bpy.ops.anim.keyframe_insert_menu(type='WholeCharacter') 