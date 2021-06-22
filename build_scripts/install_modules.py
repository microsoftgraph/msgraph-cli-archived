from os import path, getcwd, pardir, listdir
import subprocess
import sys


def install():
    command_modules = path.join(getcwd(), pardir, 'msgraph', 'cli', 'command_modules')

    for module in listdir(command_modules):
        try:
            subprocess.check_call(
                [sys.executable, '-m', 'pip', 'install',
                 path.join(command_modules, module, '.')])
        except Exception as err:
            print(err)


if __name__ == '__main__':
    install()
