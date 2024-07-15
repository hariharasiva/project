from datetime import datetime
import random
import numpy as np
from colorama import Fore, Style, init

# Initialize colorama
init()

print(Fore.LIGHTBLUE_EX + "S.MAHESHWARI BOOKS")
print("------------------")
print("Collection of books and stationary items" + Style.RESET_ALL)

# Define the Book class
class Book:
    def __init__(self, title, author, year, price, discount):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.discount = discount

    def display_info(self):
        return f"{Fore.RED}Title: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nPrice: Rs{self.price:.2f}\nDiscount: {self.discount*100}%{Style.RESET_ALL}"
            
    def discounted_price(self):
        discount_amount = self.price * self.discount
        return self.price - discount_amount

# Define the StudyBooks class
class StudyBooks:
    def __init__(self, title, author, edition, price):
        self.title = title
        self.author = author
        self.edition = edition
        self.price = price

    def display_info(self):
        return f"{Fore.GREEN}Title: {self.title}\nAuthor: {self.author}\nEdition: {self.edition}\nPrice: Rs{self.price:.2f}{Style.RESET_ALL}"

# Define the Comics class
class Comics:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        return f"{Fore.MAGENTA}Title: {self.title}\nAuthor: {self.author}\nPrice: Rs{self.price:.2f}{Style.RESET_ALL}"

# Define the Stationary class
class Stationary:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        return f"{Fore.LIGHTGREEN_EX}Item: {self.name}\nPrice: Rs{self.price:.2f}{Style.RESET_ALL}"

# Create instances of the Book class
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960, 12000, 0.10)
book2 = Book("1984                 ", "George Orwell", 1949, 2400, 0.10)
book3 = Book("Mahabharatham        ", "Vinaponavan", 1667, 15000, 0.10)
book4 = Book("Ramayanam            ", "Valmigi", 1899, 15670, 0.10)

# Create instances of the StudyBooks class
codebook1 = StudyBooks("Python for Beginners", "Guido Van Rossum", "6th edition", 1200)
codebook2 = StudyBooks("Java for Beginners  ", "J Balagurusamy", "7th edition", 780)
codebook3 = StudyBooks("C# for Advanced     ", "Anders Hejlsberg", "3rd edition", 890)
codebook4 = StudyBooks("C++ for Beginners   ", "Bjarne Stroustrup", "5th edition", 570)

# Create instances of the Comics class 
comicsbook1 = Comics("Maus                   ", "Art Spiegelman", 460)
comicsbook2 = Comics("ALL Star Superman Vol2 ", "Grant Morrison", 570)
comicsbook3 = Comics("Anya's Ghost           ", "Vera Brosgol", 780)
comicsbook4 = Comics("Batman: The Dark Knight", "Frank Miller", 1000)

# Create instances of the Stationary class
pencil = Stationary("Pencil", 5)
pen = Stationary("Pen", 10)
eraser = Stationary("Eraser", 5)
long_notebook = Stationary("Long Notebook", 50)
short_notebook = Stationary("Short Notebook", 30)
Drawing_book   = Stationary("Drawing book 150GSM",450)
Scale = Stationary("30cm Scale",10)
colour_paper=Stationary("Pink colour",12)
geomentry_Box=Stationary("Geomentry_Box",120)

# List of books, codebooks, comicsbooks, and stationary 
books = [book1, book2, book3, book4]
codebooks = [codebook1, codebook2, codebook3, codebook4]
comicsbooks = [comicsbook1, comicsbook2, comicsbook3, comicsbook4]
stationary_items = [pencil, pen, eraser, long_notebook, short_notebook,Drawing_book,Scale,colour_paper]

# Display information for all books, codebooks, comicsbooks, and stationary items
print(Fore.CYAN + "Books available:" + Style.RESET_ALL)
for i, book in enumerate(books, start=1):
    print(f"\nBook {i}:")
    print(book.display_info())

print(Fore.CYAN + "\nStudy Books available:" + Style.RESET_ALL)
for i, book in enumerate(codebooks, start=1):
    print(f"\nStudy Book {i}:")
    print(book.display_info())

