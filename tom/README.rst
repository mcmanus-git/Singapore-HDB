
Capstone
##########


|


:Splash Page: 
:Section Author: Tom Bresee
:Version: 2.0 
:Institution: University of Michigan
:Course: SIADS 697/698: Capstone
:Focus: Machine Learning Models / Tuning / Hyperparameters










Singapore Housing Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Examining of Singapore HDB Flat Resale Pricing Values

* More

  *  In late



|
|



Jupyter Notebooks
~~~~~~~~~~~~~~~~~~~

* EDA pt I of II [`view <https://github.com/mcmanus-git/Singapore-HDB/blob/main/tom/nb_EDA_pt_I_of_II.ipynb>`_] [html]
* Kaggle XGBoost + Optuna Research [`view <https://www.kaggle.com/code/tombresee/xgboost-drivers-license/notebook>`_]


|
|



Images
~~~~~~~~~~~~~~~~~~~

* Correlation Plot of all base features [`full image <https://github.com/mcmanus-git/Singapore-HDB/raw/main/tom/images/correlation_matrix_baseline.png>`_] [`triangular image <https://github.com/mcmanus-git/Singapore-HDB/raw/main/tom/images/correlation_matrix_baseline_triangular.png>`_]

* Correlation normed price to all other features [`image <https://github.com/mcmanus-git/Singapore-HDB/raw/main/tom/images/correlation_with_price_per-sqm_normed.png>`_]




|
|



Feature Importances 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* insert feature importances for model 1

* insert feature importances for model 2 


|
|



General Observations
~~~~~~~~~~~~~~~~~~~~~~~

**Machine Learning Models:**

* Although lease remaining time can be calculated from the current year and lease start year, its correlation to the lease year was not very high.  Using both these variables together though seemed to increase model accuracy.

* Although Linear Regression is interpretable, random forest regression appeared to perform relatively well. 

* Random forest regression needed relatively high depth

**Random Forest:**

* It was important to review the difference between the predicted and actual (gives us inight into how the model was performing)

* Some features were very very significant, while there were many where its importance value was quite low (exponential layout)

* Creating a mapping of town to region I believe helped with the analysis

* Singapore uses the metric system, thus sticking with meters (and not items like square feet)

* A common approach to eliminating features is to describe their relative importance to a model, then eliminate weak features or combinations of features and re-evalute to see if the model fairs better during cross-validation.




|
|




Appendix
~~~~~~~~~~~

* The Array of Things (AoT) is an experimental urban measurement system comprising programmable, modular "nodes" with sensors and computing capability so that they can analyze data internally, for instance counting the number of vehicles at an intersection (and then deleting the image data rather than sending it to a data center). AoT nodes are installed in Chicago and a growing number of partner cities to collect real-time data on the city’s environment, infrastructure, and activity for research and public use. The concept of AoT is analogous to a “fitness tracker” for the city, measuring factors that impact livability in the urban environment, such as climate, air quality, and noise.  


* AoT is **now** an anchor partner in a new NSF-funded project called SAGE.

  *  In late 2018 the AoT team proposed a new effort to the National Science Foundation's Mid-Scale Research Infrastuructre program, with an expanded vision, building on all of the lessons learned from the AoT project and creating a new hardware and software infrastructure. Successfully funded with a start of October 2019, the new NSF-funded project, called SAGE: A Software-Defined Sensor Network, will result in a migration of AoT functions to new devices in 2021. SAGE is led by Northwestern University in partnership with the Discovery Partners Institute (University of Illinois), University of Chicago, Argonne National Laboratory, the University of Colorado, the University of California-San Diego, Northern Ill


|


----------
Citations
----------

`Journal of Open Source Software article <http://joss.theoj.org/papers/10.21105/joss.00205>`_.

    L. McInnes, J. Healy, S. Astels, *hdbscan: Hierarchical density based clustering*
    In: Journal of Open Source Software, The Open Journal, volume 2, number 11.
    2017
    

    McInnes L, Healy J. *Accelerated Hierarchical Density Based Clustering* 
    In: 2017 IEEE International Conference on Data Mining Workshops (ICDMW), IEEE, pp 33-42.
    2017


|


----------------
Reference Links
----------------



* http://arrayofthings.github.io/

* **SAGE** - `Access Sage Sensors <https://sagecontinuum.github.io/sage-docs/docs/tutorials/access-sage-sensors>`_


|


----------------
The Data
----------------


