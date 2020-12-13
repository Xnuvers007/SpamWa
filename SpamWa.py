# user/XnuversXploitXentzh/bin/python 3.7

# PYTHON 3.7 or 3.x

from selenium import webdriver
import os
import sys
import datetime
import time
from datetime import date, datetime

os.system('color B')
print ('''                                                                       
 @@@@@@   @@@@@@@    @@@@@@   @@@@@@@@@@      @@@  @@@  @@@   @@@@@@   
@@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@@@@@     @@@  @@@  @@@  @@@@@@@@  
!@@       @@!  @@@  @@!  @@@  @@! @@! @@!     @@!  @@!  @@!  @@!  @@@  
!@!       !@!  @!@  !@!  @!@  !@! !@! !@!     !@!  !@!  !@!  !@!  @!@  
!!@@!!    @!@@!@!   @!@!@!@!  @!! !!@ @!@     @!!  !!@  @!@  @!@!@!@!  
 !!@!!!   !!@!!!    !!!@!!!!  !@!   ! !@!     !@!  !!!  !@!  !!!@!!!!  
     !:!  !!:       !!:  !!!  !!:     !!:     !!:  !!:  !!:  !!:  !!!  
    !:!   :!:       :!:  !:!  :!:     :!:     :!:  :!:  :!:  :!:  !:!  
:::: ::    ::       ::   :::  :::     ::       :::: :: :::   ::   :::  
:: : :     :         :   : :   :      :         :: :  : :     :   : :  
                                                                       
                                     
@@@  @@@   @@@@@@         @@@@@@@@   
@@@  @@@  @@@@@@@@       @@@@@@@@@@  
@@!  @@@       @@@       @@!   @@@@  
!@!  @!@      @!@        !@!  @!@!@  
@!@  !@!     !!@         @!@ @! !@!  
!@!  !!!    !!:          !@!!!  !!!  
:!:  !!:   !:!           !!:!   !!!  
 ::!!:!   :!:       :!:  :!:    !:!  
  ::::    :: :::::  :::  ::::::: ::  
   :      :: : :::  :::   : : :  :   
                                     

Coding By XnuversXploitXen''')
print("Mohon tunggu Sebentar")
time.sleep(6)
os.system('cls')

print ('\n')
print ("|-------------------------------------|")
print ("| Author   : XNUVERS007               |")
print ("| You Tube : https://bit.ly/Xnuvers   |")
print ("| github   : https://bit.ly/Xnuvrs1   |")
print ("| Facebook : https://bit.ly/Fesbuck   |")
print ("| Instagram: https://bit.ly/Xnvrs13   |")
print ("| Site     : http://bit.ly/Mykingbee  |")
print ("|-------------------------------------|")
devdate = "18 November 2020"
aplikasi = "Spam Whatsapp By Xnuvers v20"
Versi = "Version 2.0"

print(aplikasi)
print(Versi)
print(devdate)

print ('\n')


d = 'Hari (Day) = '
e = 'Bulan ke (Months) = '
f = 'Tahun (Year) = '

hari_ini = datetime.now()
tanggal = hari_ini.strftime(d+'%d, ' + e+'%m, ' + f+'%y')
print (tanggal)

J = 'Jam (hours) = '
M = 'Menit (Minutes) = '
D = 'Detik (Seconds) = '

saat_ini = datetime.now()
jam = saat_ini.strftime(J+'%H : ' + M+'%M : ' + D+'%S')
print(jam)
print("\n")
input("Tekan Enter , dan tunggu 5 detik untuk menjalankan")
time.sleep(5)

driver = webdriver.Chrome('webdriver/chromedriver.exe')
driver.implicitly_wait(15) 
driver.get('https://web.whatsapp.com')
print("\n========= CTRL + C atau close Untuk Memberhentikan =========")
print("\n")
print("Terimakasih Sudah menggunakan Program/Aplikasi dari Aku ini :D\n")
print("KEEP SPIRIT dan jangan disalah gunakan ya\n")
print("Dukung Programmer Indonesia menuju yang Terbaik\n")
print("==============================================================")
time.sleep(6)
print("\n")
driver.find_element_by_css_selector("span[title='" + input("Masukan Nama yang ingin di spam (Huruf besar kecil berpengaruh): ") + "']").click()
inputString = input("Masukan Pesan Yang ingin dikirim: ")
while(True):
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
