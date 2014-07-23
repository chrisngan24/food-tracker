import subprocess

SCRIPT = 'classify.R'
BASE_DIR = 'r_classifier'

def run_script(script, args=[]):
    command = ('Rscript').split() + [script] + args
    import pdb; pdb.set_trace()
    out = subprocess.Popen( command, 
            cwd=BASE_DIR,
            stdout=subprocess.PIPE).communicate()[0]
    print out
    return out

def classify_photo(photo_file):
    print photo_file
    #script = '%s/%s' % (BASE_DIR, SCRIPT)
    script = SCRIPT
    return run_script(script, args=['../' + photo_file])
