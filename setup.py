from setuptools import setup
from setuptools import find_packages


long_description = ""
with open("README.md", "r") as opn:
    long_description = opn.read()

setup(
    # Project
    name='sideralib',
    version='3.0.0',
    
    # Sources
    packages=find_packages(),
    package_data={},
    
    # Dependencies
    install_requires=['pyswisseph==2.10.3.2'],
    
    # Metadata
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='This Python package is for astrology and uses the sidereal system.',
    url='https://github.com/EH30/sideralib',
    keywords=[
        "Astrology", "Sidereal Astrology", "Kundli",  
        "Sidereal", "Tools", "Chart", "Sidereal Sign", "Astrology Chart", 
        "Astrology Kundli", "Sidereal Library", "Ayanamsa", "Sidereal Kundli",
        "Sidereal Chart", "Sidereal Calculations", "Sidereal Number", "Sidereal Package",
        "Astro", "Astro signs", "Astro Number", "Sidereal Ayanamsa"   
    ],
    license='Unlicense',
    
    # Authoring
    author='EH',
    author_email=None,
    
    # Classifiers
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: Freely Distributable',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ] 
)
