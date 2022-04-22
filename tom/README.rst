
SHAP — a tool that helps to explain what are the main features that affect the output of the regression model





Capstone
##########


|


:Splash Page: 
:Section Author: Tom Bresee
:Version: 2.0 
:Institution: University of Michigan
:Course: SIADS 697/698: Capstone
:Focus: Machine Learning Models / Tuning / Hyperparameters


|
|




Singapore Housing Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Examining Singapore HDB Flat Resale Pricing Values via machine learning methods

* Hyperparameter Tuning Optimization

  *  Adjusting parameters (results)



|
|



Jupyter Notebooks
~~~~~~~~~~~~~~~~~~~

* EDA pt I of II [`view <https://github.com/mcmanus-git/Singapore-HDB/blob/main/tom/nb_EDA_pt_I_of_II.ipynb>`_] [html]
* Kaggle XGBoost + Optuna Research [`view <https://www.kaggle.com/code/tombresee/xgboost-drivers-license/notebook>`_]


|
|



Image Results 
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


---------------
Correlations
---------------


* Although lease remaining time can be calculated from the current year and lease start year, its correlation to the lease year was not very high.  Using both these variables together though seemed to increase model accuracy.

* Although Linear Regression is interpretable, random forest regression appeared to perform relatively well. 

* Experiments we did were run on huge data, 80% of it in the training set, 20% of it being used for evaluation.


|


---------------
XGBoost
---------------

**General:**

* Although XGBoost training and prediction can be accelerated with CUDA-capable GPUs (allowing approximately 6X - 8X faster training vs conventional CPU), it should be noted that it gave *slightly* different results than the CPU-trained model. These differences were usually at the fourth or third decimal point level, but they did exist. XGBoost contains a parameter called the tree_method (tree construction algorithm), which is set to ``hist`` on CPU and set to hist or ``gpu_hist`` on GPU. 

* It turns out that the tree method ``hist`` and ``gpu_hist`` algorithms are actually different. This was manifested in different prediction results for a larger type dataset (which ours was). 

  * Why is this important ? Because hyperparameter tuning methods such as `GridSearch` are inherently brute force, **so any edge in training time is a massive advantage**, especially for tuning in our case as much as we needed. 


* **Note:** - GPU accelerated prediction is enabled by default when ``gpu_hist`` is set. The tree_method hist is not the CPU version of the tree_method gpu_hist. They are different algorithms.


* We enabled GPU training via the parameters: ``XGBRegressor(tree_method='gpu_hist', gpu_id=0)``

  * The tree_method hist is **not** the CPU version of the tree_method gpu_hist.  They are different algorithms.   

  * XGBoost also allows GPU support for SHAP acceleration


* We used the very latest version of XGBoost (version 1.6.0), which contains improvements and full coverage of experimental categorical data support. Metric calculation is now performed in double precision.  XGBoost now uses double for GPU Hist node sum, which improves the accuracy of our `gpu_hist`. 

* Regularization worked quite well. 

* General Parameters, Booster Parameters, and Learning Task Parameters:

* Configuration
  
  * Parameters:  Loss function to be minimized was set as ``reg:squarederror``.  


* `Reference <https://github.com/mcmanus-git/Singapore-HDB/raw/main/tom/final_images/default_xgboost_regressor_parameters.png>`_ default extracted XGBoost parameters (starting point)


**Modeling:**

* Due to our GPU usage, we were able to iterate over set parameters for speed...

* **max_depth** - as the depth increased, so the training time increased.  Large values of max_depth consumes memory when training. As expected, we observed that increasing this value would make the model more complex and more likely to overfit (thus the need for regularization). 






|


--------------------------
Random Forest Regression
--------------------------


* Random forest regression needed relatively high depth

* It was important to review the difference between the predicted and actual (gives us inight into how the model was performing)


* Some features were very very significant, while there were many where its importance value was quite low (exponential layout)

* Creating a mapping of town to region I believe helped with the analysis

* Singapore uses the metric system, thus sticking with meters (and not items like square feet)

* A common approach to eliminating features is to describe their relative importance to a model, then eliminate weak features or combinations of features and re-evalute to see if the model fairs better during cross-validation.



|
|




Appendix
~~~~~~~~~~~

https://www.tombresee.com/NFL/Milestone/

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


<hr>


The toctree directive initially is empty, and looks like this::

   .. tom
      tom









Running the build
-----------------

Now that you have added some files and content, let's make a first build of the
docs.  A build is started with the :program:`sphinx-build` program, called like
this::

   $ sphinx-build -b html sourcedir builddir


to run ::

   $ make html








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
