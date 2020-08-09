from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='cira',
    version='0.0.1',    
    description='A simpler library for the alapaca trade api',
    url='https://github.com/AxelGard/cira',
    author='Axel Gard',
    author_email='axel.gard@tutanota.com',
    license='MIT',
    packages=['cira'],
    install_requires=['alpaca-trade-api'],
    long_description=long_description,
    long_description_content_type="text/markdown",

    classifiers=[
        'Development Status :: 1 - Plannig',
        'Intended Audience :: Finance/Quantitative',
        'License :: OSI Approved :: MIT',  
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',

    ],
)
