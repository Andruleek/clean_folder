from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean_folder=clean_folder.setup:setup',
        ],
    },
    install_requires=[
        # Список залежностей, якщо потрібно
    ],
)