print(Fore.CYAN + "\nComics Available:" + Style.RESET_ALL)
for i, book in enumerate(comicsbooks, start=1):
    print(f"\nComic Book {i}:")
    print(book.display_info())

print(Fore.CYAN + "\nStationary Items Available:" + Style.RESET_ALL)
for i, item in enumerate(stationary_items, start=1):
    print(f"\nStationary Item {i}:")
    print(item.display_info())

# Generate the bill receipt for the selected items
def generate_receipt(selected_items):
    total_price = 0
    GST_RATE = 0.03
    bill_number = np.random.randint(100, 999)

    receipt = Style.BRIGHT+Fore.YELLOW + "\t\tS. MAHESHWARI BOOKS\n"
    receipt += "\t====================================\n"
    receipt += Style.BRIGHT+"\t\t   BILL RECEIPT\n"
    receipt += "\t------------------------------------\n"
    receipt += Fore.YELLOW+Style.BRIGHT+f"\t\t\t\tBill No: {bill_number}\n"
    receipt += "\t------------------------------------\n"
    receipt += f"\tDate: {datetime.now().strftime('%Y-%m-%d')}\n"
    receipt += f"\tTime: {datetime.now().strftime('%H:%M:%S')}\n"
    receipt += "\t------------------------------------\n"
    receipt += Style.BRIGHT+Fore.YELLOW+"\tItem:\t\t\tPrice:\n"
    receipt += "\t------------------------------------\n"
    
    for item in selected_items:
        if isinstance(item, Book):
            discounted_price = item.discounted_price()
            total_price += discounted_price
            receipt += Style.BRIGHT+Fore.YELLOW+f"\t{item.title[:15]} \tRs{discounted_price:.2f}\n"
        elif isinstance(item, StudyBooks):
            total_price += item.price
            receipt += Style.BRIGHT+Fore.YELLOW+f"\t{item.title[:15]} \tRs{item.price:.2f}\n"
        elif isinstance(item, Comics):
            total_price += item.price
            receipt += Style.BRIGHT+Fore.YELLOW+f"\t{item.title[:15]} \tRs{item.price:.2f}\n"
        elif isinstance(item, Stationary):
            total_price += item.price
            receipt += Style.BRIGHT+Fore.YELLOW+f"\t{item.name[:15]} \tRs{item.price:.2f}\n"
    
    GST_amount = total_price * GST_RATE
    final_amount = total_price + GST_amount
    
    receipt += "\t------------------------------------\n"
    receipt += f"\tNumber of Items: {len(selected_items)}\n"
    receipt += f"\tTotal Price:... - \tRs{total_price:.2f}\n"
    receipt += f"\tGST @ {GST_RATE*100}%: \t\tRs{GST_amount:.2f}\n"
    receipt += "\t------------------------------------\n"
    receipt += f"\tTotal Payment: \t\tRs{final_amount:.2f}\n"
    receipt += "\t====================================\n"
    receipt += "\tAddress:\n"
    receipt += "\t192/A Northcar Street,Tenkasi-627811\n"
    receipt += "\t====================================\n"
    receipt += "\t\tThank You for Shopping\n" + Style.RESET_ALL
    
    return receipt


selected_items = []

# Select a general book
general_book_index = int(input("\nEnter the number of the general book you want to view: ")) - 1
if 0 <= general_book_index < len(books):
    print("\nSelected General Book:")
    print(books[general_book_index].display_info())
    
    # Ask if the user wants to buy the selected book
    buy_general = input("\nDo you want to buy this book? (yes/no): ").lower()
    
    if buy_general == 'yes':
        selected_items.append(books[general_book_index])
        buy_another = input("\nDo you want to buy another book? (yes/no): ").lower()
        
        while buy_another == 'yes':
            # Select another book
            another_book_index = int(input("\nEnter the number of the book you want to buy: ")) - 1
            if 0 <= another_book_index < len(books) and another_book_index != general_book_index:
                selected_items.append(books[another_book_index])
                buy_another = input("\nDo you want to buy another book? (yes/no): ").lower()
            else:
                print("Invalid book number or the same book selected again.")
                break
