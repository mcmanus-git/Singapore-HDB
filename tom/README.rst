
Capstone - University of Michigan
#####################################


|


:Section Author: Tom Bresee
:University: Michigan
:Course: SIADS 697: Capstone
:Version: 0.7


|
|


HDB Housing Analysis
~~~~~~~~~~~~~~~~~~~~~~~


**Background**

* bullet

* `Really good video of experiement in action <https://www.youtube.com/watch?v=XOEN9W05_4A>`_ 



|  
|




Jupyter Notebooks
~~~~~~~~~~~~~~~~~~~

* EDA pt I of II [`view <https://github.com/mcmanus-git/Singapore-HDB/blob/main/tom/nb_EDA_pt_I_of_II.ipynb>`_]



|
|



Images
~~~~~~~~~~~~~~~~~~~

* Correlation Plot of all base features [`full image <https://github.com/mcmanus-git/Singapore-HDB/raw/main/tom/images/correlation_matrix_baseline.png>`_] [`triangular image <https://github.com/mcmanus-git/Singapore-HDB/raw/main/tom/images/correlation_matrix_baseline_triangular.png>`_]

* Correlation normed price to all other features [`image <https://github.com/mcmanus-git/Singapore-HDB/raw/main/tom/images/correlation_with_price_per-sqm_normed.png>`_]




|
|




Observations
~~~~~~~~~~~~~~

* Although lease remaining time can be calculated from the current year and lease start year, its correlation to the lease year was not very high.  Using both these variables together though seemed to increase model accuracy.

* Although Linear Regression is interpretable, random forest regression appeared to perform relatively well. 

* Random forest regression needed relatively high depth

* It was important to review the difference between the predicted and actual (gives us inight into how the model was performing)

* Some features were very very significant, while there were many where its importance value was quite low (exponential layout)

* Creating a mapping of town to region I believe helped with the analysis

* Singapore uses the metric system, thus sticking with meters (and not items like square feet)



|
|



Master Reference Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `Dataset 1 <https://lbd.udc.es/research/real-life-HAR-dataset/>`_ - A Public Domain Dataset




|
|





Data Files:
::
    data.csv.gz	    # compressed file of all data values
    nodes.csv	       # list of nodes in the dataset and their metadata
    README.md	       # An explaination of the database fields 
    sensors.csv	    # A list of sensors and their metadata
    offsets.csv       # data.csv.gz file byte offsets


|



ToDo:
::
    do this
    do that




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
