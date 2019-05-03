from distutils.core import setup

from setuptools import find_packages

setup(
    name='affirm-pay',
    packages=find_packages(),
    version='0.4',
    license='MIT',
    description='Python Client for Affirm',
    author='Anshul Sharma',
    author_email='anshul.jmi@gmail.com',
    url='https://github.com/raun/affirm-python-sdk',
    download_url='https://github.com/raun/affirm-python-sdk/archive/v_03.tar.gz',
    keywords=['AFFIRM', 'SDK', 'CLIENT', 'INTEGRATION'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Operating System :: OS Independent',
        'Natural Language :: English',
    ],
)
