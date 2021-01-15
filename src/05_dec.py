

def dec(string):
    def warp(func):
        def inner():
            print('dev ' + string)
            func()
            print('end ' + string)
        return inner
    return warp


 
@dec('sasdasd')
def a_func_that_takes_a_long_time():
    print('doing something')
    return 'hwlo world'


a_func_that_takes_a_long_time()


