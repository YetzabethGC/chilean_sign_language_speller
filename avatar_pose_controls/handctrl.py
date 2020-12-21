# -*- coding: utf-8 -*-

import bpy

def hRH(pos): #height RIGHT HAND
    h=bpy.data.objects['3'].pose.bones['hand.ik.R']
    c=bpy.data.objects['3'].pose.bones['elbow.pt.ik.R']
    cl=bpy.data.objects['3'].pose.bones['clavicle.R']
    crh=(0,-0.2,0) #elbow initial position
    clp=(1,0,0.1,0.05) #clavicle initial position
    if pos ==0: #IDLE
        hrh= (0.18,-0.04, 0.32) 
        rrh=(0.834,0.38,-0.2,-0.3)
    elif pos==1:#STOMACH
        hrh=(0.25, -0.067, 0.22)
        rrh=(0.12,-0.1,-0.02,-0.2)
    elif pos==2:#CHEST
        hrh=(0.23, -0.16, 0.19)
        rrh=(0.595,-0.5,-0.013,-0.5)
    elif pos==3:#NECK
        hrh =(0.39, -0.2, 0.08)
        rrh=(0.5,-0.62,-0.055,-0.6)
    elif pos==4:#FACE
        hrh=(0.51, -0.26, 0.04)
        rrh=(0.476,-0.621,-0,-0.6)
        clp=(0.96,0.25,0,0.1)
        crh=(0.16,-0.11,0.44)
    elif pos==5:#HEAD+
        hrh= (0.59, -0.4, -0.02) 
        rrh=(0.38,-0.71,-0.226,-0.54) 
        crh=(0.045,0.06,0.7)
        clp=(0.986,0.16,0.1,0.03)
    else:
        hrh= (0.18,-0.04, 0.32) 
        rrh=(0.834,0.38,-0.2,-0.3)
        print('Only numbers from 0 to 5')
    
    
    h.location=hrh
    c.location=crh
    h.rotation_quaternion=rrh
    cl.rotation_quaternion=clp

#hRH(0) #example, uncomment and run script to test




def hLH(pos): #height LEFT HAND
    h=bpy.data.objects['3'].pose.bones['hand.ik.L']
    c=bpy.data.objects['3'].pose.bones['elbow.pt.ik.L']
    cl=bpy.data.objects['3'].pose.bones['clavicle.L']
    clh=(0.02,-0.1,0) #elbow initial position
    clp=(1,0,0,0) #clavicle initial position
    if pos ==0:
        hlh= (-0.12,-0.01, 0.33) #IDLE
        rlh=(0.72,0.46,0.227,0.45)
    elif pos==1:
        hlh=(-0.218, -0.08, 0.2)#ESTOMACH
        rlh=(1.2,-0.636,0,1.19)
    elif pos==2:
        hlh=(-0.26, -0.077, 0.16)#CHEST
        rlh=(0.5,-0.5,0.034,0.56)
    elif pos==3:
        hlh =(-0.4, -0.13, 0.095)#NECK
        rlh=(0.412,-0.547,0.4,0.6)
    elif pos==4:
        hlh=(-0.47, -0.2, 0.01)#FACE
        rlh=(0.4,-0.77,0.1,0.47)
        clh=(-0.218,-0.15,-0.043)
        clp=(0.9,0.2,-0.265,-0.1)
    elif pos==5:#HEAD+
        hlh= (-0.52, -0.4, -0.01) 
        rlh=(0.48,-0.676,0.13,0.54) 
        clh=(-0.31,-0.25,0.2)
        clp=(0.965,0.1,-0.85,0.2)
    else:
        hlh= (-0.12,-0.01, 0.33) #IDLE
        rlh=(0.72,0.46,0.227,0.45)
        print ('Only numbers from 0 to 5')
    
    
    h.location=hlh
    c.location=clh
    h.rotation_quaternion=rlh
    cl.rotation_quaternion=clp

#hLH(3) #example, uncomment and run script to test


################################################################################

def dLH(pos): #distance from the body LEFT HAND
    h=bpy.data.objects['3'].pose.bones['hand.ik.L']
    e=bpy.data.objects['3'].pose.bones['elbow.pt.ik.L']
    if pos==0: #CENTER
        a=-0
        h.location[2]=h.location[2]+a
    elif pos==1: #away from body
        a=-0.15
        h.location[2]=h.location[2]+a
        h.location[0]=h.location[0]-a
    elif pos==-1: #opposite side
        a=0.15
        h.location[2]=h.location[2]+a
        h.location[0]=h.location[0]-a
        e.location=(-0.15,0.15,0.42)
    else:
    	print ('inputs are -1, 0 and 1')  

