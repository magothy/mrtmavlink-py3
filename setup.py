from setuptools import setup
import os.path


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name="mrtmavlink",
    version=get_version("mrtmavlink/version.py"),
    python_requires='>=3.6',
    packages=['mrtmavlink'],
    install_requires=['wheel']
)
