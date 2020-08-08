from setuptools import setup

setup(
    name='cira',
    version='0.0.1',    
    description='A simpler library for the alapaca trade api',
    url='https://github.com/AxelGard/cira',
    author='Axel Gar',
    author_email='axel.gard@tutanota.com',
    license='MIT',
    packages=['cira'],
    install_requires=['alpaca-trade-api'],

    classifiers=[
        'Development Status :: 1 - Plannig',
        'Intended Audience :: Finance/Quantitative',
        'License :: OSI Approved :: MIT',  
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
    ],
)
