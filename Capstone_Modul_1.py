# Nama :Sufriana
# Program : JCDS-Jakarta

from tabulate import tabulate

data = [
        {'Nomor': 1, 'Kode' : '001', 'Nama Produk' : 'Sunscreen','Kemasan': 'Refill','Stok':90, 'Harga':50000, 'Total Nilai Stok':4500000},
        {'Nomor': 2, 'Kode' : '002', 'Nama Produk' : 'Toner','Kemasan': 'Plastik pompa','Stok':60, 'Harga':30000, 'Total Nilai Stok':1800000},
        {'Nomor': 3, 'Kode' : '003', 'Nama Produk' : 'Moisturizer','Kemasan': 'Jar','Stok':70, 'Harga':80000, 'Total Nilai Stok':4000000},
        {'Nomor': 4, 'Kode' : '004', 'Nama Produk' : 'Day Cream','Kemasan': 'Jar','Stok':100, 'Harga':80000, 'Total Nilai Stok':4000000},
        {'Nomor': 5, 'Kode' : '005', 'Nama Produk' : 'Serum','Kemasan': 'Kaca Dropper','Stok':60, 'Harga':70000, 'Total Nilai Stok':2800000}
        ]


#Validasi
def input_numerik(prompt):
    while True:
        nomor = input(prompt)
        if nomor.isdigit():
            return int (nomor)
        else:
            print('Yang Anda Masukkan Bukan Angka')

def input_alfabet(prompt):
    while True:
        nama = input(prompt)
        if nama.replace(" ","").isalpha():
            return nama
        else:
            print('Yang Anda Masukkan Bukan Alfabet')

def validasi_harga(harga):
    if harga <= 0 or harga == 100:
        return False
    elif harga % 1000 != 0:
        return False
    else:
        return True

def input_harga(prompt):
    while True:
        harga = input_numerik(prompt)
        if validasi_harga(harga):
            return harga
        else:
            print("Harga Harus Kelipatan Ribuan (Minimal 1000)")

#Menampilkan Data
def pilihread():
    while True:
        pilih =input('''
                        Menu Melihat Data Skincare
                     1. Melihat Seluruh Data Skincare
                     2. Kembali Ke Menu Utama
 
                     Masukkan Angka yang Igin Dijalankan : ''')
        if pilih == '1':
            read_data()
        elif pilih == '2':
            break
        else:
            print('Masukkan Angka 1 atau 2')

def read_data():
    for index, setiap_data in enumerate(data):
        setiap_data['Nomor'] = index + 1
    print(tabulate(data, headers='keys', tablefmt='fancy_grid'))


#Menambahkan Data
def pilihcreate():
    while True:
        pilih =input('''
                        Menu Membuat Data Skincare
                     1. Menambah Data Skincare
                     2. Kembali ke Menu Utama
 
                     Masukkan Angka yang Ingin Dijalankan : ''')
        if pilih == '1':
            create_data()
        elif pilih == '2':
            break
        else:
            print('Masukkan Angka 1 atau 2')


def create_data():
    read_data()
    last_code = int(data[-1]['Kode']) + 1
    nama_produk = input_alfabet('Masukkan Nama Produk: ')
    stok = input_numerik('Masukkan Stok: ')
    kemasan = input_alfabet('masukkan Kemasan: ')
    harga = input_harga('Masukkan Harga: ')
    total = harga * stok
    data.append({'Kode': str(last_code).zfill(3), 'Nama Produk': nama_produk.title(), 'Kemasan': kemasan.title(), 'Stok': stok, 'Harga': harga, 'Total Nilai Stok': total})
    print('Data Berhasil Dibuat')
    read_data()

#Memperbaharui Data
def pilihUpdate():
    while True:
        pilih =input('''
                        Menu Memperbaharui Data Skincare
                     1. Megubah Data Skincare
                     2. Kembali ke Main Menu
 
                     Masukkan Angka yang Igin Dijalankan : ''')
        if pilih == '1':
            update_data()
        elif pilih == '2':
            break
        else:
            print('Masukkan Angka 1 atau 2')

def update_data():
    while True:
        read_data()
        kode_data = input('Masukkan Kode Data: ')
        found = True
        for index, produk in enumerate(data):
            if produk['Kode'] == kode_data:
                found = True
                print(tabulate([data[index]], headers='keys', tablefmt='fancy_grid'))
                print('Pilih Data yang Akan Diperbaharui')
                print('1. Nama Produk')
                print('2. Stok')
                print('3. Kemasan') 
                print('4. Harga')    
                pilih = input_numerik ('Masukkan Pilihan yang Ingin Dijalankan: ')
                if pilih == 1:
                    nama_produk = input_alfabet('Masukkan Nama Produk Baru: ')
                    data[index]['Nama Produk'] = nama_produk.title()
                elif pilih == 2:
                    stok = input_numerik('Masukkan Stok Baru: ')
                    data[index]['Stok'] = stok  
                elif pilih == 3:
                    kemasan = input_alfabet('Masukkan Nama Kemasan Baru: ')
                    data[index]['Kemasan'] = kemasan.title()                                         
                elif pilih == 4:
                    harga = input_harga('Masukkan Harga Baru: ')
                    data[index]['Harga'] = harga
                    data[index]['Stok'] = data[index]['Total Nilai Stok'] // harga             
                else :
                    print ('Masukkan Angka 1 hingga 4')
                
                data[index]['Total Nilai Stok'] = data[index]['Stok'] * data[index]['Harga']
                print('Data Berhasil Diupdate')
                read_data()
                while True:
                    update_lagi = input("Apakah Anda Ingin Memperbaharui Data Lagi? (Y/N): ").upper()
                    if update_lagi == 'Y':
                        break
                    elif update_lagi == 'N':
                        return 
                    else:
                        print("Masukkan Huruf Y atau N.")
                break
            else:
                found = False
        if found == False:
            print("Kode tidak Valid. Silahkan Masukkan Kode Data yang Valid")


