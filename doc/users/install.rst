.. _install:

======================
 Download and install
======================

This page covers the necessary steps to install Nipype.
There are two options: install the latest stable release, or install from source.

Option 1: Install The Current Release
-------------------------------------

Download the current release: `<https://github.com/nipy/nipype/releases/latest>`_.

Mac OSX
~~~~~~~

The installation process is similar to other Python packages.

If you already have a Python environment set up (for example, with Anaconda_ or
Canopy_), you can do::

	easy_install nipype

or::

	pip install nipype

Debian and Ubuntu
~~~~~~~~~~~~~~~~~

Add the `NeuroDebian <http://neuro.debian.org>`_ repository and install
the ``python-nipype`` package using ``apt-get`` or your favorite package
manager.


Option 2: Install From Latest Source
------------------------------------

1. Download the source. Do one of the following:

   * Download the latest source
     (`zip <http://github.com/nipy/nipype/zipball/master>`__ `tar.gz
     <http://github.com/nipy/nipype/tarball/master>`__) or a `previous version
     <http://github.com/nipy/nipype/tags>`_ and unpack/unzip the download. Move
     into the ``niype-x.y`` directory.
   * Use git to check out the latest development version::

        git clone git://github.com/nipy/nipype.git
        cd nipype

     or::

        git clone https://github.com/nipy/nipype.git
        cd nipype

2. Install::

        pip install -e .

   or::

        python setup.py install

**Note:** Depending on permissions you may need to use ``sudo``.

Nipype's `current dependencies <https://github.com/nipy/nipype/blob/master/nipype/info.py>`_.

Testing the install
-------------------

The best way to test the install is to run the test suite.  If you have
nose_ installed, then do the following::

    python -c "import nipype; nipype.test()"

you can also test with nosetests::

    nosetests --with-doctest <installation filepath>/nipype  --exclude=external --exclude=testing

or::

    nosetests --with-doctest nipype

A successful test run should complete in a few minutes and end with
something like::

    Ran 13053 tests in 126.618s

    OK (SKIP=66)

All tests should pass (unless you're missing a dependency). If SUBJECTS_DIR
variable is not set some FreeSurfer related tests will fail. If any tests
fail, please report them on our `bug tracker
<http://github.com/nipy/nipype/issues>`_.

On Debian systems, set the following environment variable before running
tests::

       export MATLABCMD=$pathtomatlabdir/bin/$platform/MATLAB

where ``$pathtomatlabdir`` is the path to your matlab installation and
``$platform`` is the directory referring to x86 or x64 installations
(typically ``glnxa64`` on 64-bit installations).

Avoiding any MATLAB calls from testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On unix systems, set an empty environment variable::

    export NIPYPE_NO_MATLAB=

This will skip any tests that require matlab.

Recommended Software
------------

Strong Recommendations
~~~~~~~~~~~~~~~~~~~~~~

IPython_ 0.10.2 - 1.0.0
  Interactive python environment. This is necessary for some parallel
  components of the pipeline engine.

Matplotlib_ 1.0 - 1.2
  Plotting library

`RDFLib <http://rdflib.readthedocs.org/en/latest/>`_ 4.1
  RDFLibrary required for provenance export as RDF

Sphinx_ 1.1
  Required for building the documentation

`Graphviz <http://www.graphviz.org/>`_
  Required for building the documentation. The python wrapper package (``graphviz``)
  and the program itself both need to be installed.

Interface Dependencies
~~~~~~~~~~~~~~~~~~~~~~

You might not need some of the following packages, depending on what exactly you
want to use nipype for. If you do need any of them, install nipype's wrapper package
(``nipype.interfaces``), then install the programs separately onto your computer, just
like you would install any other app.

FSL_
  4.1.0 or later

matlab_
  2008a or later

SPM_
  SPM5 or later

FreeSurfer_
  FreeSurfer v4.0.0 or later

AFNI_
  2009_12_31_1431 or later

Slicer_
  3.6 or later

Nipy_
  0.1.2+20110404 or later

Nitime_
  (optional)

Camino_

Camino2Trackvis_

ConnectomeViewer_

.. include:: ../links_names.txt
