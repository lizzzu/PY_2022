from utils import process_item

if __name__ == '__main__':
    while 1:
        x = input('Enter integer or \'q\' to quit: ')
        if x == 'q': break
        print(process_item(int(x)))
