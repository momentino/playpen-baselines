from setuptools import setup, find_packages

setup(
    name="playpen-baselines",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "playpen @ git+ssh://git@github.com/momentino/playpen.git",
        "torch",
        "transformers",
        "accelerate>=0.26.0"
    ],
)