
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


Singapore Housing Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The A


* AoT is **now** an anchor partner in a new NSF-funded project called SAGE.

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



The Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SubFiles:
::
    data.csv.gz	    # massive compressed file of all sensor data values and readings
    nodes.csv	    # list of nodes in the dataset and their individual metadata
    README.md	    # An explaination of the database fields 
    sensors.csv	    # A list of active sensors and their pertinent metadata
    offsets.csv     # data.csv.gz file byte offsets


|
|


* What Data is Collected ?  

  * The nodes will initially measure temperature, barometric pressure, light, vibration, carbon monoxide, nitrogen dioxide, sulfur dioxide, ozone, ambient sound pressure, and pedestrian and vehicle traffic. Continued research and development is using machine learning to create sensors to monitor other urban factors of interest such as solar light intensity (visible, UV, and IR) and cloud cover (important to building energy management), and flooding and standing water.


|

**More:**

|
|


What is the Chicago AoT Program ? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* The Array of Things (AoT) is an experimental urban measurement system comprising programmable, modular "nodes" with sensors and computing capability so that they can analyze data internally, for instance counting the number of vehicles at an intersection (and then deleting the image data rather than sending it to a data center). AoT nodes are installed in Chicago and a growing number of partner cities to collect real-time data on the city’s environment, infrastructure, and activity for research and public use. The concept of AoT is analogous to a “fitness tracker” for the city, measuring factors that impact livability in the urban environment, such as climate, air quality, and noise.  


* AoT is **now** an anchor partner in a new NSF-funded project called SAGE.

  *  In late 2018 the AoT team proposed a new effort to the National Science Foundation's Mid-Scale Research Infrastuructre program, with an expanded vision, building on all of the lessons learned from the AoT project and creating a new hardware and software infrastructure. Successfully funded with a start of October 2019, the new NSF-funded project, called SAGE: A Software-Defined Sensor Network, will result in a migration of AoT functions to new devices in 2021. SAGE is led by Northwestern University in partnership with the Discovery Partners Institute (University of Illinois), University of Chicago, Argonne National Laboratory, the University of Colorado, the University of California-San Diego, Northern Ill


|
|



General Observations
~~~~~~~~~~~~~~~~~~~~~~~

* Although lease remaining time can be calculated from the current year and lease start year, its correlation to the lease year was not very high.  Using both these variables together though seemed to increase model accuracy.

* Although Linear Regression is interpretable, random forest regression appeared to perform relatively well. 

* Random forest regression needed relatively high depth

* It was important to review the difference between the predicted and actual (gives us inight into how the model was performing)

* Some features were very very significant, while there were many where its importance value was quite low (exponential layout)

* Creating a mapping of town to region I believe helped with the analysis

* Singapore uses the metric system, thus sticking with meters (and not items like square feet)

* A common approach to eliminating features is to describe their relative importance to a model, then eliminate weak features or combinations of features and re-evalute to see if the model fairs better during cross-validation.



|
|



Reference Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* http://arrayofthings.github.io/

* **SAGE** - `Access Sage Sensors <https://sagecontinuum.github.io/sage-docs/docs/tutorials/access-sage-sensors>`_


|
|




------
Citations
------

`Journal of Open Source Software article <http://joss.theoj.org/papers/10.21105/joss.00205>`_.

    L. McInnes, J. Healy, S. Astels, *hdbscan: Hierarchical density based clustering*
    In: Journal of Open Source Software, The Open Journal, volume 2, number 11.
    2017
    

    McInnes L, Healy J. *Accelerated Hierarchical Density Based Clustering* 
    In: 2017 IEEE International Conference on Data Mining Workshops (ICDMW), IEEE, pp 33-42.
    2017


|
|


The Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SubFiles:
::
    data.csv.gz     # massive compressed file of all sensor data values and readings
    nodes.csv       # list of nodes in the dataset and their individual metadata
    README.md       # An explaination of the database fields 
    sensors.csv     # A list of active sensors and their pertinent metadata
    offsets.csv     # data.csv.gz file byte offsets


|
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
