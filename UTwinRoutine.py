import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import pylab
import turtle
import cv2
import random
import time
import sys
import PIL
from collections import deque
from itertools import combinations,groupby
import time
import string
from pygsp import graphs, filters
import re

def OpenInp(path):
    lkm=[]
    try: 
        file = open(path, "r")
        lines=file.readlines()
        for l in lines:
            lkm.append(l)
        file.close()
    except Exception as X:
        print("Exception raised while opening file. Exception: "+str(X))
        try:file.close()
        except: pass
        return [], [], [], [], [], [], [],[]

    #print (len(lkm))    

    Node_Names, Nodes_coord_X, Nodes_coord_Y, Cond_Names, Nodes_in, Nodes_out, Length,Roughness,Cond_cross_shape,Cond_cross_section_geom_1,Cond_cross_section_geom_2,Cond_cross_section_geom_3,Cond_cross_section_geom_4,Junc_Names,Junc_elevation,Junc_max_depth,Junc_init_depth,Storage_name,Storage_elevation,Storage_max_depth,Pump_name,Pump_From_Node,Pump_To_Node,Pump_Curve,Pump_Status,Pump_Sartup,Pump_Shutoff,Outfalls_name,Outfalls_elevation,Outfalls_type=extract_info(lkm)
    
    return Node_Names, Nodes_coord_X, Nodes_coord_Y, Cond_Names, Nodes_in, Nodes_out, Length,Roughness,Cond_cross_shape,Cond_cross_section_geom_1,Cond_cross_section_geom_2,Cond_cross_section_geom_3,Cond_cross_section_geom_4,Junc_Names,Junc_elevation,Junc_max_depth,Junc_init_depth,Storage_name,Storage_elevation,Storage_max_depth,Pump_name,Pump_From_Node,Pump_To_Node,Pump_Curve,Pump_Status,Pump_Sartup,Pump_Shutoff,Outfalls_name,Outfalls_elevation,Outfalls_type
           

