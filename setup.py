#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test


class mytest(test):
    def run(self, *args, **kwargs):
        from runtests import runtests
        runtests()

setup(
    name='nexus-memcache',
    version='0.1.0',
    author='David Cramer',
    author_email='dcramer@gmail.com',
    url='http://github.com/dcramer/nexus-memcache',
    description = 'Memcache Plugin for Nexus',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'django-celery',
    ],
    test_suite = 'nexus_celery.tests',
    include_package_data=True,
    cmdclass={"test": mytest},
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)