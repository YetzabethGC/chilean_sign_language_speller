# -*- coding: utf-8 -*-
import bpy

def spinectrl(a,q): #ingresar numeros del 1 al 10
    ch=bpy.context.object.pose.bones["chest"]
    q=q/10
    if a=='x':
        ch.rotation_quaternion[1]=q
    elif a=='y':
        ch.rotation_quaternion[2]=q
    elif a=='z':
        ch.rotation_quaternion[3]=-q
    else:
        ch.rotation_quaternion[1]=0
        ch.rotation_quaternion[2]=0
        ch.rotation_quaternion[3]=0
            

#spinectrl('x',0)     