#dLH(0)  #example, uncomment and run script to test    


def dRH(pos): #distance from body RIGHT HAND
    h=bpy.data.objects['3'].pose.bones['hand.ik.R']
    if pos==0: #CENTER
        a=0
        h.location[2]=h.location[2]+a
    elif pos==1: #away from body
        a=-0.15
        h.location[2]=h.location[2]+a
        h.location[0]=h.location[0]+a
    elif pos==-1: #opposite side
        a=0.15
        h.location[2]=h.location[2]+a
        h.location[0]=h.location[0]+a
    else:
    	print ('inputs are -1, 0 and 1')  

#dRH(0)    #example, uncomment and run script to test    

#############################################################################

def rhF(x1,x2,x3,x4,x5): #finger extension control RIGHT HAND (thumb,index,middle,ring,pinky)
    a1=x1/10
    if x1>=6:
        a1=0.8
    bpy.data.objects['3'].pose.bones["thumb.R"].rotation_quaternion[1]=a1
    a2=x2/10
    bpy.data.objects['3'].pose.bones["index.R"].rotation_quaternion[1]=a2
    a3=x3/10
    if x3==6:
        a3=0.8
    bpy.data.objects['3'].pose.bones["middle.R"].rotation_quaternion[1]=a3
    a4=x4/10
    if x4==6:
        a4=0.7
    bpy.data.objects['3'].pose.bones["ring.R"].rotation_quaternion[1]=a4
    a5=x5/10
    bpy.data.objects['3'].pose.bones["pinky.R"].rotation_quaternion[1]=a5    
    
    
#rhF(0,0,0,0,0)  #example, uncomment and run script to test  

def lhF(x1,x2,x3,x4,x5): #finger extension control LEFT HAND (thumb,index,middle,ring,pink)
    a1=x1/10
    bpy.data.objects['3'].pose.bones["thumb.L"].rotation_quaternion[1]=a1
    if x1>6:
        print('only numbers between 0 and 6')
    a2=x2/10
    bpy.data.objects['3'].pose.bones["index.L"].rotation_quaternion[1]=a2
    a3=x3/10
    if x3==6:
        a3=0.7
    bpy.data.objects['3'].pose.bones["middle.L"].rotation_quaternion[1]=a3
    a4=x4/10
    if x4==6:
        a4=0.7
    bpy.data.objects['3'].pose.bones["ring.L"].rotation_quaternion[1]=a4
    a5=x5/10
    bpy.data.objects['3'].pose.bones["pinky.L"].rotation_quaternion[1]=a5    
    
    
#lhF(0,0,0,0,0) #example, uncomment and run script to test  

##################################################################

def detRF(f,m,r): #especific finger position RIGHT HAND (finger=[1=thumb...,5=pinky],separation from fingers=[-1,0,1], perpendicular to pal=[0,1])
    #which finger
    y1='thumb.01.R'
    y2='f_index.01.R'
    y3='f_middle.01.R'
    y4='f_ring.01.R'
    y5='f_pinky.01.R'
           
    if f==0:
        m=0
        r=0  
    elif f==1:
        d=bpy.data.objects['3'].pose.bones[y1]
    elif f==2:
        d=bpy.data.objects['3'].pose.bones[y2]
    elif f==3:
        d=bpy.data.objects['3'].pose.bones[y3]
    elif f==4:
        d=bpy.data.objects['3'].pose.bones[y4]
    elif f==5:
        d=bpy.data.objects['3'].pose.bones[y5]
    else:
        print ('error')
                          
    #separation from other fingers
    if m==0:
        mov=0
    elif m==1:   #moves away
         mov= -0.2 
    elif m==-1:  #moves closer
        mov= 0.2
        if f==1 or f==5:
            mov=0.2
        elif f==4:
            mov=0.1    
    else:
        print('error')   
    if f>0 and f<=2:
        d.rotation_quaternion[3]=mov
    elif f>2 and f<=5:
        d.rotation_quaternion[3]=-mov          
    else:
        print ('error')
        
 #perpendicular from palm
    if r==1:
        if f==1:
            d.rotation_quaternion[1]=0.2
        else:
             d.rotation_quaternion[1]=0.5
    elif r==0:
          d.rotation_quaternion[1]=0            
           
        
