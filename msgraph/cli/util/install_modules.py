from os import path, getcwd, pardir, listdir
import subprocess
import sys


def install():
    command_modules = path.join(getcwd(), pardir, 'command_modules')

    for module in listdir(command_modules):
        if path.isdir(path.join(command_modules, module)):
            try:
                subprocess.check_call([
                    sys.executable, '-m', 'pip', 'install',
                    path.join(command_modules, module, '.')
                ])
            except Exception as err:
                print(err)


if __name__ == '__main__':
    install()
