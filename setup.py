from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='foss-meetups',
  version='0.0.1',
  description='Foss Meetup by Mihir Panchal',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Mihir Panchal',
  author_email='mihirpanchal5400@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['meetup', 'foss', 'mihir']
  packages=find_packages(),
  install_requires=['requests','tk'] 
)