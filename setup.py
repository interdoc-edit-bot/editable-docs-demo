# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = {"": "src"}

packages = ["editable_docs_demo"]


install_requires = ["click==7.0"]

extras_require = {
    "docs": [
        "sphinx",
        "sphinx-rtd-theme",
        "sphinxcontrib-editable",
    ]
}

entry_points = {"console_scripts": ["editable_docs_demo = editable_docs_demo.cli:cli"]}


setup_kwargs = {
    "name": "editable-docs-demo",
    "version": "0.1.0",
    "description": "Editable docs demo",
    "long_description": open('README.rst').read(),
    "author": "Editable",
    "author_email": "email@example.com",
    "url": None,
    "package_dir": package_dir,
    "packages": packages,
    "install_requires": install_requires,
    "entry_points": entry_points,
    "python_requires": ">=3.7,<4.0",
    "extras_require": extras_require,
}


setup(**setup_kwargs)
