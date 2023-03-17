import os

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self, page, page_size):
        start = (page - 1) * page_size
        end = start + page_size
        current = self.head
        i = 0
        while current and i < end:
            if i >= start:
                print(current.data)
            current = current.next
            i += 1
        if i < start:
            print("Page tidak valid.")
        elif not current:
            print("Tidak ada data.")

    def count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count


def main():
    hp_list = LinkedList()
    hp_list.add("Samsung Galaxy A12")
    hp_list.add("Samsung Galaxy A22")
    hp_list.add("Samsung Galaxy A32")
    hp_list.add("Samsung Galaxy A42")
    hp_list.add("Samsung Galaxy A52")
    hp_list.add("Samsung Galaxy A72")
    hp_list.add("Samsung Galaxy S20")
    hp_list.add("Samsung Galaxy S21")
    hp_list.add("Samsung Galaxy S22")
    hp_list.add("Samsung Galaxy Z Flip")
    hp_list.add("Samsung Galaxy Z Fold2")
    hp_list.add("Samsung Galaxy Z Fold3")
    
    page_size = 3
    current_page = 1
    total_pages = (hp_list.count() + page_size - 1) // page_size
    while True:
        print("\n\tDaftar lisat HP SAMSUNG")
        print(f"\nHalaman {current_page}/{total_pages}:")
        hp_list.display(current_page, page_size)
        print("\nMenu:")
        print("1. Halaman selanjutnya")
        print("2. Halaman sebelumnya")
        print("3. Keluar")
        choice = input("Pilih menu: ") 
        if choice == "1":
            if current_page < total_pages:
                current_page += 1
            else:
                print("Halaman terakhir.")
        elif choice == "2":
            if current_page > 1:
                current_page -= 1
            else:
                print("Halaman pertama.")
        elif choice == "3":
            print("Anda telah Keluar.")
            break
        else:
            print("Mohon maaf tidak ada di menu.")

if __name__ == "__main__":
    main()
