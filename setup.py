from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

extras_require = {
    "rest_framework": ["djangorestframework>=3.12"],
    "filters": ["django-filter>=2.4"],
}

setup(
    name='django-email-accounts',
    version='0.3.0',
    author='Fathi Abdelmalek',
    author_email='abdelmalek.fathi.2001@gmail.com',
    description='A Django app for user management with email-based authentication.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fathiabdelmalek/django-email-accounts',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.7",
    install_requires=[
        'Django>=3.2.0',
    ],
    extras_require=extras_require,
)
