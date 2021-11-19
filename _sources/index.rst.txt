.. System Description Language documentation master file, created by
   sphinx-quickstart on Tue Mar  2 13:29:16 2021.


Welcome the func language doc!
################################################################################################

The specification language.
================================================================================================

The *func* is a description language that aims at producing rigorous, concise and human readable
functional specification for any project, concerning any domain of application.

* **Descriptive language** for multi-domain specification;
* **Generation of documentation** in various format;
* **Modeling and proofing** of functional behavior.

.. code-block:: func

   block Train_Odometer {
      define Tick {
         """
         Duration of the odometer tick in ms
         """
         Duration: real;
         """
         Count of increments during last odometer tick
         """
         Increments: natural [[ < 256 ]];
      }

      require Read_Kinematics_From_Odometer on Reading:
      ""
      {Reading.Distance} shall be equal to {Tick.Increments} ...
      {Reading.Speed} shall be equal to {Tick.Increments} ...
      "";

      define output Reading {
         Distance: real; # distance reading in meters
         Speed: real; # speed reading in meters/seconds
      }
   }


Table of Contents:
################################################################################################

.. toctree::
   :maxdepth: 2
   :caption: Language presentation

   presentation

.. toctree::
   :maxdepth: 2
   :caption: Language documentation

   documentation/home



Indices and tables:
################################################################################################

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
