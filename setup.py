from distutils.core import setup

setup(
    name='HDR_CDAT',
    version='0.7dev',
    packages=['CDAT','CDAT.collision_diagrams','CDAT.collision_diagrams.modules',],
    package_data={
    'CDAT':['static/*.*','templates/*.*']},
    url='http://HDRCDAT.com',
    author='RoadSafetyEIT',
    author_email='samuel.klump@hdrinc.com',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    install_requires=['matplotlib'],
    long_description=open('README.txt').read(),
)