#detRF(5,0,0) #example, uncomment and run script to test  

def detLF(f,m,r): #especific finger position RIGHT HAND (finger=[1=thumb...,5=pinky],separation from fingers=[-1,0,1], perpendicular to pal=[0,1])
    #which finger
   
    y1='thumb.01.L'
    y2='f_index.01.L'
    y3='f_middle.01.L'
    y4='f_ring.01.L'
    y5='f_pinky.01.L'
           
    if f==0:
        print('no finger was specified')
        return  
    elif f==1:
        d=bpy.data.objects['3'].pose.bones[y1]
    elif f==2:
        d=bpy.data.objects['3'].pose.bones[y2]
    elif f==3:
        d=bpy.data.objects['3'].pose.bones[y3]    
    elif f==4:
        d=bpy.data.objects['3'].pose.bones[y4]
    elif f==5:
        d=bpy.data.objects['3'].pose.bones[y5]
    else:
        print ('no finger was specified')
        return
                         
    #separation from fingers
    if m==0:
        mov=0
    elif m==-1:   #moves closer
        mov= -0.2     
        if f==4:
            mov=-0.12
    elif m==1:  #moves away
        mov= 0.1
        if f==1:
            mov=0.2
    else:
        print('error')
    if f>0 and f<=2:
        d.rotation_quaternion[3]=mov
    elif f>3 and f<=5:
        d.rotation_quaternion[3]=-mov    
    else:
        print ('error')   
 
 #perpendicular from palm
    if r==0:
        d.rotation_quaternion[1]=0
    elif r==1:
        if f==1: 
            d.rotation_quaternion[1]=0.2
        else:
             d.rotation_quaternion[1]=0.5
             
detLF(1,0,0)

 
####################################################


def rotLH(t,r):
    wik=bpy.data.objects['3'].pose.bones["hand.ik.L"]
    wfk=bpy.data.objects['3'].pose.bones["hand.fk.L"]
    if r==0: #rot muneca adentro afuera
        wik.rotation_quaternion[0]=wik.rotation_quaternion[0]
        wik.rotation_quaternion[1]=wik.rotation_quaternion[1]
        wik.rotation_quaternion[2]=wik.rotation_quaternion[2]
        wik.rotation_quaternion[3]=wik.rotation_quaternion[3]
    elif r==1:
        a=2
        b=0.05
        if wik.location[2]<0.1 and wik.location[2]>=0.05:
            a=5
            b=-0.3
        if wik.location[2]<0.05:
            a=6
            b=-2    
        bpy.ops.mhx2.snap_fk_ik(data="MhaArmIk_L 2 3 12")
        wfk.rotation_quaternion[0]=a
        wfk.rotation_quaternion[1]=b
        bpy.ops.mhx2.snap_ik_fk(data="MhaArmIk_L 2 3 12")
    elif r==2:
        a=30
        b=-25
        bpy.ops.mhx2.snap_fk_ik(data="MhaArmIk_L 2 3 12")
        wfk.rotation_quaternion[0]=a
        wfk.rotation_quaternion[2]=b
        bpy.ops.mhx2.snap_ik_fk(data="MhaArmIk_L 2 3 12")    
    else:
        print ('error')
    if t==0:
        r=0
    elif t==1:
        a=0.4
        b=-0.7
        bpy.ops.mhx2.snap_fk_ik(data="MhaArmIk_L 2 3 12")
        wfk.rotation_quaternion[1]=a
        wfk.rotation_quaternion[3]=b
        bpy.ops.mhx2.snap_ik_fk(data="MhaArmIk_L 2 3 12")
    elif t==-1:
        a=-1
        b=-0.1
        bpy.ops.mhx2.snap_fk_ik(data="MhaArmIk_L 2 3 12")
        wfk.rotation_quaternion[1]=a
        wfk.rotation_quaternion[3]=b
        bpy.ops.mhx2.snap_ik_fk(data="MhaArmIk_L 2 3 12")        
              
#rotLH(0,0)                 


def rotRH(t,r):  #rotacion mano derecha
    wik=bpy.data.objects['3'].pose.bones["hand.ik.R"]
    wfk=bpy.data.objects['3'].pose.bones["hand.fk.R"]
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
                   
#rotRH(0,2)

def default():
    hRH(0)
    rhF(0,0,0,0,0)
    hLH(0)
    lhF(0,0,0,0,0)

      
