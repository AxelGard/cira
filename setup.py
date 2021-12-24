from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='cira',
    version='2.3.0',
    description='A simpler library for the alapaca trade api',
    url='https://github.com/AxelGard/cira',
    author='Axel Gard',
    author_email='axel.gard@tutanota.com',
    license='MIT',
    packages=['cira'],
    long_description=long_description,
    long_description_content_type="text/markdown",

    install_requires=['alpaca-trade-api'],

    extras_requires = {
        "dev": [
            "pytest"
        ]
    },


    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Office/Business :: Financial",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