def extract_info(file_text,delimeter="\s"):#deimeters for inp - \s,\t
    
    substring1=  "COORDINATES"
    substring2=  "CONDUITS"
    substring2_1="XSECTIONS"
    substring3=  "JUNCTIONS"
    substring4=  "STORAGE"
    substring5=  "PUMPS"
    substring6=  "OUTFALLS"
    
    Node_Names=[]
    Nodes_coord_X=[]
    Nodes_coord_Y=[]

    Cond_Names=[]
    Nodes_in=[]
    Nodes_out=[]
    #CONDUITS CROSS SECTIONS
    Cond_cross_shape=[]
    Cond_cross_section_geom_1=[]
    Cond_cross_section_geom_2=[]
    Cond_cross_section_geom_3=[]
    Cond_cross_section_geom_4=[]

    Junc_Names=[]
    Junc_elevation=[]
    Junc_max_depth=[]
    Junc_init_depth=[]

    Storage_name=[]
    Storage_elevation=[]
    Storage_max_depth =[]

    Pump_name = []
    Pump_From_Node = []
    Pump_To_Node = []
    Pump_Curve = []
    Pump_Status = []
    Pump_Sartup = []
    Pump_Shutoff = []

    Outfalls_name=[]
    Outfalls_elevation=[]
    Outfalls_type=[]

    #service variables
    #nodes    
    string1_substring="["
    string1_list=[]
    coord_flag=False
    
    #conduits    
    string2_substring="["
    string2_list=[]
    #conduits geometry
    string2_1_list=[]

    #junctions    
    string3_substring="["
    string3_list=[]

    #storages    
    string4_substring="["
    string4_list=[]

    #pumps    
    string5_substring="["
    string5_list=[]
    
    #outfalls
    string6_substring="["
    string6_list=[]

    for_string_56=file_text
    
    #this are the Nodes information
    for k in file_text:
        
        if(coord_flag==False):
            try:
                k.index(substring1)
            except ValueError:
                pass
            else:
                coord_flag=True
        else:
            try:
                k.index(string1_substring)            
            except ValueError:
                string1_list.append(k)
            else:
                break
    
    offset=2
    #nodes names and coordinates
    for k in range (offset,len(string1_list)):
        str_tmp=string1_list[k]
        str_list=re.split(delimeter,str(str_tmp)) #str(k).split(delimeter)
        str_list = list(filter(None, str_list))        
        if(len(str_list)==3):            
            Node_Names.append(str_list[0].strip())
            Nodes_coord_X.append(float(str_list[1].strip()))
            Nodes_coord_Y.append(float(str_list[2].strip()))

    #----------------------------------------
    #this is conduit information
    #----------------------------------------
    
    coord_flag=False
    
    for k in file_text:
        
        if(coord_flag==False):
            try:
                k.index(substring2)
            except ValueError:
                pass
            else:
                coord_flag=True
        else:
            try:
                k.index(string2_substring)            
            except ValueError:
                string2_list.append(k)
            else:
                break

    #check if the list includes the needed information
    #print(string2_list)
    Length=[]
    Roughness=[]
    InOffset=[]
    OutOffset  =[]
    InitFlow   =[]
    MaxFlow=[]
    
    offset=2
    #conduits names and coordinates
    for g in range(offset,len(string2_list)):        
        k=string2_list[g]        
        str_list=re.split(delimeter,str(k))#str(k).partition(delimeter) #split(delimeter)
        #remove empty elements frmom list
        str_list = list(filter(None, str_list))
        
        if(len(str_list)==9):
            Cond_Names.append((str_list[0]).strip())
            Nodes_in.append  ((str_list[1]).strip())
            Nodes_out.append ((str_list[2]).strip())
            Length.append    ((str_list[3]).strip())
            Roughness.append ((str_list[4]).strip())
            InOffset.append  ((str_list[5]).strip())
            OutOffset.append ((str_list[6]).strip())
            InitFlow.append  ((str_list[7]).strip())
            MaxFlow.append   ((str_list[8]).strip())

    
    #____________________________________________________________
    #____________conduits cross sections_________________________
    string2_1_list=[]
    coord_flag=False
    
    for k in file_text:
        
        if(coord_flag==False):
            try:
                k.index(substring2_1)
            except ValueError:
                pass
            else:
                coord_flag=True
        else:
            try:
                k.index(string2_substring)            
            except ValueError:
                string2_1_list.append(k)
            else:
                break

    #print("-----------CONDUITS CROSS SECTIONS--------------")
    #print(string2_1_list)

    #check if the list includes the needed information
    #print(string2_list)

    Cond_cross_shape=[]
    Cond_cross_section_geom_1=[]
    Cond_cross_section_geom_2=[]
    Cond_cross_section_geom_3=[]
    Cond_cross_section_geom_4=[]

    for p in range(0,len(Cond_Names)):
        Cond_cross_shape.append([])
        Cond_cross_section_geom_1.append([])
        Cond_cross_section_geom_2.append([])
        Cond_cross_section_geom_3.append([])
        Cond_cross_section_geom_4.append([])

    offset=2
    #conduits names and coordinates
    for g in range(offset,len(string2_1_list)):        
        k=string2_1_list[g]        
        str_list=re.split(delimeter,str(k))#str(k).partition(delimeter) #split(delimeter)
        #remove empty elements frmom list
        str_list = list(filter(None, str_list))
        
        if(len(str_list)>=5):

            cond_name=(str_list[0]).strip()
            try:
                indx=Cond_Names.index(cond_name)
            except Exception as Ex:
                continue

            Cond_cross_shape[indx].append(((str_list[1]).strip()))
            Cond_cross_section_geom_1[indx].append  (float((str_list[2]).strip()))
            Cond_cross_section_geom_2[indx].append (float((str_list[3]).strip()))
            Cond_cross_section_geom_3[indx].append (float((str_list[4]).strip()))
            Cond_cross_section_geom_4[indx].append (float((str_list[5]).strip()))
            
    tmpCond_cross_shape=[]
    tmpCond_cross_section_geom_1=[]
    tmpCond_cross_section_geom_2=[]
    tmpCond_cross_section_geom_3=[]
    tmpCond_cross_section_geom_4=[]
    
    for p in range(0,len(Cond_cross_shape)):
        
        #print(Cond_cross_shape[p])
        tmpCond_cross_shape.append(Cond_cross_shape[p][0])
        tmpCond_cross_section_geom_1.append(Cond_cross_section_geom_1[p][0])
        tmpCond_cross_section_geom_2.append(Cond_cross_section_geom_2[p][0])
        tmpCond_cross_section_geom_3.append(Cond_cross_section_geom_3[p][0])
        tmpCond_cross_section_geom_4.append(Cond_cross_section_geom_4[p][0])

    
    Cond_cross_shape=tmpCond_cross_shape
    Cond_cross_section_geom_1=tmpCond_cross_section_geom_1
    Cond_cross_section_geom_2=tmpCond_cross_section_geom_2
    Cond_cross_section_geom_3=tmpCond_cross_section_geom_3
    Cond_cross_section_geom_4=tmpCond_cross_section_geom_4

    

    #____________________________________________________________
    #____________________________________________________________

    offset=2
    #---------------
    #junctions
    #-------------
    coord_flag=False
    
    for k in file_text:
        
        if(coord_flag==False):
            try:
                k.index(substring3)
            except ValueError:
                pass
            else:
                coord_flag=True
        else:
            try:
                k.index(string3_substring)            
            except ValueError:
                string3_list.append(k)
            else:
                break

    #conduits names and coordinates
    for g in range(offset,len(string3_list)):        
        k=string3_list[g]        
        str_list=re.split(delimeter,str(k))#str(k).partition(delimeter) #split(delimeter)
        #remove empty elements frmom list
        str_list = list(filter(None, str_list))
        
        if(len(str_list)==6):
            Junc_Names.append((str_list[0]).strip())
            Junc_elevation.append (float((str_list[1]).strip()))
            Junc_max_depth.append (float((str_list[2]).strip()))
            Junc_init_depth.append(float((str_list[3]).strip()))  

    #-------------------
    #--Storages---------
    #-------------------
    offset=2

    coord_flag=False

    for k in file_text:
        
        if(coord_flag==False):
            try:
                k.index(substring4)
            except ValueError:
                pass
            else:
                coord_flag=True
        else:
            try:
                k.index(string4_substring)            
            except ValueError:
                string4_list.append(k)
            else:
                break
        
    #print("Open storages")
    #clean commented lines
    updated_list=[]
    for m in string4_list:
        if (";" in m)==False:
            updated_list.append(m)
    string4_list=updated_list
    #for m in string4_list:
    #    print(m)
    #print("Updated length of storage list: "+str(len(string4_list)))

    #storage names and data
    for g in range(0,len(string4_list)):        
        k=string4_list[g]        
        str_list=re.split(delimeter,str(k))#str(k).partition(delimeter) #split(delimeter)
        #remove empty elements frmom list
        str_list = list(filter(None, str_list))
        #print("Storage "+str(g))
        if(len(str_list)>=3):
                    Storage_name.append((str_list[0]).strip())
                    Storage_elevation.append((str_list[1]).strip())
                    Storage_max_depth.append((str_list[2]).strip())

    #-------------------
    #--PUMPS---------
    #-------------------

    #this are the Nodes information
    #print("pumps")
    #print(substring5)
    #print(string5_substring)
    #print(file_text)

    #for line in for_string_56:
    #    print(line)

    #print("PUMPS")
    coord_flag=False

    for line in for_string_56:              
        if(coord_flag==False):
            try:
                line.index(substring5)
            except ValueError:
                pass
            else:
                coord_flag=True                            
        else:
            try:
                line.index(string5_substring)            
            except ValueError:
                string5_list.append(line)
            else:
                break
    
    offset=3
        
    #print("----------------------------------------")
    #for m in string5_list:
    #    print(m)
    #print("----------------------------------------")

    #nodes names and coordinates
    #for k in range (offset,len(string5_list)):
    for mmm in string5_list:        
        #print(mmm)
        str_tmp=mmm
        str_list=re.split(delimeter,str(str_tmp)) #str(k).split(delimeter)
        if(";" in str_list[0]):
            continue
        str_list = list(filter(None, str_list))        
        if(len(str_list)>=3):
            #print("Pump found")
            Pump_name.append(str_list[0].strip())
            Pump_From_Node.append(str_list[1].strip())
            Pump_To_Node.append(str_list[2].strip())
            Pump_Curve.append(str_list[3].strip())
            Pump_Status.append(str_list[4].strip())
            Pump_Sartup.append(str_list[5].strip())
            Pump_Shutoff.append(str_list[6].strip())

    #-----------------
    #outfalls
    #-----------------
    #print("OUTFALLS")
    #for ll in for_string_56:
    #    print(ll)

    coord_flag=False
    for line in for_string_56:        
            if(coord_flag==False):
                try:
                    line.index(substring6)
                except ValueError:
                    pass
                else:
                    coord_flag=True                            
            else:
                try:
                    line.index(string6_substring)            
                except ValueError:
                    string6_list.append(line)
                else:
                    break
        
    #for lm in string6_list:
    #    print(lm)

    offset=3
    for g in range(0,len(string6_list)):       
        k=string6_list[g]        
        str_list=re.split(delimeter,str(k))#str(k).partition(delimeter) #split(delimeter)
        if(";" in str_list[0])==True:
            continue

        #remove empty elements frmom list
        str_list = list(filter(None, str_list))
        #print("Storage "+str(g))
        if(len(str_list)>=3):
                    #print((str_list[0]).strip())
                    #print((str_list[1]).strip())
                    #print((str_list[2]).strip())
                    Outfalls_name.append(str((str_list[0]).strip()))
                    Outfalls_elevation.append(float((str_list[1]).strip()))
                    Outfalls_type.append(str((str_list[2]).strip()))


    return Node_Names, Nodes_coord_X, Nodes_coord_Y, Cond_Names, Nodes_in, Nodes_out, Length,Roughness, Cond_cross_shape, Cond_cross_section_geom_1, Cond_cross_section_geom_2, Cond_cross_section_geom_3, Cond_cross_section_geom_4, Junc_Names,Junc_elevation,Junc_max_depth,Junc_init_depth,Storage_name,Storage_elevation,Storage_max_depth,Pump_name,Pump_From_Node,Pump_To_Node,Pump_Curve,Pump_Status,Pump_Sartup,Pump_Shutoff,Outfalls_name,Outfalls_elevation,Outfalls_type