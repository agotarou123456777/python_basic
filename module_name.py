import time



def func():
    print('    This is func() in test_module.py')
    print('    __name__ is', __name__)


if __name__ == '__main__':
    print("Start if __name__ == '__main__'")
    print('call func()')
    func()
    
    print('This is test_main.py')
    print('test_module.__name__ is', time.sleep.__name__)

    print('---')
    print('call test_module.func()')
