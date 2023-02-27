#Python ile Veri Analizi

#NumPy
import numpy as np
a=[1,2,3,4]
b=[2,3,4,5]
ab=[]
#Basit Pythonic Way
for i in range(0,len(a)):
    ab.append(a[i]*b[i])
ab
#Numpy Way:
a=np.array([1,2,3,4])
b=np.array([1,2,3,4])
a*b

#Numpy Array Özellikleri
np.array([1,2,3,4,5])
type(np.array([1,2,3,4,5]))
#>numpy.ndarray

np.zeros(10,dtype=int)
#>array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

np.random.randint(0,10,size=10)
#>array([0, 9, 6, 3, 2, 1, 7, 8, 4, 5])

np.random.normal(10,4, (3,4))
#>array([[ 6.73623927,  9.39426646, 10.32602148, 14.04217107],
       [ 9.94684428, 10.50350147, 12.3806758 , 14.84385932],
       [ 6.7415238 , 11.29974311,  6.25618169,  9.30290149]])
#std sapması 4, ort.sı 10'dur.


#ndim: boyut sayısı
#shape: shape bilgisi
#size: toplam eleman sayısı
#dtype: array veri tipi

a=np.random.randint(10,size=5)
#size(10: tek boyutluk 10 elemanlık array oluşturmak
#size(3,5): 2 boyutlu 3 satır 5 sütundan oluşan array oluşturma
a
#> array([0, 1, 8, 0, 0])
a.ndim
#> 1
a.shape
#(5,)
a.size
#5
a.dtype
#dtype('int32')


#Yeniden Şekillendirme (Reshaping)

#Elimizdeki bir numpy arrayinin boyutunu değiştirmek istediğimizde numpy arrayi kullanırız

np.random.randint(1,10,size=9) #Tek boyutlu bir arraydir.
# array([7, 6, 3, 2, 3, 9, 4, 2, 7])

#3'e 3'lük bir matrise dönüştürmek istiyorsak:
np.random.randint(1,10,size=9).reshape(3,3)
#array([[8, 2, 7],
#       [9, 5, 1],
#       [3, 4, 2]])

ar=np.random.randint(1,10,size=9)
ar
# array([9, 3, 3, 3, 3, 2, 4, 3, 4])

ar.reshape(3,3)
#array([[9, 3, 3],
#       [3, 3, 2],
#       [4, 3, 4]])

#Size'ı 10 olsaydı, 10 eleman olsaydı 3.3=9'dan eşit olmadığından hata alacaktı.



#Index İşlemleri
a=np.random.randint(10,size=10)
a
#>array([3, 7, 2, 6, 6, 2, 4, 4, 0, 3])

a[0] #index seçimi
#>3
a[0:5]  #dilimleme
#>array([3, 7, 2, 6, 6])
a[0]=999
a
#>array([999,   7,   2,   6,   6,   2,   4,   4,   0,   3])
#İki boyutlu arraylerde seçim işlemi
m=np.random.randint(10, size=(3,5))
m
#>array([[6, 1, 4, 9, 5],
#       [7, 2, 8, 5, 3],
#       [1, 9, 9, 8, 5]])
m[0,0]
#> 6
m[1,1]
#>2
m[:,0] #bütün satırları seç ve 0. sütunu seç
m[0:2,0:3]
#array([[6, 1, 4],
#       [7, 2, 8]])

#Fancy Index
v=np.arange(0,30,3) #0'dan 30'a kadar 3'er 3'er artacak bir array
v
#>array([ 0,  3,  6,  9, 12, 15, 18, 21, 24, 27])
v[1]
#>3
v[4]
#> 12
#Bir numpy arrayine bir liste girdiğinizde index numarası veya true false ifadelerini de tutuyor olabilir
catch=[1,2,3]
v[catch]
#array([3, 6, 9])

#Numpy Koşullu İşlemler

v=np.array([1,2,3,4,5])
#Klasik python döngü ile
ab=[]
#Bu listenin tüm elemanlarını gezip 3'ten küçük mü sorgusu yapıp bu yeni listeye append metoduyla ekleme işlemi yapılacak.
for i in v:
    if i<3:
        ab.append(i)
ab
#>[1, 2]

#Numpy ile

v<3
#>array([ True,  True, False, False, False])

v[v<3] #True olarak gördüklerini seçer, False olarak gördüklerini seçmez
v[v>3]
v[v!=3]
v[v==3]
v[v<=3]
v[v>=3]
#Mantıksal operatörler kullanılabilir.
#Arka tarafta çalışan mantık fancy kavramıdır çünkü içine True False array'i gönderiyoruz.

#Matematiksel İşlemler
v=np.array([1,2,3,4,5])
#OPERATÖRLER ARACILIĞI İLE
v/5
#>array([0.2, 0.4, 0.6, 0.8, 1. ])

v*5/10
#> array([0.5, 1. , 1.5, 2. , 2.5])

v**2
#>array([ 1,  4,  9, 16, 25], dtype=int32)

v-1
# array([0, 1, 2, 3, 4])

#METODLAR ARACILIĞI İLE
np.subtract(v,1)
#çıkarmadır. >array([0, 1, 2, 3, 4])
np.add(v,1)
#> array([2, 3, 4, 5, 6])
np.mean(v)
#3.0
np.sum(v)
#15
np.min(v)
#1
np.max(v)
#5
np.var(v)
#2.0

#İşlemlerin kalıcı olmasını istiyorsak da tekrardan atama yapmalıyız!