SubFiles:
::
    data.csv.gz     # massive compressed file of all sensor data values and readings
    nodes.csv       # list of nodes in the dataset and their individual metadata
    README.md       # An explaination of the database fields 
    sensors.csv     # A list of active sensors and their pertinent metadata
    offsets.csv     # data.csv.gz file byte offsets


|


ToDo:
::
     plot feature importances (ranked) for baseline model
     summarize baseline model results / predictions
     improve plots from regression
     show the gridsearch 
     Optuna use
     use that nice output from milestone II (blocks)
     https://github.com/DistrictDataLabs/yellowbrick/blob/develop/yellowbrick/regressor/residuals.py
     




You can use ``backticks`` for showing ``highlighted`` code.


A cool bit of code::

   Some cool Code

.. code-block:: rst

   A bit of **rst** which should be *highlighted* properly.


---




The root directory of a Sphinx collection of reStructuredText document sources
is called the :term:`source directory`.  This directory also contains the Sphinx
configuration file :file:`conf.py`, where you can configure all aspects of how
Sphinx reads your sources and builds your documentation.  [#]_

Sphinx comes with a script called :program:`sphinx-quickstart` that sets up a
source directory and creates a default :file:`conf.py` with the most useful
configuration values from a few questions it asks you.  Just run ::

   $ sphinx-quickstart

and answer its questions.  (Be sure to say yes to the "autodoc" extension.)

There is also an automatic "API documentation" generator called
:program:`sphinx-apidoc`; see :ref:`invocation-apidoc` for details.


Defining document structure
---------------------------

Let's assume you've run :program:`sphinx-quickstart`.  It created a source
directory with :file:`conf.py` and a master document, :file:`index.rst` (if you
accepted the defaults).  The main function of the :term:`master document` is to
serve as a welcome page, and to contain the root of the "table of contents tree"
(or *toctree*).  This is one of the main things that Sphinx adds to
reStructuredText, a way to connect multiple files to a single hierarchy of
documents.

.. sidebar:: reStructuredText directives

   ``toctree`` is a reStructuredText :dfn:`directive`, a very versatile piece of
   markup.  Directives can have arguments, options and content.

   *Arguments* are given directly after the double colon following the
   directive's name.  Each directive decides whether it can have arguments, and
   how many.

   *Options* are given after the arguments, in form of a "field list".  The
   ``maxdepth`` is such an option for the ``toctree`` directive.

   *Content* follows the options or arguments after a blank line.  Each
   directive decides whether to allow content, and what to do with it.

   A common gotcha with directives is that **the first line of the content must
   be indented to the same level as the options are**.


The toctree directive initially is empty, and looks like this::

   .. toctree::
      :maxdepth: 2

You add documents listing them in the *content* of the directive::

   .. toctree::
      :maxdepth: 2

      intro
      tutorial
      ...

This is exactly how the toctree for this documentation looks.  The documents to
include are given as :term:`document name`\ s, which in short means that you
leave off the file name extension and use slashes as directory separators.

|more| Read more about :ref:`the toctree directive <toctree-directive>`.

You can now create the files you listed in the toctree and add content, and
their section titles will be inserted (up to the "maxdepth" level) at the place
where the toctree directive is placed.  Also, Sphinx now knows about the order
and hierarchy of your documents.  (They may contain ``toctree`` directives
themselves, which means you can create deeply nested hierarchies if necessary.)


Adding content
--------------

In Sphinx source files, you can use most features of standard reStructuredText.
There are also several features added by Sphinx.  For example, you can add
cross-file references in a portable way (which works for all output types) using
the :rst:role:`ref` role.

For an example, if you are viewing the HTML version you can look at the source
for this document -- use the "Show Source" link in the sidebar.

|more| See :ref:`rst-primer` for a more in-depth introduction to
reStructuredText and :ref:`sphinxmarkup` for a full list of markup added by
Sphinx.


Running the build
-----------------

Now that you have added some files and content, let's make a first build of the
docs.  A build is started with the :program:`sphinx-build` program, called like
this::

   $ sphinx-build -b html sourcedir builddir

where *sourcedir* is the :term:`source directory`, and *builddir* is the
directory in which you want to place the built documentation.  The :option:`-b`
option selects a builder; in this example Sphinx will build HTML files.

|more| See :ref:`invocation` for all options that :program:`sphinx-build`
supports.

However, :program:`sphinx-quickstart` script creates a :file:`Makefile` and a
:file:`make.bat` which make life even easier for you:  with them you only need
to run ::

   $ make html

to build HTML docs in the build directory you chose.  Execute ``make`` without
an argument to see which targets are available.

.. admonition:: How do I generate PDF documents?

   ``make latexpdf`` runs the :mod:`LaTeX builder
   <sphinx.builders.latex.LaTeXBuilder>` and readily invokes the pdfTeX
   toolchain for you.


Documenting objects
-------------------

One of Sphinx' main objectives is easy documentation of :dfn:`objects` (in a
very general sense) in any :dfn:`domain`.  A domain is a collection of object
types that belong together, complete with markup to create and reference
descriptions of these objects.

