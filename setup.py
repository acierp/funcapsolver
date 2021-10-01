import setuptools

with open("requirements.txt") as fp:
    requirements = fp.read().splitlines()

setuptools.setup(
    name="funcapsolver",
    author="AcierP",
    description="An audio-solving python funcaptcha solving module",
    url="https://github.com/AcierP/funcapsolver",
    packages=setuptools.find_packages(),
    classifiers=[],
    install_requires=requirements,
    include_package_data=True,
    version="1.0.2"
)
