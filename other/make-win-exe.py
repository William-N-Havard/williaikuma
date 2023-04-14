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
    args = [
        'pyinstaller',
        '--noconfirm',
        '--clean',
        '--onefile',
        '--windowed',
        '--add-data', '"{};{}"'.format(os.path.join(this_files_path, 'williaikuma', 'assets'),
                                       os.path.join('.','williaikuma','assets')),
        '--specpath', '{}'.format(os.path.join(this_files_path, 'other', 'win-exe', 'spec')),
        '--distpath', '{}'.format(os.path.join(this_files_path, 'other', 'win-exe', 'dist')),
        '--workpath', '{}'.format(os.path.join(this_files_path, 'other', 'win-exe', 'build')),
        '--collect-submodules', '"williaikuma"',
        '{}'.format(os.path.join(this_files_path, 'Williaikuma.py')),
    ]

    # subprocess doesn't work... (don't know why)
    os.system(' '.join(args))

    # Clean
    if os.path.exists(os.path.join(this_files_path, 'other', 'win-exe', 'spec')):
        shutil.rmtree(os.path.join(this_files_path, 'other', 'win-exe', 'spec'))

    if os.path.exists(os.path.join(this_files_path, 'other', 'win-exe', 'build')):
        shutil.rmtree(os.path.join(this_files_path, 'other', 'win-exe', 'build'))

    if os.path.exists(os.path.join(this_files_path, 'other', 'win-exe', 'dist', 'Williaikuma.exe')):
        shutil.move(os.path.join(this_files_path, 'other', 'win-exe', 'dist', 'Williaikuma.exe'),
                    os.path.join(this_files_path, 'other', 'win-exe', 'Williaikuma.exe'))
        shutil.rmtree(os.path.join(this_files_path, 'other', 'win-exe', 'dist'))


def main():
    make_win_exe()


if __name__ == '__main__':
    main()
