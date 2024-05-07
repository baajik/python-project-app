from setuptools import setup, find_packages
setup(
name='pratusha_flask_app',
version='1.0.0',
packages=find_packages(),
include_package_data=True,
py_modules=['main'],
install_requires=[
'Flask>=3.0.3',
],
)