#Menghapus Data
def pilihdelete():
    while True:
        pilih =input('''
                        Menu Hapus Data Skincare
                     1. Hapus Data Skincare
                     2. Kembali Ke Menu Utama
 
                     Masukkan Angka yang Igin Dijalankan : ''')
        if pilih == '1':
           delete_data()
        elif pilih == '2':
            break
        else:
            print('Masukkan Angka 1 atau 2')

def delete_data():
    while True:
        read_data()
        kode_data = input('Masukkan Kode Data yang Ingin Dihapus: ')
        for index, produk in enumerate(data):
            if produk['Kode'] == kode_data:
                print(tabulate([data[index]], headers='keys', tablefmt='fancy_grid'))
                pilih = input("Apakah Anda Yakin Ingin Menghapus Data Ini? (Y/N): ").upper()
                if pilih == 'Y':
                    del data[index]
                    print("Data Berhasil Dihapus")
                    read_data()
                elif pilih == 'N':
                    print("Penghapusan Data Dibatalkan")
                else:
                    print("Masukkan 'Y' untuk ya atau 'N' untuk tidak")
                return
        print("Kode tidak Ditemukan. Silahkan Masukkan Kode Data yang Valid")   

#Mengurutkan Data
def pilihSorted():
    while True:
        pilih =input('''
                        Menu Mengurutkan Data Skincare
                     1. Urutkan Data Skincare
                     2. Kembali Ke Menu Utama
 
                     Masukkan Angka yang Igin Dijalankan : ''')
        if pilih == '1':
           sorted_data()
        elif pilih == '2':
            break
        else:
            print('Masukkan Angka 1 atau 2')

def sorted_data():
    while True:
        print('''
                Menu Data yang Ingin Diurutkan
              1. Nama Produk
              2. Kemasan
              3. Stok ''')

        pilih = input_numerik('Masukkan Data yang Ingin Diurutkan: ')
        if pilih == 1:
            sorted_data= sorted(data, key= lambda x: x['Nama Produk'])
            print(tabulate(sorted_data, headers='keys', tablefmt='fancy_grid'))
            break
        elif pilih == 2:
            sorted_data= sorted(data, key= lambda x: x['Kemasan'])    
            print(tabulate(sorted_data, headers='keys', tablefmt='fancy_grid'))
            break
        elif pilih ==3:
            sorted_data= sorted(data, key=lambda x: x['Stok']) 
            print(tabulate(sorted_data, headers='keys', tablefmt='fancy_grid'))
            break
        else: 
            print('Pilihan tidak Valid. Masukkan Angka 1 Hingga 3')     

#Cari Data
def pilihFilter():
    while True:
        pilih =input('''
                        Menu Mencari Data Skincare
                     1. Mencari Data Skincare
                     2. Kembali Ke Menu Utama
 
                     Masukkan Angka yang Igin Dijalankan : ''')
        if pilih == '1':
           filter_data()
        elif pilih == '2':
            break
        else:
            print('Masukkan Angka 1 atau 2')

def filter_data():
    read_data()
    while True:
      kolom_filter = input('Mau Cari Data di Kolom yang Mana?')
      if kolom_filter in ['Harga','Stok']:
         minimal = input_numerik(f'Minimal {kolom_filter} yang anda filter : ')
         maksimal = input_numerik(f'Maksimal {kolom_filter} yang anda filter : ')
         List_Filter = list(filter(lambda setiap_data: setiap_data[kolom_filter] >= minimal and setiap_data[kolom_filter] <= maksimal,data))
         if len(List_Filter) != 0:
            print(tabulate(List_Filter,headers='keys',tablefmt='fancy_grid'))
            break
         else:
            print("Data tidak Ditemukan")
            break
      elif kolom_filter in ['Nama Produk','Kemasan','Kode']:
         cari_filter = input('Mau Cari Data Apa? ')
         List_Filter = list(filter(lambda setiap_data: setiap_data[kolom_filter] == cari_filter,data))
         if len(List_Filter) != 0:
            print(tabulate(List_Filter,headers='keys',tablefmt='fancy_grid'))
            break
         else:
            print('Data tidak Ditemukan')
            break
      else:
         print("Kolom yang Diminta tidak Ada")

#Menu Utama
def main():
    while True:
        print('''
              
                LAPORAN STOK SKINCARE PADA GUDANG
                             PT CARE
              
                    1. Melihat Data Skincare
                    2. Menambahkan Data Skincare 
                    3. Memperbaharui Data Skincare
                    4. Menghapus Data Skincare
                    5. Mengurutkan Data Skincare
                    6. Mencari Data Skincare
                    7. Keluar Aplikasi ''')
        menu = input_numerik('Masukkan Pilihan yang Ingin Dijalankan: ')
        if menu == 1:
            pilihread()
        elif menu== 2:
            pilihcreate()
        elif menu==3:
            pilihUpdate()
        elif menu==4:
            pilihdelete()
        elif menu == 5:
            pilihSorted()
        elif menu == 6:
            pilihFilter()
        elif menu == 7:
            print('Selesai')
            break
        else:
            print('Masukkan Angka 1 Hingga 7')

main()

         
