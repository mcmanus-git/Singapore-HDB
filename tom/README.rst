
Capstone - University of Michigan
#####################################


|


:Section Author: Tom Bresee
:Version: 0.7
:University: Michigan
:Course: SIADS 697: Capstone



|
|
|


Information
~~~~~~~~~~~~~~~~~~~


* `Raw Dataset Description and Download <https://lbd.udc.es/research/real-life-HAR-dataset/>`_ - A Public Domain Dataset For Real-life Human Activity Recognition Using Smartphone Sensors

* This `location <https://data.mendeley.com/datasets/3xm88g6m6d/2>`_ also has those above raw files (as the authors prefer to store here). Moderate corrections were posted to the above `here <https://www.mdpi.com/1424-8220/20/16/4650/htm>`_.  Original paper in html form is `here <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7218897/>`_. 



* Note:  Related but not used original UCI-level dataset can be found `here <Smartphone-Based Recognition of Human Activities and Postural Transitions Data Set>`_ 

* `Really good video of experiement in action <https://www.youtube.com/watch?v=XOEN9W05_4A>`_ 



|




**Dataset II - Unsupervised Learning**

* **Plot**:  Take the list of sensor node GPS coordinates, and plot nicely into something like Leaflet or some visualization, this is an easy but nice to show visualization technique that will get us points.  Raw lat/long data files kept `here <https://github.com/tombresee/Michigan_Milestone_Initial_Work/blob/main/ENTER/RAW%20DATASET%20II/nodes.csv>`_.  The online arc gis like map from AoT is viewable `here <https://data.cityofchicago.org/Environment-Sustainable-Development/Array-of-Things-Locations-Map/2dng-xkng>`_, maybe we build our own version of this.  Should be easy to do, just taking lats/lons into some pretty picture.  


* **Great Lakes**:  Do some initial processing on the Michigan Great Lakes cluster, to build ability to later to ask for compute time for potential capstone extension analysis...



|
|



Master Reference Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `Dataset 1 <https://lbd.udc.es/research/real-life-HAR-dataset/>`_ - A Public Domain Dataset For Real-life Human Activity Recognition Using Smartphone Sensors

* `R based Analysis <http://rstudio-pubs-static.s3.amazonaws.com/100601_62cc5079d5514969a72c34d3c8228a84.html>`_

* `UCI Similar Dataset <https://archive.ics.uci.edu/ml/datasets/Smartphone-Based+Recognition+of+Human+Activities+and+Postural+Transitions>`_


|
|



* `Dataset 2 <https://www.mcs.anl.gov/research/projects/waggle/downloads/datasets/index.php>`_ - We will use huge file 'AoT_Chicago.complete.latest.tar', where `this <https://github.com/waggle-sensor/waggle/blob/master/data/README.md>`_ explains how to unzip it 

Files:
::
    data.csv.gz	    # compressed file of all data values
    nodes.csv	    # list of nodes in the dataset and their metadata
    README.md	    # An explaination of the database fields 
    sensors.csv	    # A list of sensors and their metadata
    offsets.csv     # data.csv.gz file byte offsets


* `Array of Things Overview <http://arrayofthings.github.io/>`_


* `Heroku Link <https://michigan-milestone.herokuapp.com/>`_


.. figure:: https://github.com/tombresee/Michigan_Milestone_Initial_Work/raw/main/ENTER/IMAGES/AoT-Diagram.jpg
   :scale: 50 %
   :alt: map to buried treasure

   Fig:  Current Architecture



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
