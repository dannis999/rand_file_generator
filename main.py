import os,string,random

_s = string.ascii_letters + string.digits + '+-_ ' + ('.' * 3)

def gen_one():
    n = random.randrange(3,30)
    fn = ''.join((random.choice(_s) for _ in range(n)))
    with open(fn,'wb') as f:
        n = random.randrange(1,1<<28)
        f.write(os.urandom(n))

def gen_many():
    while True:
        try:
            gen_one()
        except Exception:
            pass

if __name__=='__main__':
    gen_many()
