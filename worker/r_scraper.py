import subprocess

SCRIPT = 'hello.R'
BASE_DIR = 'r_classifier'

def run_script(script, args=[]):
    command = ['Rscript', script] + args
    out = subprocess.Popen( command, stdout=subprocess.PIPE).communicate()[0]
    print out
    return out

def classify_photo(photo_file):
    print photo_file
    script = '%s/%s' % (BASE_DIR, SCRIPT)
    return run_script(script, args=[photo_file])
