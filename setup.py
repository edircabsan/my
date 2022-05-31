import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='my',  
     version='0.2',
     author="Edircabsan",
     author_email="astner-br@gmail.com",
     description="A test package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/edircabsan/my",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )