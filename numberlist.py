#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      08140
#
# Created:     19/12/2018
# Copyright:   (c) 08140 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

#-------Seting---------

N = 7
data= []

#-----------------------

def RandomNumbers():
    for i in range(0,N):
        data.append(random.randint(1,101))

    print('原始資料 = ' )

    for i in range(N):
        print('%5d' %data[i],end = '')

    print('\n','----------------------------')

    pass


def 氣泡排序法():
    data = [54,97,32,30,30,36,31]
    N = len(data)
    print('氣泡排序法')
    print('原始資料 = ' )

    for i in range(N):
        print('%3d' %data[i],end = '')

    print('\n','----------------------------')

    print()
    for i in range(N-1,-1,-1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]

        for j in range(N):
            print('%3d' %data[j],end = '')
        print()


def 氣泡排序法2():
    RandomNumbers()
    for i in range(0,N,1):
        for j in range(N-1):
            if data[j+1] < data[j]:
                data[j+1],data[j] = data[j],data[j+1]
        for j in range(N):
            print('%5d' %data[j],end = '')
        print()
    return

def 選擇排序法():
    print('選擇排序法')
    RandomNumbers()

    for i in range(N):
        for j in range(i+1,N):
            if data[i] > data[j]:
                data[i],data[j] = data[j],data[i]

    for i in data:
        print('%5d' %i,end = '')
    return



def 插入排序法():
    print('插入排序法')
##    RandomNumbers()

    data = [101,94,12,95,84,70,100]

    for i in range(1,N):
        tmp = data[i]
        no = i-1

        print('tmp =' ,tmp )

        while no >= 0 and tmp < data[no]:
            print('tmp (', tmp ,')< data[i-1] (' ,data[no], ')')
            data[no+1] = data[no]
            no=no-1

            data[no+1] = tmp
            print(no)
            print('\n','------------------------')
            for i in range(N):
                print('%5d' %data[i],end = '')
            print('\n','------------------------')

##            print('tmp =' ,tmp )
##            print('data[',no,']+1 =' ,data[no+1] )
##            print('data[',no+1,']+2 =' ,data[no+1] )


    for i in range(N):
        print('%5d' %data[i],end = '')

def 插入排序法2():
    print('插入排序法2')
    RandomNumbers()

    for i in range(1,N-1):
        tmp = data[i]
        no = i-1
##        print(tmp)
        while i-1 >= 0 and tmp < data[i-1]:
##            print('data[',i,']', data[i],'<','data[',i-1,']', data[i-1])
            data[i] = data[i-1]
            i=i-1
##            print('no =',i-1)
            data[i] = tmp

##            print('data[i] = ' ,data[i])
##            print('data[i-1] = ' ,data[no])
##
##            print('data[',i,']', data[i],'<','data[',no,']', data[no])

##        print('\n','------------------------')
##        for i in range(N):
##            print('%5d' %data[i],end = '')
##        print('\n','------------------------')


    print('\n','------------------------')
    for i in range(N):
        print('%5d' %data[i],end = '')


def main():
##    氣泡排序法2()
##    選擇排序法()
    插入排序法2()
    pass

if __name__ == '__main__':
    main()