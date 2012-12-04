from setuptools import setup, find_packages


install_requires = ['requests']

try:
    import argparse     # NOQA
except ImportError:
    install_requires.append('argparse')


with open('README.rst') as f:
    README = f.read()


classifiers = ["Programming Language :: Python",
               "License :: OSI Approved :: Apache Software License",
               "Development Status :: 1 - Planning"]


setup(name='vaurienclient',
      version='0.8',
      packages=find_packages(),
      description=("Client for the TCP Chaos Proxy"),
      long_description=README,
      author="Mozilla Foundation & contributors",
      author_email="services-dev@lists.mozila.org",
      include_package_data=True,
      zip_safe=False,
      classifiers=classifiers,
      install_requires=install_requires,
      test_requires=install_requires + ['nose'],
      test_suite='nose.collector',
      entry_points="""
      [console_scripts]
      vaurienctl = vaurienclient:main
      """)
