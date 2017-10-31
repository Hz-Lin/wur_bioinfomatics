import sys

len_argv = len(sys.argv)
if len_argv == 1:
    sys.stderr.write("you haven't give me any number")
if len_argv >1:
    result_n = 1
    for n in range(1,len_argv):
        try:
            n = float(sys.argv[n])
        except:
            sys.stderr.write('this is not a number')
        result_n = result_n * n
    sys.stderr.write('miltiply result is %d\n' % (result_n))