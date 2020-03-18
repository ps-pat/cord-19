from setuptools import find_packages, setup

setup(
    name = "cord19",
    version = "1.0",
    description = "Bunch of tools to mine the CORD-19 dataset",
    author = "Patrick Fournier",
    author_email = "p_fournier@hushmail.com",
    packages = find_packages(),
    ## install_requires = [],
    python_requires = ">=3"
)


## Local Variables:
## python-shell-interpreter: "ipython3"
## End:
