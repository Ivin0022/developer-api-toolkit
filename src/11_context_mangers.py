
class ContextManager(): 
    is_being_edited = False

    def __init__(self): 
        print('init method called', self.is_being_edited)

    def __enter__(self): 
        print('enter method called') 
        return self
      
    def __exit__(self, exc_type, exc_value, exc_traceback): 
        print('exit method called',) 
        
    def print_a(self):
        print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
  
c = ContextManager()


with c as manager: 
    print('with statement block') 
    manager.print_a()
