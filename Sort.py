#!/bin/env python
#coding:utf-8

'''
排序
'''


#bubble sort
def Bubble_sort(la):
    print("Bubble_sort")
    if(None==la):
        return
    for j in range(len(la)):
        for i in range(len(la)-j-1):
            if(la[i]>la[i+1]):
                la[i],la[i+1]=la[i+1],la[i]

#选择排序

def Select_sort(la):
    print("select sort")
    if(None==la):
        return





def Print(arr):
    for temp in arr:
        print(temp)

def test(arr):
    Bubble_sort(arr);
    Select_sort(arr);
    Print(arr);

if __name__=='__main__':

    array=[23,12,32,56,21,1,5,9];
    test(array);

