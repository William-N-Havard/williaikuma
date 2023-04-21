#!usr/bin/env python
# -*- coding: utf8 -*-
#
# -----------------------------------------------------------------------------
#   File: App.py (as part of project Williaikuma)
#   Created: 14/04/2023 12:13
#   Last Modified: 14/04/2023 12:13
# -----------------------------------------------------------------------------
#   Author: William N. Havard
#           Postdoctoral Researcher
#
#   Mail  : william.havard@ens.fr / william.havard@gmail.com
#
#   Institution: ENS / Laboratoire de Sciences Cognitives et Psycholinguistique
#
# ------------------------------------------------------------------------------
#   Description:
#       •
# -----------------------------------------------------------------------------

import os
import shutil

def make_win_exe():
    this_files_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    specs_path = os.path.join(this_files_path, 'other', 'win-exe', 'spec')
    build_path = os.path.join(this_files_path, 'other', 'win-exe', 'build')
    dist_path = os.path.join(this_files_path, 'other', 'win-exe', 'dist')

    args = [
        'pyinstaller',
        '--noconfirm',
        '--clean',
        '--onefile',
        '--windowed',
        '--hidden-import', '"babel.numbers"',
        '--add-data', '"{};{}"'.format(os.path.join(this_files_path, 'williaikuma', 'assets'),
                                       os.path.join('.','williaikuma','assets')),
        '--specpath', '{}'.format(specs_path),
        '--distpath', '{}'.format(dist_path),
        '--workpath', '{}'.format(build_path),
        '--collect-submodules', '"williaikuma"',
        '{}'.format(os.path.join(this_files_path, 'Williaikuma.py')),
    ]

    # subprocess doesn't work... (don't know why)
    os.system(' '.join(args))

    # Clean
    if os.path.exists(specs_path):
        shutil.rmtree(specs_path)

    if os.path.exists(build_path):
        shutil.rmtree(build_path)

    if os.path.exists(os.path.join(dist_path, 'Williaikuma.exe')):
        shutil.move(os.path.join(dist_path, 'Williaikuma.exe'),
                    os.path.join(this_files_path, 'other', 'win-exe', 'Williaikuma.exe'))
        shutil.rmtree(dist_path)


def main():
    make_win_exe()


if __name__ == '__main__':
    main()
