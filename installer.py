import os
import sys
from pip import main

error_log = open('error_log.txt', 'w')

def install(package):
    try:
        main(['install'] + [str(package)])
    except Exception as e:
        try:
            main(['uninstall'] + [str(package)])
        except Exception as e:
            error_log.write(str(e))
        install(package)
        error_log.write(str(e))

if __name__ == '__main__':
    f = open('requirements.txt', 'r')
    for line in f:
        install(line)
    f.close()
    error_log.close()
