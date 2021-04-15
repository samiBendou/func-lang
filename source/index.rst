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

Progress...
================================================================================================

* **Apr. 14, 2021** - First release of language specification
* **Mar. 28, 2021** - Prototyping first version of VSCode syntax extension
* **Mar. 02, 2021** - Prototyping first version of core language library
* **Feb. 18, 2021** - Expressing initial need and answer proposition

Contribute!
================================================================================================

This project has just started and *any initiative will be greatly welcome*, the more point of views we have,
the best improvements we can provide.

*Issues and improvements are welcomed!*

*Do not hesitate to ask for your own projects to appear here!*

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

Related projects:
################################################################################################

Maths and logic
================================================================================================

- `Low dimension maths toolbox <https://github.com/samiBendou/geomath>`_
- Multi dimension math toolbox
- Formal logic library
- Functional algebra library
- *Ask for yours !*

Physics and electronics
================================================================================================

- `Physics units and dimension <https://github.com/samiBendou/unitflow>`_
- `Dynamics numerical simulation <https://github.com/samiBendou/dynamics>`_
- *Ask for yours !*

Natural Language Processing
================================================================================================

- *Ask for yours !*

Misc
================================================================================================

- *Ask for yours !*

Indices and tables:
################################################################################################

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
