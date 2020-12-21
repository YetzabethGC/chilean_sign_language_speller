import bpy

def htilt(m,x,a): #control movimientos de cabeza (M= r o t)
    hd= bpy.context.object.pose.bones["head"]
    nc= bpy.context.object.pose.bones["neck"]
    if m=='r':
        if a==0:
            hd.rotation_quaternion=(1,0,0,0)
            nc.rotation_quaternion=(1,0,0,0)
        elif a==1:
            hd.rotation_quaternion[2]=0.6
        elif a==-1:
            hd.rotation_quaternion[2]=-0.6
    elif m=='t':
        if x=='x':
            if a==0:
                nc.rotation_quaternion=(1,0,0,0)
            elif a==1:
                nc.rotation_quaternion[3]=-0.2
            elif a==-1:
                nc.rotation_quaternion[3]=0.2
        elif x=='y':
            if a==0:
                nc.rotation_quaternion=(1,0,0,0)
            elif a==1:
                nc.rotation_quaternion[1]=-0.2
            elif a==-1:
                nc.rotation_quaternion[1]=0.3        
                                            
                                            
htilt('t','y',1)    

def mouth(a):
    jaw=bpy.context.object.pose.bones["jaw"]
    pmoL=bpy.context.object.pose.bones["p_mouth_out.L"]
    pmoR=bpy.context.object.pose.bones["p_mouth_out.R"]
    if a==0:
        pmoL.location[0]=0.012
        pmoL.location[2]=-0.012
        pmoR.location[0]=-pmoL.location[0]
        pmoR.location[2]=pmoL.location[2]
        jaw.location=(0,0,0)
    if a=='a':
        jaw.location[2]=0.02
    #elif a=='o':
            
        
#mouth(0)          