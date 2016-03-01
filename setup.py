'''
    youzan
    -----------

    youzan provides the Youzan SDK for Python.

'''
from setuptools import setup

setup(
    name='youzan',
    version='0.1.2',
    url='https://github.com/fengluo/youzan',
    license='MIT',
    author='fengluo',
    author_email='fengluo17@gmail.com',
    description='Youzan SDK for Python',
    long_description=__doc__,
    py_modules=['youzan'],
    zip_safe=False,
    packages=['youzan'],
    install_requires=['requests', ''],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ])
