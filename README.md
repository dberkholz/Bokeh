Bokeh 
=====

Bokeh is an implementation of [Grammar of
Graphics](http://www.cs.uic.edu/~wilkinson/TheGrammarOfGraphics/GOG.html) for
Python, that also supports the customized rendering flexibility of Protovis and
d3.  Although it is a Python library, its primary output backend is HTML5
Canvas.

There are many excellent plotting packages for Python, but they generally 
do not optimize for the particular needs of statistical plotting (easy faceting,
bulk application of aesthetic and visual parameters across categorical variables,
pleasing default color palettes for categorical data, etc.).  The goal of Bokeh
is to provide a compelling Python equivalent of [ggplot](http://ggplot.had.co.nz) in R.

A related project is [Pandas](http://pandas.pydata.org), whose [DataFrame](http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe) objects are directly
used by Bokeh.  Bokeh will also interface with the NDTable objects in [Blaze](https://github.com/ContinuumIO/blaze).


Technology
==========

Bokeh has a function-oriented interface that closely resembles ggplot.  These
functions can be used interactively from the Python prompt, or from within a
script (a la [Matplotlib](http://matplotlib.sourceforge.net/)).  Behind the
scenes, these functions construct a scenegraph and data transformation pipeline
that consists of nodes which can export their state into JSON.

The JSON representation of the graphic is then embedded in an HTML document
which also contains the Bokeh JS runtime.  This runtime is built on a port of
[Protovis](http://mbostock.github.com/protovis/) to HTML5 Canvas, and consists
of some higher-level canned plot layouts built on top of the Protovis
framework.

Dependencies
============

For the initial prototype, Bokeh is implemented as a wrapper on top of the
[Chaco](http://code.enthought.com/projects/chaco) plotting system, and displays
its output using Chaco.  This will change as we implement the Javascript/HTML
backend.

You can install the following with easy_install, "pip install", or they may
be available for your Linux system via the system package management.  If you
are using a distribution like the [Enthought Python Distribution](http://enthought.com/epd) or [Python(X,Y)](http://code.google.com/p/pythonxy),
then you already have them installed.

 * [Chaco](https://github.com/enthought/chaco)
 * [Traits](https://github.com/enthought/traits)
 * [Pandas](https://github.com/pydata/pandas)


Status
======

Bokeh was started in March 2012, and still remains in the
experimental/prototype stage.  It is under active development by contributors
at [Continuum Analytics](http://continuum.io), and with the recent award of a
grant from DARPA, we are able to devote more resources into it, along with
collaborators from Indiana University.  




