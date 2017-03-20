from subprocess import Popen

def launch(fname): 
    p = Popen(fname, cwd=r"C:\Users\crazy\Dropbox\Wyatts Projects\Python\Audio\COMMAND")
    stdout, stderr = p.communicate()
