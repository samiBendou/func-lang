Context Overview
################################################################################################

*This parts gives an overview of the idea of a general purpose specification and where did it come from.*

Specification?
================================================================================================

*This parts intends to describe the currently available system description tools and how they relate to the func language.*

In the context of complexity growth of `multi-domain <https://en.wikipedia.org/wiki/Multiphysics>`_ industrial systems [#]_,
the need for more *traceability*, *flexibility* and *safety* of systems has increased.

Indeed, systems nowadays have different levels of precision in their functional specification.
This induces that it is critical to *trace* between items of different specification in order.
This guarantees that each level of precision in the functional specification behaves as expected by other level. 

Systems nowadays tends to be deployed in very heterogenous environment and this must be done in preserving system overall functional behavior.
Flexibility in specification is a productivity booster as it avoids functional specification duplicates and the additional design that comes with.

The consideration regarding safety of systems are increasing, the system must statistically ensure that it is safe regarding official criterion.
Safe specification allows reduce the time allocated to test phases, a specification that is proved to be safe will be tested less.

The needs describe above reveals the opportunity to provide better design *tools* for engineers, developers and
better *information systems* for everyone.

This project aims at providing a *system functional description language*, the **func**,
and associated *tools* going in that direction.


.. [#] Communication networks, supply chains, software applications, hardware devices, mutli-physics systems ...
.. [#] Multi-domain technical specification, including software specification.

What is available?
================================================================================================

Modeling Language based solutions
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Nowadays, system description frameworks such as respectively UML or SysML frameworks are commonly used to
describe respectively software systems or multi-physics systems.
However they seems to reach their limits as the complexity of the systems grows.

Indeed, system engineers seems to progressively abandon these solutions,
at the benefits of hand made specification frameworks that are mostly derived from the SysML with specific features.

These solutions, despite being the only ones working nowadays, are often based on XML files, a file format initially
destined to client-server heterogeneous communication.

The XML format is not adapted to the functional description of a system because this last requires only a simple set
of language elements that is homogeneous to describe a vast range of systems.

This causes the currently developed solutions to work poorly, implementing slower algorithms and
introducing a significant complexity increase in version control.

Furthermore, the modeling language based solutions have been initially though with a particular care for object oriented
application design which is not enough nowadays regarding the variety of system architecture developed.
This cause, among others, modeling language to be poorly featured when dealing with non object-oriented systems.

Lastly, these solution are based on input code that is poorly human readable making operations
such as diff reading between versions complicated.

The func language aims at replacing the system description frameworks such as UML or SysML
by providing a human readable code description of systems that can easily be visualized in any user interface.

High Level Synthesis based solutions
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

In microelectronics design, descriptions language such as VHDL or Verilog are used to describe
ASIC or FPGA components that are latter integrated into embedded electronics boards.

The description languages allows to perform a synthesis of the description provided by sources files
in order to give an abstract graph representation of the electronics circuit of the component called the netlist.
The construction of the netlist involves heuristics that builds a logic gate representation of the component.

The synthesis process can therefore be seen as a system validation mechanism in the sense that if the heuristic fails
for expected reasons, it means that the system is not valid, for instance that the component design cannot be synthetizable.

The func language intends to generalize netlist representation of multi-domain systems in order to give an analogous
validation that the one that is provided by electronics components synthesis.

The func language also intends to provide code generation tools that accelerates the specification to implementation
process using netlist representation.

Format proof based solutions
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Research in mathematics has proven a growing interest in developing formal proof automated method
to ensure consistency and correctness of their demonstrations, which is still an active topic.

Mathematics lead a more general initiative for formal proofing of both science publications.
Both by providing open-source code associated to the results of publications and by developing standard
evaluation methods for significance and consistence evaluation.

The func language intends to provide a compdefinee proofing framework based both on natural language analysis
and formal validation.

Block design based solutions
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Tools such as Simulink or Labview can be seen as a solution to the design behavior and testing issue.
However they are expensive and do not provide enough output for documentation.
That because these are only meant for design purpose.
They also suffer from the lack of production output generation contrary to HLS based solutions.

The func language is based on functional block representation allowing to generation it from source code and
therefore providing the same visualization tools of block design solutions without the heavy framework needed.

The func language also intends to provide a simulation framework allowing to visualize input dynamic behavior.

Programming code based solutions
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Nowadays, software developers tends to avoid duplicating specification outside of the code
because of evident versioning issues and the additional work that requires to maintain a separated documentation.

Solutions such as doxygen or autodoc allows to deal with this issue by generating documentation website
for software projects.

This allows to write a compdefinee software specification inside the code and generate a website from code
and documentation.

This solution is preferable for small software project, especially when they are mono-language or mono-target.
However, if these conditions are not verified, for example if the application is composed of multiple APIs
of various language, such as Restful APIs, it can be useful to express all the functional needs and
the functional encapsulation of the application in an homogeneous way among the project.

The func language intends to fulfill this need by providing a specification language that allows to write any API
specification in a functional form.

Conclusion
================================================================================================

The needs for a specification language are very heterogeneous and should be considered progressively,
regarding the best opportunities to improve the language.

Indeed, any stakeholder of an industrial, scientific or open project can be constrained to express its input or
output functional terms. For example, in the building of an Airbus airplane, many european countries are evolved,
causing an increasing in technical specification sharing in a standardized way.

Engineers, researcher, developers, managers are welcomed to contribute to the language specification,
in order the language to be the more compdefinee and therefore fulfill the maximum of needs.