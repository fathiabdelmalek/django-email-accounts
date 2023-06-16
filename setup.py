from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='django-email-accounts',
    version='0.1.0',
    author='Fathi Abdelmalek',
    author_email='abdelmalek.fathi.2001@gmail.com',
    description='A reusable Django accounts package override the default login system with email login',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fathiabdelmalek/django-email-accounts',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=[
        'Django>=3.2.0'
    ],
)
