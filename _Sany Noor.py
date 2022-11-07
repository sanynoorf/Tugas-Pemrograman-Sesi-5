#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1.Buatlah biodata sederhana dengan menggunakan fungsi input(), dan output variabel dengan fungsi format()


# In[1]:


nama = input("masukan nama : ")
kelas = input("masukan kelas : ")
nim = input("masukan nim : ")
jurusan = input("masukan jurusan : ")

print("Hello, nama saya %s, kelas saya %s, nim %s, jurusan %s " % (nama, kelas, nim, jurusan))


# In[ ]:


# 2.Jika terdapat kalimat UNIVERSITAS NUSA PUTRA SUKABUMI ,buatlah kode program untuk menampilkan output:
 a.putra nusa
 b.NIVERSITAS NSA PTRA SKABMI
 c.SUKABUMI PUTRA NUSA UNIVERSITAS
 d.UNPS
 e.TAS SAPU BUMI


# In[2]:


judul = "UNIVERSITAS NUSA PUTRA SUKABUMI"

a = judul[17:22].lower()+' '+judul[12:16].lower()
b = judul[1:11]+' '+judul[12]+judul[14:16]+' '+judul[17]+judul[19:22]+' '+judul[22:31].upper()
c = judul[23:31]+' '+judul[17:22]+' '+judul[12:16]+' '+judul[0:11].upper()
d = judul[0]+judul[12]+judul[17]+judul[23].upper()
e = judul[8:11]+' '+judul[14:16]+judul[17:19]+' '+judul[27:31].upper()

print("JAWABAN OPTION A :", a)
print("JAWABAN OPTION B :", b)
print("JAWABAN OPTION C :", c)
print("JAWABAN OPTION D :", d)
print("JAWABAN OPTION E :", e)

