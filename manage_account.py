import library
from config import cls
lbm = library.Library_Management_System.Book()


def display_res():
    lbm.Reservation_status_print()

def display_bor():
    cls()
    print('{0:9} | {1:9} | {2:9} | {3}\n'.format('BORO ID','USER ID','BOOK ID','BORROWED ON'))
    with open('bin\\books\\borrowed_book.txt') as lines:
        for line in lines:
            line=line.strip().split('-')
            print('{0:9} | {1:9} | {2:9} | {3}'.format(line[0],line[1],line[2],line[3].replace(',','/')))

def display_ret():
    cls()
    print('{0:10} | {1:13} | {2:4} | {3}\n'.format('CONTACT','ISBN','DAY','RETURNED ON'))
    with open('bin\\books\\returned_book.txt') as lines:
        for line in lines:
            line=line.strip().split('-')
            print('{0:10} | {1:13} | {2:4} | {3}'.format(line[0],line[1],line[2],line[3].replace(',','/')))


