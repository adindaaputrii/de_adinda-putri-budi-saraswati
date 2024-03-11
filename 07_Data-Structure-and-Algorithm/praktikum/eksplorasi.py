import uuid

class Pengeluaran:
    def __init__(self, nama, jumlah):
        self.id = uuid.uuid4()
        self.nama = nama 
        self.jumlah = jumlah 

data_pengeluaran = []

def tambah_pengeluaran(data_pengeluaran):
    nama = input("Enter Expense Name: ")
    jumlah = int(input("Enter Amount: "))
    data_pengeluaran.append(Pengeluaran(nama, jumlah))
    print("Data added!\n")

def lihat_pengeluaran(data_pengeluaran):
    total_pengeluaran = 0
    print("All Expenses")
    if not data_pengeluaran:
        print("Tidak Ada Pengeluaran!\n")
        return
    for item in data_pengeluaran:
        print("==")
        print(f"ID: {item.id} \nNama: {item.nama} \nJumlah: {item.jumlah}")
        total_pengeluaran += item.jumlah
    print("==")
    print(f"== TOTAL: {total_pengeluaran} ==\n")

def update_pengeluaran(data_pengeluaran):
    if not data_pengeluaran:
        print("Tidak Ada Pengeluaran!\n")
        return
    item_terakhir = data_pengeluaran[-1]
    print("-- Last Expense --")
    print(f"ID: {item_terakhir.id} \nNama: {item_terakhir.nama} \nJumlah: {item_terakhir.jumlah} \n")
    id_hapus = input("Enter Expense ID: ")
    nama_baru = input("Enter New Expense Name: ")
    jumlah_baru = int(input("Enter New Amount: "))
    item_terakhir.nama = nama_baru
    item_terakhir.jumlah = jumlah_baru
    print("Data Updated!\n")

def hapus_pengeluaran(data_pengeluaran):
    if not data_pengeluaran:
        print("Tidak Ada Pengeluaran!\n")
        return
    id_pengeluaran = input("Enter expense ID: ")
    for i, item in enumerate(data_pengeluaran):
        if str(item.id) == id_pengeluaran:
            del data_pengeluaran[i]
            print("Data Deleted!\n")
            break
        else:
            print("ID Pengeluaran Tidak Ditemukan\n")

while True:
    print("== MENU ==")
    print("1. Create New Expense Data")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Detele Expense")
    print("5. Exit")
        
    choice = input("Enter Your Choice: ")

    if choice == "1":
        tambah_pengeluaran(data_pengeluaran)
    elif choice == "2":
        lihat_pengeluaran(data_pengeluaran)
    elif choice == "3":
        update_pengeluaran(data_pengeluaran)
    elif choice == "4":
        hapus_pengeluaran(data_pengeluaran)
    elif choice == "5":
        print("Bye...")
        break
    else:
        print("Pilihan Tidak Ada!\n")