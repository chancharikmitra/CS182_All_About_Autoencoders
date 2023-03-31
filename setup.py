from setuptools import setup
from setuptools import find_packages

setup(
    name='CS182_All_About_Autoencoders',
    version='1.0',
    description='This is an educational walkthrough of autoencoder architectures, \
        describing their theoretical and practical underpinnings as well as architecture developments over time',
    author='Chancharik Mitra, Michael Huang, Joshua You, Jason Zhang',
    author_email='cmitra, michael_huang1291, jyou12, jason.z (all @berkeley.edu)',
    url='https://github.com/chancharikmitra/CS182_All_About_Autoencoders',
    packages=find_packages(),
    python_requires='>=3.9',
    install_requires=[
        'torch',
        'numpy',
        'pandas',
        'matplotlib',
        'jupyter'
    ],
    #entry_points= use if necessary,
    #license= We'll do this at the end


)