from distutils.core import setup
setup(
    name='Package_Statistics',
    packages=['Package_Statistics'],
    version='0.1',
    license='MIT',
    description=
    "Command line tool dor downloads the compressed Contents file, parse the file and output the statistics of the top 10 packages that have the most files associated with them",
    author='MaxMaxoff',
    author_email='maxim.vt@gmail.com',
    url='https://github.com/MaxMaxoff/Package-Statistics.git',
    download_url=
    'https://github.com/MaxMaxoff/Package-Statistics/archive/refs/tags/v0.1.tar.gz',
    keywords=['PackageStatistics', 'Debian', 'Debian Contents file'],
    install_requires=[],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    include_package_data=True,
    package_data={'': ['_conf/package_statistics.json']})
