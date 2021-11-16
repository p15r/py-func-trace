from setuptools import setup

setup(
    install_requires=[
        'glom==20.11.0'
    ],

    test_suite='nose.collector',
    tests_require=['nose'],
)
