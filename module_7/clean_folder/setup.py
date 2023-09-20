from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.1',
    description='Module 7 Homework',
    url='https://github.com/d43v30n/goit-python/tree/main/module_7',
    author='Andrii',
    author_email='andrii@example.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'clean-folder = clean_folder.main:main_prog']}
)
