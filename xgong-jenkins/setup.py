from setuptools import setup, find_packages

version = '0.1'

setup(name='xgong_jenkins',
      version=version,
      description="Play a message when jenkins fails",
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Wazo Authors',
      author_email='dev.wazo@gmail.com',
      url='http://wazo.community',
      license='GPL3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'requests'
      ],
      entry_points={
          'console_scripts': [
              'xgong_jenkins = xgong_jenkins.main:main'
          ]
      }
      )
