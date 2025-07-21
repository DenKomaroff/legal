from services import init
# from .argus import argus
from adapters import ExtLegalEntityInfo
import sys


def main():
    # print(sys.builtin_module_names, end='\n\n')
    # print('sys.path:', sys.path)
    init('services')


if __name__ == '__main__':
    main()
