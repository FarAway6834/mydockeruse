from sys import argv as _a

@(lambda f : lambda x : f(_a[2] if len(a) > 3 else input('file name : ')) if x == '-r' else x)
def r(f):
	with open(f) as fp: return fp.read()

main = lambda x = input('docker img : ') if len(_a) < 2 else r(_a[1]): default_docker_environment_manager(x)

main()