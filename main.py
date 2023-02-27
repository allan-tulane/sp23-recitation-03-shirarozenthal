"""
CMPS 2200  Recitation 3.
See recitation-03.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def quadratic_multiply(x, y):
  return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    ### TODO

    if (len(x.binary_vec) > 1 or len(y.binary_vec) > 1):
      x.binary_vec, y.binary_vec = pad(x.binary_vec, y.binary_vec)

    n = len(x.binary_vec)
    
    if (n <= 1):
      return BinaryNumber(x.decimal_val & y.decimal_val)

    xl, xr = split_number(x.binary_vec)
    yl, yr = split_number(y.binary_vec)

    l = bit_shift(_quadratic_multiply(xl, yl), n)

    ml = _quadratic_multiply(xl, yr)
    mr = _quadratic_multiply(xr, yl)
  
    m = bit_shift(BinaryNumber(ml.decimal_val + mr.decimal_val), n//2)

    r = _quadratic_multiply(xr, yr)

    return BinaryNumber(l.decimal_val + m.decimal_val + r.decimal_val)
    ###


## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert quadratic_multiply(BinaryNumber(3), BinaryNumber(2)) == 3*2
    assert quadratic_multiply(BinaryNumber(6), BinaryNumber(6)) == 6*6
    assert quadratic_multiply(BinaryNumber(60), BinaryNumber(6)) == 60*6
    assert quadratic_multiply(BinaryNumber(13), BinaryNumber(7)) == 13*7
    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000
