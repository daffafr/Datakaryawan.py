#CAPSTONE PROJECT MODULE 1 DATA KARYAWAN - Daffa Fauzi Ramadhan

karyawan_tetap = [
    {
        'nama': 'Mike',
        'divisi': 'Finance',
        'level': 'Staff',
        'jabatan': 'Accountant',
        'gaji': 9500000,
    },
    {
        'nama': 'Bella',
        'divisi': 'Marketing',
        'level': 'Staff',
        'jabatan': 'Specialist',
        'gaji': 8000000,
    },
    {
        'nama': 'Kevin',
        'divisi': 'Marketing',
        'level': 'Manager',
        'jabatan': 'Manager',
        'gaji': 12000000,
    },
    {
        'nama': 'Daffa',
        'divisi': 'Finance',
        'level': 'Staff',
        'jabatan': 'Accountant',
        'gaji': 9500000
    },
    
]
staff_magang = [
    {
        'nama': 'Bob',
        'divisi': 'Marketing',
        'level': 'Internship',
        'jabatan': 'Copywriter',
        'gaji': 3000000,
    },
    {
        'nama': 'Jemmy',
        'divisi': 'Marketing',
        'level': 'Internship',
        'jabatan': 'Sales',
        'gaji': 3700000,
    },
    {
        'nama': 'David',
        'divisi': 'Finance',
        'level': 'Internship',
        'jabatan': 'Accountant',
        'gaji': 3500000,
    },
    {
        'nama': 'Fauzi',
        'divisi': 'Creative',
        'level': 'Internship',
        'jabatan': 'Designer',
        'gaji': 3500000
    }
]



def menu():
    print(f'''
        ========================================
             Data Karyawan PT. SINAR SURYA 
        ========================================     
        List Main Menu:
        1. Menampilkan Daftar Data Karyawan
        2. Update Data Karyawan
        3. Menghapus Data Karyawan
        4. Exit
    ''')

def menu1():
    print(f'''
    ====================================
        MENU 1 DAFTAR DATA KARYAWAN
    ====================================
        1. Daftar Data Karyawan
        2. Back
    ''')

def pilih_karyawan():
    print(f'''
        Pilih Data Karyawan:
        1. Karyawan Tetap
        2. Staff Magang
        3. Back
    ''')

def pilih_opsi():
    pilih = int(input('Input Pilihan: '))
    return pilih

def kembali():
    pilih = str(input('Apakah Anda Ingin Kembali ke Menu Sebelumnya ? (Y/N): ').capitalize())
    return pilih

def lihat_karyawan(karyawan):
    print('Index\t| Nama\t| Divisi\t | Level\t | Jabatan\t| Gaji')
    for i in range(len(karyawan)):
        print(f"{i}\t| {karyawan[i]['nama']}\t| {karyawan[i]['divisi']}\t | {karyawan[i]['level']}\t | {karyawan[i]['jabatan']}\t| {karyawan[i]['gaji']} ")
    return

def menu2():
    print(f'''
    ====================================
        MENU 2 UPDATE DATA KARYAWAN
    ====================================
        1. Tambah Data Karyawan
        2. Update Data Karyawan
        3. Back 
    ''')

def tambah(karyawan):
    lihat_karyawan(karyawan)
    while True:
        nama = str(input('Input nama: '))
        for i in range(len(karyawan)):
            if nama == (karyawan[i]['nama']):
                print('Data Karyawan Dengan Nama Tersebut Sudah Ada')
                break
        else:
            divisi = str.title(input('Input divisi: '))
            level = str.title(input('Input level: '))
            jabatan = str.title(input('Input jabatan: '))
            gaji = int(input('Input Gaji: '))
            cek = str(input('Konfirmasi ulang untuk menambah data ini (Y/N) '))
            if cek == 'Y':
                karyawan.append({
                'nama': nama,
                'divisi': divisi,
                'level': level,
                'jabatan': jabatan,
                'gaji': gaji
                })
                lihat_karyawan(karyawan)
                break
            else:
                print('Data tidak jadi ditambahkan')
                lihat_karyawan(karyawan)
                break
    return

