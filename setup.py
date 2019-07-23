from distutils.core import setup

setup(
    name='HDR_CDAT',
    version='0.1dev',
    packages=['CDAT',],
    url='http://HDRCDAT.com',
    author='RoadSafetyEIT',
    author_email='samuel.klump@hdrinc.com',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    install_requires=['matplotlib'],
    long_description=open('README.txt').read(),
)