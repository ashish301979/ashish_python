class CM(object):
    def __enter__(self):
        print "Rais IO E 1"
        raise IOError()
        return self
def __exit__(self,exc_type, exc_val, exc_tb):
    print "exiting"
    return False
c=CM()
with c:
    try:
        print "Rais IO E 2"
        raise ValueError()
    except ValueError:
        print "T C"
