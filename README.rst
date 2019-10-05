========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/editable_docs_demo/badge/?style=flat
    :target: https://readthedocs.org/projects/editable_docs_demo
    :alt: Documentation Status


.. |travis| image:: https://travis-ci.org/orange-aardvark/editable_docs_demo.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/orange-aardvark/editable_docs_demo

.. |version| image:: https://img.shields.io/pypi/v/editable-docs-demo.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/pypi/editable-docs-demo

.. |commits-since| image:: https://img.shields.io/github/commits-since/orange-aardvark/editable_docs_demo/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/orange-aardvark/editable_docs_demo/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/editable-docs-demo.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/pypi/editable-docs-demo

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/editable-docs-demo.svg
    :alt: Supported versions
    :target: https://pypi.org/pypi/editable-docs-demo

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/editable-docs-demo.svg
    :alt: Supported implementations
    :target: https://pypi.org/pypi/editable-docs-demo


.. end-badges

Editable docs demo

* Free software: MIT License

Installation
============

::

    pip install editable-docs-demo

Documentation
=============


https://editable_docs_demo.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
