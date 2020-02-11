import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="week5test"
    version="0.0.1",
    author="Scott Johnson",
    author_email="ScottyJohnson002@gmail.com",
    url="https://github.com/ScottJohnson02/week-5-test",
    description="basic set-up for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
