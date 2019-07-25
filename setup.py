import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mcs_lib',
    version='1.0',
    scripts=['mcs_lib'],
    author="Niel Venter",
    author_email="support@minelert.com",
    description="Minelert utility package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dpventer/mcs_lib",
    packages=setuptools.find_packages(),
    install_requires=[
          'pySerial',
      ],
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)