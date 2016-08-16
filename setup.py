# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name='ADNerd',
    version='1.0',
    packages=['Dialog_Classes', 'Threads_Classes'],
    url='https://github.com/moyamartin/Digital_III',
    license='',
    author='Martin',
    author_email='moyamartin1@gmail.com',
    description='Software diseñado para comunicarse mediante el protocolo UART hacia un termociclador de ADN,'
                ' obteniendo los valores de temperaturas actuales dentro del sistema.'
)
