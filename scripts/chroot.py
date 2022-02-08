#!/usr/bin/env python3

import os
import sys
import uuid

if not os.path.exists(os.environ['BINPKGS_DIR']):
    os.mkdir(os.environ['BINPKGS_DIR'])

# Retain old behavior
if 'CHROOT_CMD' in os.environ:
    chroot_cmd = os.environ.get('CHROOT_CMD')
    if chroot_cmd == 'pychroot':
        os.execvpe('pychroot',
                   ['pychroot', '-B', f'{os.environ["BINPKGS_DIR"]}:/var/cache/binpkgs',
                    os.environ['CHROOT_DIR'], *sys.argv[1:]], os.environ)
    elif chroot_cmd == 'systemd-nspawn':
        os.execvpe('systemd-nspawn',
                   ['systemd-nspawn', f'--machine={uuid.uuid4()}', f'--directory={os.environ["CHROOT_DIR"]}',
                    f'--bind={os.environ["BINPKGS_DIR"]}:/var/cache/binpkgs', *sys.argv[1:]],
                   os.environ)

# Add new behavior
elif os.path.exists('/sbin/openrc-run'):
    os.execvpe('pychroot',
               ['pychroot', '-B',  f'{os.environ["BINPKGS_DIR"]}:/var/cache/binpkgs',
                os.environ['CHROOT_DIR'], *sys.argv[1:]], os.environ)
elif 'systemd' in os.readlink('/proc/1/exe'):
    os.execvpe('systemd-nspawn',
               ['systemd-nspawn', f'--machine={uuid.uuid4()}', f'--directory={os.environ["CHROOT_DIR"]}',
                f'--bind={os.environ["BINPKGS_DIR"]}:/var/cache/binpkgs', *sys.argv[1:]],
               os.environ)
else:
    raise RuntimeError("Unknown error occured, probably because I couldn't figure out the init system automatically"
                       " or CHROOT_CMD env variable was not manually set.")
