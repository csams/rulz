from setuptools import setup, find_packages

runtime = set([
])

develop = set([
    "flake8",
    "ipython",
    "pytest",
    "setuptools",
    "twine",
    "wheel",
])

if __name__ == "__main__":
    setup(
        name="rulz",
        version="0.0.5",
        description="rulz is a decorator based IoC framework.",
        long_description=open("README.md").read(),
        long_description_content_type="text/markdown",
        url="https://github.com/csams/rulz",
        author="Christopher W. Sams",
        packages=find_packages(),
        install_requires=list(runtime),
        package_data={"": ["LICENSE"]},
        license="Apache 2.0",
        extras_require={
            "develop": list(runtime | develop),
        },
        classifiers=[
            "Intended Audience :: Developers",
            "Natural Language :: English",
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7"
        ],
        include_package_data=True
    )
