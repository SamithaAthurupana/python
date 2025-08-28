# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Bult-in.

'''def func1():
    a = 1 # local
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()'''


# if __name__ = __main_: (this script can be import Or run standalone)
#                 Functions and classes in this module can be reuses
#                 without the main block code executing

def main():
    pass

if __name__ == '__main__':
    main()











