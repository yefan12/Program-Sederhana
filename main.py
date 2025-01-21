# Daftar untuk menyimpan data produk
produk_list = []

# Fungsi Menambah Produk
def add_product():
    """
    Fungsi untuk menambahkan produk baru ke dalam daftar produk.
    Pengguna diminta untuk memasukkan ID, Nama, Kategori, dan Jumlah Stok produk.
    """
    product_id = input("Masukkan ID Produk: ")
    name = input("Masukkan Nama Produk: ")
    category = input("Masukkan Kategori Produk: ")
    stock = int(input("Masukkan Jumlah Stok: "))
    product = {"ID": product_id, "Name": name, "Category": category, "Stock": stock}
    produk_list.append(product)
    print("Produk berhasil ditambahkan.\n")

# Fungsi Menampilkan Semua Produk
def display_products():
    """
    Fungsi untuk menampilkan daftar semua produk yang ada di gudang.
    Produk ditampilkan dalam format tabel dengan kolom ID, Nama, Kategori, dan Jumlah Stok.
    """
    if not produk_list:
        print("Tidak ada produk dalam daftar.\n")
        return
    print("\nDaftar Produk di Gudang:")
    print(f"{'ID':<10} {'Nama':<30} {'Kategori':<20} {'Stok':<5}")
    print("-" * 70)
    for product in produk_list:
        print(f"{product['ID']:<10} {product['Name']:<30} {product['Category']:<20} {product['Stock']:<5}")
    print()

# Fungsi Menghapus Produk
def delete_product():
    """
    Fungsi untuk menghapus produk berdasarkan ID yang dimasukkan pengguna.
    """
    product_id = input("Masukkan ID Produk yang ingin dihapus: ")
    global produk_list
    for product in produk_list:
        if product['ID'] == product_id:
            produk_list.remove(product)
            print("Produk berhasil dihapus.\n")
            return
    print("Produk tidak ditemukan.\n")

# Fungsi Mengupdate Produk
def update_product():
    """
    Fungsi untuk memperbarui data produk berdasarkan ID yang dimasukkan pengguna.
    Pengguna dapat memperbarui Nama, Kategori, dan Jumlah Stok.
    """
    product_id = input("Masukkan ID Produk yang ingin diupdate: ")
    for product in produk_list:
        if product['ID'] == product_id:
            new_name = input("Masukkan Nama Baru: ")
            new_category = input("Masukkan Kategori Baru: ")
            new_stock = int(input("Masukkan Jumlah Stok Baru: "))
            product['Name'] = new_name
            product['Category'] = new_category
            product['Stock'] = new_stock
            print("Produk berhasil diupdate.\n")
            return
    print("Produk tidak ditemukan.\n")

# Fungsi Pencarian Produk Berdasarkan Nama
def search_product_by_name():
    """
    Fungsi untuk mencari produk berdasarkan nama.
    Jika produk ditemukan, informasi produk akan ditampilkan.
    """
    target_name = input("Masukkan Nama Produk yang ingin dicari: ")
    found = False
    for product in produk_list:
        if target_name.lower() in product['Name'].lower():
            print(f"\nProduk Ditemukan: {product}")
            found = True
            break
    if not found:
        print("Produk tidak ditemukan.\n")

# Fungsi Menampilkan Produk yang Terurut Berdasarkan Stok
def sort_products_by_stock():
    """
    Fungsi untuk mengurutkan produk berdasarkan jumlah stok.
    Produk akan diurutkan secara ascending.
    """
    global produk_list
    produk_list = sorted(produk_list, key=lambda x: x['Stock'])
    print("Produk telah diurutkan berdasarkan jumlah stok.\n")

# Menu Utama
def main_menu():
    """
    Fungsi untuk menampilkan menu utama dan menangani input pilihan pengguna.
    Menu utama memungkinkan pengguna untuk memilih operasi yang ingin dilakukan seperti
    menambah, mengupdate, menghapus produk, atau menampilkan daftar produk.
    """
    while True:
        print("=== Sistem Manajemen Produk di Gudang ===")
        print("1. Tambah Produk")
        print("2. Tampilkan Semua Produk")
        print("3. Update Produk")
        print("4. Hapus Produk")
        print("5. Cari Produk Berdasarkan Nama")
        print("6. Urutkan Produk Berdasarkan Stok")
        print("7. Keluar")
        choice = input("Pilih menu (1-7): ")
        print()
        if choice == "1":
            add_product()
        elif choice == "2":
            display_products()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            search_product_by_name()
        elif choice == "6":
            sort_products_by_stock()
        elif choice == "7":
            print("Terima kasih telah menggunakan Sistem Manajemen Produk di Gudang!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

# Jalankan Program
if __name__ == "__main__":
    main_menu()