else:
    print("Invalid book number.")

# Select another book from study
book_type = input("\nDo you want to view 'study' books? :").lower()
if book_type == 'study':
    selected_book_index = int(input("\nEnter the number of the study book you want to view: ")) - 1
    if 0 <= selected_book_index < len(codebooks):
        print("\nSelected Study Book:")
        print(codebooks[selected_book_index].display_info())
        
        # Ask if the user wants to buy the selected book
        buy_study = input("\nDo you want to buy this book? (yes/no): ").lower()
        
        if buy_study == 'yes':
            selected_items.append(codebooks[selected_book_index])
            buy_another = input("\nDo you want to buy another book? (yes/no): ").lower()
            
            while buy_another == 'yes':
                # Select another book
                another_book_index = int(input("\nEnter the number of the book you want to buy: ")) - 1
                if 0 <= another_book_index < len(codebooks):
                    selected_items.append(codebooks[another_book_index])
                    buy_another = input("\nDo you want to buy another book? (yes/no): ").lower()
                else:
                    print("Invalid book number or the same book selected again.")
                    break
    else:
        print("Invalid book number.")

# Select another book from comics        
book_type=input("\nDo you want to view 'comics' books? :").lower()
if book_type == 'comics':
    selected_book_index = int(input("\nEnter the number of the comics book you want to view: ")) - 1
    if 0 <= selected_book_index < len(comicsbooks):
        print("\nSelected Comics Book:")
        print(comicsbooks[selected_book_index].display_info())
        
        # Ask if the user wants to buy the selected book
        buy_comics = input("\nDo you want to buy this book? (yes/no): ").lower()
        if buy_comics == 'yes':
            selected_items.append(comicsbooks[selected_book_index])
            buy_another = input("\nDo you want to buy another book? (yes/no): ").lower()
            
            while buy_another == 'yes':
                # Select another book
                another_book_index = int(input("\nEnter the number of the book you want to buy: ")) - 1
                if 0 <= another_book_index < len(comicsbooks):
                    selected_items.append(comicsbooks[another_book_index])
                    buy_another = input("\nDo you want to buy another book? (yes/no): ").lower()
                else:
                    print("Invalid book number or the same book selected again.")
                    break
    else:
        print("Invalid book number.")

# Select stationary items
item_type = input("\nDo you want to view 'stationary' items? :").lower()
if item_type == 'stationary':
    selected_item_index = int(input("\nEnter the number of the stationary item you want to view: ")) - 1
    if 0 <= selected_item_index < len(stationary_items):
        print("\nSelected Stationary Item:")
        print(stationary_items[selected_item_index].display_info())
        
        # Ask if the user wants to buy the selected item
        buy_stationary = input("\nDo you want to buy this item? (yes/no): ").lower()
        if buy_stationary == 'yes':
            selected_items.append(stationary_items[selected_item_index])
            buy_another = input("\nDo you want to buy another item? (yes/no): ").lower()
            
            while buy_another == 'yes':
                # Select another item
                another_item_index = int(input("\nEnter the number of the item you want to buy: ")) - 1
                if 0 <= another_item_index < len(stationary_items):
                    selected_items.append(stationary_items[another_item_index])
                    buy_another = input("\nDo you want to buy another item? (yes/no): ").lower()
                else:
                    print("Invalid item number or the same item selected again.")
                    break
    else:
        print("Invalid item number.")
else:
    print("Invalid item type.")

# Generate and print the receipt if any item is selected
if selected_items:
    receipt = generate_receipt(selected_items)
    print(receipt)

    cancel_item = input("\nDo you want to cancel any item? (yes/no): ").lower()
    if cancel_item == 'yes':
        cancel_index = int(input("Enter the number of the item you want to cancel: ")) - 1
        if 0 <= cancel_index < len(selected_items):
            selected_items.pop(cancel_index)
            receipt = generate_receipt(selected_items)
            print(receipt)
        else:
            print("Invalid item number.")
    else:
        print("\nThank you for shopping....\n")
else:
    print("You chose not to buy any item.")
