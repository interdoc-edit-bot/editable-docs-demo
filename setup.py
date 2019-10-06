# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = {"": "src"}

packages = ["editable_docs_demo"]


install_requires = ["click==7.0"]

extras_require = {
    "docs": [
        "sphinx",
        "sphinx-rtd-theme",
        "sphinx-autodoc-typehints",
        "sphinx-click",
        "marshmallow-jsonschema",
        "sphinx-jsonschema",
        "sphinxcontrib-editable",
    ]
}

entry_points = {"console_scripts": ["editable_docs_demo = editable_docs_demo.cli:cli"]}


setup_kwargs = {
    "name": "editable-docs-demo",
    "version": "0.1.0",
    "description": "",
    "long_description": "========\nOverview\n========\n\n.. start-badges\n\n.. list-table::\n    :stub-columns: 1\n\n    * - docs\n      - |docs|\n    * - tests\n      - | |travis|\n        |\n    * - package\n      - | |version| |wheel| |supported-versions| |supported-implementations|\n        | |commits-since|\n\n.. |docs| image:: https://readthedocs.org/projects/editable_docs_demo/badge/?style=flat\n    :target: https://readthedocs.org/projects/editable_docs_demo\n    :alt: Documentation Status\n\n\n.. |travis| image:: https://travis-ci.org/orange-aardvark/editable_docs_demo.svg?branch=master\n    :alt: Travis-CI Build Status\n    :target: https://travis-ci.org/orange-aardvark/editable_docs_demo\n\n.. |version| image:: https://img.shields.io/pypi/v/editable-docs-demo.svg\n    :alt: PyPI Package latest release\n    :target: https://pypi.org/pypi/editable-docs-demo\n\n.. |commits-since| image:: https://img.shields.io/github/commits-since/orange-aardvark/editable_docs_demo/v0.1.0.svg\n    :alt: Commits since latest release\n    :target: https://github.com/orange-aardvark/editable_docs_demo/compare/v0.1.0...master\n\n.. |wheel| image:: https://img.shields.io/pypi/wheel/editable-docs-demo.svg\n    :alt: PyPI Wheel\n    :target: https://pypi.org/pypi/editable-docs-demo\n\n.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/editable-docs-demo.svg\n    :alt: Supported versions\n    :target: https://pypi.org/pypi/editable-docs-demo\n\n.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/editable-docs-demo.svg\n    :alt: Supported implementations\n    :target: https://pypi.org/pypi/editable-docs-demo\n\n\n.. end-badges\n\nEditable docs demo\n\n* Free software: MIT License\n\nInstallation\n============\n\n::\n\n    pip install editable-docs-demo\n\nDocumentation\n=============\n\n\nhttps://editable_docs_demo.readthedocs.io/\n\n\nDevelopment\n===========\n\nTo run the all tests run::\n\n    tox\n\nNote, to combine the coverage data from all the tox environments run:\n\n.. list-table::\n    :widths: 10 90\n    :stub-columns: 1\n\n    - - Windows\n      - ::\n\n            set PYTEST_ADDOPTS=--cov-append\n            tox\n\n    - - Other\n      - ::\n\n            PYTEST_ADDOPTS=--cov-append tox\n",
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