def update(karyawan):
    lihat_karyawan(karyawan)
    while True:
        index_karyawan = int(input('Input nomor index data karyawan yang ingin diupdate:  '))
        if index_karyawan not in range(len(karyawan)):
            print('Data dengan nomor index tersebut tidak ada')
            continue
        else:
            for i in range(len(karyawan)):
                if karyawan[index_karyawan] == karyawan[i]:
                    divisi = str.title(input('Input divisi:  '))
                    level = str.title(input('Input level:  '))
                    jabatan = str.title(input('Input jabatan:  '))
                    gaji = int(input('Input gaji: '))
                    cek = str(input('Konfirmasi ulang untuk mengupdate data ini (Y/N)  ')).capitalize()
                    if cek == 'Y':
                        karyawan[i]['divisi'] = divisi
                        karyawan[i]['level'] = level
                        karyawan[i]['jabatan'] = jabatan
                        karyawan[i]['gaji'] = gaji
                        lihat_karyawan(karyawan)
                        continue
                    else:
                        print('Data tidak disimpan')
                        lihat_karyawan(karyawan)
                        break
        cek = str(input('Apakah anda ingin mengupdate data lagi? (Y/N) '))
        if cek == 'Y':
            continue
        else:
            break
    return

def hapus(karyawan):
    lihat_karyawan(karyawan)
    while True:
        index_karyawan = int(input('Input nomor index data karyawan yang ingin dihapus:  '))
        cek = str(input('Konfirmasi ulang untuk menghapus data (Y/N)  '))
        if cek == 'Y':
            del karyawan[index_karyawan]
            lihat_karyawan(karyawan)
            print('Data telah dihapus')
        else:
            continue
        return
    


while True:
    menu()
    pilihan_menu = int(input('Input angka menu:  '))
    if(pilihan_menu == 1):
        while True:
            menu1()
            pilih = pilih_opsi()
            if(pilih == 1):
                while True:
                    print('''
                    ====================================
                        MENU 1 DAFTAR DATA KARYAWAN
                    ====================================
                    ''')
                    pilih_karyawan()
                    pilih = pilih_opsi()
                    if(pilih == 1):
                        print('Daftar Data Karyawan Tetap\n')
                        lihat_karyawan(karyawan_tetap)
                    elif(pilih == 2):
                        print('Daftar Data Staff Magang\n')
                        lihat_karyawan(staff_magang)
                    elif(pilih == 3):
                        break
                    else: 
                        print('Menu tidak tersedia')
                        continue
                    pilih = kembali()
                    if(pilih == 'Y'):
                        break
                    else:
                        continue
            elif(pilih == 2):
                break
            else: 
                print('Menu tidak tersedia')
                continue
    elif(pilihan_menu == 2):
        while True:
            menu2()
            pilih = pilih_opsi()
            if(pilih == 1):
                while True:
                    print('''
                    ====================================
                       MENU 2.1 TAMBAH DATA KARYAWAN
                    ====================================
                    ''')
                    pilih_karyawan()
                    pilih = pilih_opsi()
                    if(pilih == 1):
                        tambah(karyawan_tetap)
                    elif(pilih == 2):
                        tambah(staff_magang)
                    elif(pilih == 3):
                        break
                    else:
                        print('Pilihan tidak tersedia (Pilih 1-3)')
                              
                    pilih = kembali()
                    if(pilih == 'Y'):
                        break
                    else:
                        continue
            elif(pilih == 2):
                while True:
                    print('''
                    ====================================
                      Menu 2.2 UPDATE DATA KARYAWAN
                    ====================================
                    ''')
                    pilih_karyawan()
                    pilih = pilih_opsi()
                    if(pilih == 1):
                        update(karyawan_tetap)
                    elif(pilih == 2):
                        update(staff_magang)
                    elif(pilih == 3):
                        break
                    else:
                        print('Pilihan tidak tersedia (Pilih 1-3)')
                    pilih = kembali()
                    if(pilih == 'Y'):
                        break
                    else:
                        continue
            elif(pilih == 3):
                break
            else:
                print('Pilihan tidak tersedia (Pilih 1-3)')
                continue
    elif(pilihan_menu == 3):
        while True:
            print('''
            ====================================
              MENU 3 MENGHAPUS DATA KARYAWAN
            ====================================
            ''')
            pilih_karyawan()
            pilih = pilih_opsi()
            if(pilih == 1):
                hapus(karyawan_tetap)
            elif(pilih == 2):
                hapus(staff_magang)
            elif(pilih == 3):
                break
            else:
                print('Pilihan tidak tersedia (Pilih 1-3)')
            pilih = kembali()
            if(pilih == 'Y'):
                break
            else:
                continue
    elif(pilihan_menu == 4):
        break
    else:
        print('Pilihan yang anda masukkan salah')
        continue