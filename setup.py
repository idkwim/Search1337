from setuptools import setup


setup(
    name = "cmdline-search1337",
    packages = ["1337"],
    entry_points={
        'console_scripts': [
            'search1337 = 1337.call:main',
        ]
    },
    version = "0.1",
    description = "Python 1337Day Exploit Scanner",
    author = "B3mB4m",
    author_email = "b3mb4m@gmail.com",
    )
