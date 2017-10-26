from setuptools import setup, find_packages

version = '0.1'

setup(
    name='ckanext-status',
    version=version,
    description='Status bar.',
    long_description='',
    classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author=['Alice Butcher', 'Ben Scott'],
    author_email='data@nhm.ac.uk',
    url='',
    license='',
    packages=find_packages(exclude=['ez_setup', 'list', 'tests']),
    namespace_packages=['ckanext', 'ckanext.status'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points= \
        """
            [ckan.plugins]
            status=ckanext.status.plugin:StatusPlugin
        """,
)
