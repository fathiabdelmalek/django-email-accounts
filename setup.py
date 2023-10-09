from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

extras_require = {
    "rest_framework": ["djangorestframework"],
    "filters": ["django-filter"],
}

setup(
    name="django-email-accounts",
    version="0.4.3",
    author="Fathi Abdelmalek",
    author_email="abdelmalek.fathi.2001@gmail.com",
    description="A Django app for user management with email-based authentication.",
    license = "OSI Approved :: GNU General Public License v3 (GPLv3)",
long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fathiabdelmalek/django-email-accounts",
    packages=['email_accounts'],
    package_data={
        "email_accounts": ["templates/**/*", "static/**/*"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet",
        "Topic :: Software Development",
    ],
    python_requires=">=3.6",
    install_requires=[
        "Django",
    ],
    extras_require=extras_require,
)
