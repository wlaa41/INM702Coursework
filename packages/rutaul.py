from colorama import Fore, Back, Style

def pg(*value, **kargs):
    '''
    print with green color
    '''
    #print(Back.BLACK + '')
    print(Fore.LIGHTGREEN_EX ,end='')
    print(*value, **kargs)
    print(Style.RESET_ALL, end='')

print(Back.GREEN + "")
# print(Back.YELLOW + "")
print(Style.RESET_ALL)
# print('AND THIS TO SEE ')
pg('........... 🆂  🆃  🅰   🆁  🆃 ...........')


class setPrint:

    @staticmethod
    def green(text='',end= '' ,**kargs):
        
        print(Fore.LIGHTGREEN_EX + '\033[F' + str(text), end=end, **kargs)

    @staticmethod
    def test():
        '''
        print with red color
        '''
        print('eeee')


    @staticmethod
    def red(text='', end='', **kargs):
        '''
        print with red color
        '''
        print(Fore.RED  + '\033[F' + str(text), end=end, **kargs)

        #print(Back.BLACK + '')

    @staticmethod
    def resetall(text='',end ='', **kargs):
        print(Style.RESET_ALL,+ '\033[F' + str(text), end=end, **kargs)



def pb(*value, **kargs):
    '''
    print with green blue
    '''
    #print(Back.BLACK + '')
    print(Fore.BLUE, end='')
    print(*value, **kargs)
    print(Style.RESET_ALL, end='')



def py(*value, **kargs):
    '''
    print with green color
    '''
    #print(Back.BLACK + '')
    print(Fore.LIGHTYELLOW_EX, end='')
    print(*value, **kargs)
    print(Style.RESET_ALL, end='')
    
def po(*value, **kargs):
    '''
    print with orange color
    '''
    #print(Back.BLACK + '')
    print(Fore.YELLOW, end='')
    print(*value, **kargs)
    print(Style.RESET_ALL, end='')


def pm(*value, **kargs):
    '''
    print with magenta color
    '''
    #print(Back.BLACK + '')
    print(Fore.MAGENTA, end='')
    print(*value, **kargs)
    print(Style.RESET_ALL, end='')


def pr(*value, **kargs):
    '''
    print with red color
    '''
    #print(Back.BLACK + '')
    print(Fore.LIGHTRED_EX, end='')
    print(*value, **kargs)
    print(Style.RESET_ALL, end='')


'''
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')


def pbg(text):
    print(Back.GREEN + text)

def pbr(text):
    print(Back.RED + text)
'''
if __name__  == "__main__":
    pg('test1')
    pm('test2')
    pr('test3')
    py('test4')
    pb('test5')
    # pb('test5')
    po('test6')
    pg(Fore.__dict__)
    print(type(Fore))
    print('...................................')
    setPrint.green()
    print('ee', {'will': 'eee'})
    print('....................................')
    setPrint.green(end='\n')
    print('ee')



