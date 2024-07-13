from datetime import datetime
import random
import numpy as np
from colorama import Fore, Style, init

# Initialize colorama
init()

print(Fore.LIGHTBLUE_EX + "S.MAHESHWARI BOOKS")
print("------------------")
print("Collection of books" + Style.RESET_ALL)

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

# Define the studyBooks class
class studyBooks:
    def __init__(self, title, author, edition, price):
        self.title = title
        self.author = author
        self.edition = edition
        self.price = price

    def display_info(self):
        return f"{Fore.GREEN}Title: {self.title}\nAuthor: {self.author}\nEdition: {self.edition}\nPrice: Rs{self.price:.2f}{Style.RESET_ALL}"

# Define the comics class
class comics:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        return f"{Fore.MAGENTA}Title: {self.title}\nAuthor: {self.author}\nPrice: Rs{self.price:.2f}{Style.RESET_ALL}"

# Create instances of the Book class
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960, 12000, 0.10)
book2 = Book("1984                 ", "George Orwell", 1949, 2400, 0.10)
book3 = Book("Mahabharatham        ", "Vinaponavan", 1667, 15000, 0.10)
book4 = Book("Ramayanam            ", "Valmigi", 1899, 15670, 0.10)

# Create instances of the studyBooks class
codebook1 = studyBooks("Python for Beginners", "Guido Van Rossum", "6th edition", 1200)
codebook2 = studyBooks("Java for Beginners  ", "J Balagurusamy", "7th edition", 780)
codebook3 = studyBooks("C# for Advanced     ", "Anders Hejlsberg", "3rd edition", 890)
codebook4 = studyBooks("C++ for Beginners   ", "Bjarne Stroustrup", "5th edition", 570)

# Create instances of the comics class 
comicsbook1 = comics("Maus                   ", "Art Spiegelman", 460)
comicsbook2 = comics("ALL Star Superman Vol2 ", "Grant Morrison", 570)
comicsbook3 = comics("Anya's Ghost           ", "Vera Brosgol", 780)
comicsbook4 = comics("Batman: The Dark Knight", "Frank Miller", 1000)

# List of books, codebooks, and comicsbook
books = [book1, book2, book3, book4]
codebooks = [codebook1, codebook2, codebook3, codebook4]
comicsbooks = [comicsbook1, comicsbook2, comicsbook3, comicsbook4]

# Display information for all books
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

# Generate the bill receipt for the selected books
def generate_receipt(selected_books):
    total_price = 0
    GST_RATE = 0.03
    bill_number = np.random.randint(100, 999)

    receipt = Fore.YELLOW + "\t\tS. MAHESHWARI BOOKS\n"
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
    
    for book in selected_books:
        if isinstance(book, Book):
            discounted_price = book.discounted_price()
            total_price += discounted_price
            receipt +=Style.BRIGHT+Fore.YELLOW+f"\t{book.title[:15]} \tRs{discounted_price:.2f}\n"
        else:
            total_price += book.price
            receipt +=Style.BRIGHT+Fore.YELLOW+f"\t{book.title[:15]} \tRs{book.price:.2f}\n"
    
    GST_amount = total_price * GST_RATE
    final_amount = total_price + GST_amount
    
    receipt += "\t------------------------------------\n"
    receipt += f"\tNumber of Items: {len(selected_books)}\n"
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

selected_books = []

# Select a general book
general_book_index = int(input("\nEnter the number of the general book you want to view: ")) - 1
if 0 <= general_book_index < len(books):
    print("\nSelected General Book:")
    print(books[general_book_index].display_info())
    
    # Ask if the user wants to buy the selected book
    buy_general = input("\nDo you want to buy this book? (yes/no): ").lower()
    
    if buy_general == 'yes':
        selected_books.append(books[general_book_index])
        buy_another = input("\nDo you want to buy another book? (yes/no): ").lower()
        
        while buy_another == 'yes':
            # Select another book
            another_book_index = int(input("\nEnter the number of the book you want to buy: ")) - 1
            if 0 <= another_book_index < len(books) and another_book_index != general_book_index:
                selected_books.append(books[another_book_index])
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
            selected_books.append(codebooks[selected_book_index])
            buy_another = input("\nDo you want to buy another book? (yes/no): ").lower()
            
            while buy_another == 'yes':
                # Select another book
                another_book_index = int(input("\nEnter the number of the book you want to buy: ")) - 1
                if 0 <= another_book_index < len(codebooks):
                    selected_books.append(codebooks[another_book_index])
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
            selected_books.append(comicsbooks[selected_book_index])
            buy_another = input("\nDo you want to buy another book? (yes/no): ").lower()
            
            while buy_another == 'yes':
                # Select another book
                another_book_index = int(input("\nEnter the number of the book you want to buy: ")) - 1
                if 0 <= another_book_index < len(comicsbooks):
                    selected_books.append(comicsbooks[another_book_index])
                    buy_another = input("\nDo you want to buy another book? (yes/no): ").lower()
                else:
                    print("Invalid book number or the same book selected again.")
                    break
    else:
        print("Invalid book number.")
else:
    print("Invalid book type.")

# Generate and print the receipt if any book is selected
if selected_books:
    receipt = generate_receipt(selected_books)
    print(receipt)

    cancel_book = input("\nDo you want to cancel any book? (yes/no): ").lower()
    if cancel_book == 'yes':
        cancel_index = int(input("Enter the number of the book you want to cancel: ")) - 1
        if 0 <= cancel_index < len(selected_books):
            selected_books.pop(cancel_index)
            receipt = generate_receipt(selected_books)
            print(receipt)
        else:
            print("Invalid book number.")
    else:
        print("\nThank you for shopping....\n")
else:
    print("You chose not to buy any book.")
