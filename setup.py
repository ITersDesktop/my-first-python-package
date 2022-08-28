from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="myfirstpythonpackage", 
        version=VERSION,
        author="Tom Nguyen",
        author_email="nvntungl@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(include=["myfirstpythonpackage"]),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
	setup_requires=['pytest-runner'],
   	tests_require=['pytest==4.4.1'],
    	test_suite='tests',
        
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
