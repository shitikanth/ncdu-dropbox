from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='ncdu-dropbox',
    version='0.1',
    description='Generates ncdu compatible json file for Dropbox',
    long_description=readme(),
    url='https://github.com/shitikanth/ncdu-dropbox',
    author='Shitikanth Kashyap',
    author_email='shitikanth1@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    install_requires=['dropbox'],
    entry_points={
        'console_scripts': [
            'ncdu-dropbox=ncdu_dropbox.main:main'
        ]
    }

)
