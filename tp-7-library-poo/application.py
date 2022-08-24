class Application:
    def __init__(self):
      pass

    def show_options(self):
      pass
    
    def run_option(self, option):
      pass
    
    def run(self):
        while(True):
            self.show_options()
            self.run_option(int(input('Please enter an option:')))
