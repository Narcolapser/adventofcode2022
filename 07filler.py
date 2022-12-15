import sys
a = '0' * int(sys.argv[1])
open(sys.argv[2],'w').write(a)
