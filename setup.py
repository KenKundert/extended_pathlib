try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='extended_pathlib',
    version='0.3.0',
    description='shell library',
    long_description=readme,
    author="Ken Kundert",
    author_email='extended_pathlib@nurdletech.com',
    py_modules=['extended_pathlib'],
    url='http://nurdletech.com/linux-utilities/extended_pathlib',
    download_url='https://github.com/kenkundert/extended_pathlib/tarball/master',
    license='GPLv3+',
    zip_safe=True,
    install_requires=['pathlib', 'six'],
    keywords=[
        'extended',
        'pathlib',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ],
)
