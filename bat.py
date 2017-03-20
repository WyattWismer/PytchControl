from subprocess import Popen

def launch(fname): 
    p = Popen(fname, cwd=r".")
    stdout, stderr = p.communicate()
