import os

def run(**args):
    print("[*] DirFuzz")
    pwd = os.path.realpath('.')
    files = os.listdir('.')
    return (pwd, files)

pwd, files = run()
print(pwd)
for _file in files:
    print("- {}".format(_file))
