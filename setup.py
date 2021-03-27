from setuptools import find_packages, setup
setup(
    name='quantsim',
    packages=find_packages(include=['quantsim']),
    version='0.0.10',
    description='My first Python library',
    author='kpodsiad',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.2'],
    test_suite='tests',
)