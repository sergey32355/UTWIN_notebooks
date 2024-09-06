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

    Node_Names, Nodes_coord_X, Nodes_coord_Y, Cond_Names, Nodes_in, Nodes_out, Length,Roughness=extract_info(lkm)
    
    return Node_Names, Nodes_coord_X, Nodes_coord_Y, Cond_Names, Nodes_in, Nodes_out, Length,Roughness
            

def extract_info(file_text,delimeter="\s"):#deimeters for inp - \s,\t

    substring1="COORDINATES"
    substring2="CONDUITS"
    
    Node_Names=[]
    Nodes_coord_X=[]
    Nodes_coord_Y=[]

    Cond_Names=[]
    Nodes_in=[]
    Nodes_out=[]

    #service variables
    #nodes
    substr1_offset=2
    string1_substring="["
    string1_list=[]
    coord_flag=False
    
    #conduits
    substr2_offset=2
    string2_substring="["
    string2_list=[]
    
    
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
                k.index(string1_substring)            
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
    
    offset=3
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
    
    return Node_Names, Nodes_coord_X, Nodes_coord_Y, Cond_Names, Nodes_in, Nodes_out, Length,Roughness

