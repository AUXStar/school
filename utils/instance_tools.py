import os
import sys
import shutil
import importlib
import typing

running_dir = os.path.abspath(os.path.curdir)

CURRENT_INSTANCE = None

def file_dir(file, *dirs, abspath=True):
    base = os.path.split(os.path.abspath(file))[0]
    path = os.path.join(base, *dirs)
    if abspath:
        return os.path.abspath(path)
    return path

def init_instance(instance_dir=None, base_dir=None):
    return Instance(instance_dir,base_dir)


class Instance:
    instance_dir: str
    config: typing.Any

    def __init__(self, instance_dir=None, base_dir=None) -> None:
        if base_dir is None:
            base_dir = os.path.curdir
        else:
            if not os.path.exists(base_dir):
                os.makedirs(base_dir)
        os.chdir(base_dir)
        if instance_dir is None:
            instance_dir = "instance"
        if not os.path.exists(instance_dir):
            shutil.copytree(file_dir(__file__, "instance_base"), instance_dir)
        self.instance_dir = os.path.abspath(instance_dir)
        os.chdir(self.instance_dir)
        globals()['CURRENT_INSTANCE'] = self
        try:
            self.config = self.instance_import('config')
        except:
            self.config = None
            # raise config not found

    def instance_import(self, module_str: str):
        sys.path.append(self.instance_dir)
        module = importlib.import_module(module_str)
        sys.path.remove(self.instance_dir)
        return module

    def join(self, *dirs):
        return os.path.join(self.instance_dir, *dirs)

    def open(
        self,
        file: str | list[str],
        mode="r",
        buffering: int = -1,
        encoding: str | None = None,
        errors: str | None = None,
        newline: str | None = None,
        closefd: bool = True,
        opener: None = None,
    ):
        path = self.join(file)
        return open(path, mode, buffering, encoding, errors, newline, closefd, opener)

# typing
CURRENT_INSTANCE:Instance