The most prominent domain is the Python domain.  To e.g. document the Python
built-in function ``enumerate()``, you would add this to one of your source
files::

   .. py:function:: enumerate(sequence[, start=0])

      Return an iterator that yields tuples of an index and an item of the
      *sequence*. (And so on.)

This is rendered like this:

.. py:function:: enumerate(sequence[, start=0])

   Return an iterator that yields tuples of an index and an item of the
   *sequence*. (And so on.)

The argument of the directive is the :dfn:`signature` of the object you
describe, the content is the documentation for it.  Multiple signatures can be
given, each in its own line.

The Python domain also happens to be the default domain, so you don't need to
prefix the markup with the domain name::

   .. function:: enumerate(sequence[, start=0])

      ...

does the same job if you keep the default setting for the default domain.

There are several more directives for documenting other types of Python objects,
for example :rst:dir:`py:class` or :rst:dir:`py:method`.  There is also a
cross-referencing :dfn:`role` for each of these object types.  This markup will
create a link to the documentation of ``enumerate()``::

   The :py:func:`enumerate` function can be used for ...

And here is the proof: A link to :func:`enumerate`.

Again, the ``py:`` can be left out if the Python domain is the default one.  It
doesn't matter which file contains the actual documentation for ``enumerate()``;
Sphinx will find it and create a link to it.

Each domain will have special rules for how the signatures can look like, and
make the formatted output look pretty, or add specific features like links to
parameter types, e.g. in the C/C++ domains.

|more| See :ref:`domains` for all the available domains and their
directives/roles.


Basic configuration
-------------------

Earlier we mentioned that the :file:`conf.py` file controls how Sphinx processes
your documents.  In that file, which is executed as a Python source file, you
assign configuration values.  For advanced users: since it is executed by
Sphinx, you can do non-trivial tasks in it, like extending :data:`sys.path` or
importing a module to find out the version your are documenting.

The config values that you probably want to change are already put into the
:file:`conf.py` by :program:`sphinx-quickstart` and initially commented out
(with standard Python syntax: a ``#`` comments the rest of the line).  To change
the default value, remove the hash sign and modify the value.  To customize a
config value that is not automatically added by :program:`sphinx-quickstart`,
just add an additional assignment.

Keep in mind that the file uses Python syntax for strings, numbers, lists and so
on.  The file is saved in UTF-8 by default, as indicated by the encoding
declaration in the first line.  If you use non-ASCII characters in any string
value, you need to use Python Unicode strings (like ``project = u'ExposÃ©'``).

|more| See :ref:`build-config` for documentation of all available config values.


Autodoc
-------

When documenting Python code, it is common to put a lot of documentation in the
source files, in documentation strings.  Sphinx supports the inclusion of
docstrings from your modules with an :dfn:`extension` (an extension is a Python
module that provides additional features for Sphinx projects) called "autodoc".

In order to use autodoc, you need to activate it in :file:`conf.py` by putting
the string ``'sphinx.ext.autodoc'`` into the list assigned to the
:confval:`extensions` config value.  Then, you have a few additional directives
at your disposal.

For example, to document the function ``io.open()``, reading its
signature and docstring from the source file, you'd write this::

   .. autofunction:: io.open

You can also document whole classes or even modules automatically, using member
options for the auto directives, like ::

   .. automodule:: io
      :members:

autodoc needs to import your modules in order to extract the docstrings.
Therefore, you must add the appropriate path to :py:data:`sys.path` in your
:file:`conf.py`.

|more| See :mod:`sphinx.ext.autodoc` for the complete description of the
features of autodoc.


More topics to be covered
-------------------------

- Other extensions (math, intersphinx, viewcode, doctest)
- Static files
- Selecting a theme
- Templating
- Using extensions
- Writing extensions


.. rubric:: Footnotes

.. [#] This is the usual lay-out.  However, :file:`conf.py` can also live in
       another directory, the :term:`configuration directory`.  See
       :ref:`invocation`.

.. |more| image:: more.png
          :align: middle
          :alt: more info




|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|






































































 
  





|
|
|
|
|
|
|
|
