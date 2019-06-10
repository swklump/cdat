from distutils.core import setup

setup(
    name='HDR_CAT',
    version='0.1dev',
    packages=['CAT',],
    url='http://HDRCAT.com',
    author='RoadSafetyEIT',
    author_email='samuel.klump@hdrinc.com',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    install_requires=['matplotlib'],
    long_description=open('README.txt').read(),
)