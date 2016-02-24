from distutils.core import setup
setup(
    name='hcat',
    version='1.0',
    author='Jeffrey Aven',
    author_email='info@bigdatasolutions.com',
    description='Python HCatalog client',
    url='https://github.com/avensolutions/hcat-py',
	packages=['hcat'],
    license='Apache License 2.0',
    keywords=['python', 'hcatalog', 'hcat', 'pyspark'],
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Operating System :: POSIX :: Linux',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Environment :: Other Environment'
    ]
)
