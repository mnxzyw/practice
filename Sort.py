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

#selecet sort

def Select_sort(la):
    print("Select sort")
    if(None==la):
        return

    for i in range(len(la)):
        min=i;
        for temp in range(i+1,len(la)):
            if(la[min]>la[temp]):
                min=temp
            if(min!=i):
                la[min],la[i]=la[i],la[min]


#insert sort
def Insert_sort(la):
    for i in range(1,len(la)):
        j=i-1
        temp=la[i]
        while((temp<la[j]) and (j>=0)):
            la[j+1]=la[j]
            j-=1
        la[j+1]=temp



#quick sort
def f_sort(arr,nlow,nhigh):
    temp=arr[nlow]
    while(nlow<nhigh):
        while(nlow<nhigh):
            if(arr[nhigh]<temp):
                arr[nlow]=arr[nhigh]
                nlow+=1
                break
            else:
                nhigh-=1
        while(nlow<nhigh):
            if(arr[nlow]>temp):
                arr[nhigh]=arr[nlow]
                nhigh-=1
                break
            else:
                nlow+=1

    arr[nlow]=temp
    return nlow

def Quick_sort(la,nlow,nhigh):
    if(nlow<nhigh):
        nstandard=f_sort(la,nlow,nhigh)
        Quick_sort(la,nlow,nstandard-1)
        Quick_sort(la,nstandard+1,nhigh)



def Print(arr):
    for temp in arr:
        print(temp)

def test(arr):
    Bubble_sort(arr)
    Select_sort(arr)
    Insert_sort(arr)
    Quick_sort(arr,0,len(arr)-1)
    Print(arr)

if __name__=='__main__':

    array=[23,12,32,56,21,1,5,9]
    test(array)

