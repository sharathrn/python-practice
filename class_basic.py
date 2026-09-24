class Computer:
    
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
        print("Inside Init")
        
    def config(self):
        print("Configuration is:", self.cpu, self.ram)
        
comp1 = Computer("i5", "16GB")
comp1.config()