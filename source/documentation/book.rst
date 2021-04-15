.. sectnum::

Getting Started
################################################################################################

.. _book_materials:

Materials
################################################################################################

This section is intended for anyone who wants to understand the core language concepts.

It is a good starting point, especially if you are using the func language for the first time. 

The vocabulary and mechanisms are introduced progressively without code example.

.. _book_materials_system:

System terminology
================================================================================================

.. _book_materials_functional_specification:

Functional specification
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

A *system* is an abstract entity that has a *behavior* and a *state*.

* **state**: characteristics of the system;
* **behavior**: action of the system regarding the state.

In particular, the state can be declined in terms of *internals* and *externals* characteristics.
More precisely, the *scope* of the state can be one of the following:

* **internal**: private to the system;
* **input**: given from an interfaced system;
* **output**: given to an interfaced system;
* **buffer**: shared with an interfaced system.

For instance, the *input state* of a system consist on the input characteristics of the system externally specified
by an interfaced system.

The state can also be *constant*, meaning its value is given for once and *immutable*.
Thus constants will never change in the specification.

Using this terminology, we say that we *specified* the behavior of a system
when it is unambiguously established for each value of the state.

This is called the *functional specification* of the system.

The functional specification *sources* are the sources file written in func language.

.. note:: 
    
    By unambiguously, we mean that can be formally verified as explained in :ref:`book_materials_system_verification`



.. _book_materials_state_constraint:

State constraint
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

The state of a system is the aggregation of *quantities* belonging to *domains*, 
that can be *restricted* by *constraints*.

* **domain** is analogous to a `set in mathematics <https://en.wikipedia.org/wiki/Set_(mathematics)>`_;
* **quantity** is an element of a domain, it can also be a domain;
* **constraint** is an unambiguous relationship between quantities.

Using this terminology, we say that we *constrained* a quantity
when we restricted the domain of belonging of this latter via a constraint.

Therefore, we define the *admissible domain* of a quantity to be the restricted domain.
Doing so for each quantity of the state is called the *state constraint* of the system.

The functional specification consists on establishing a valid state constraint of the system.

.. note:: 

    Constraints can be expressed in natural language, pseudo-code or formal language.

.. _book_materials_system_verification:

System verification
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

The *formal proof* of a system is the process of verifying 
the `formal satisfiability <https://en.wikipedia.org/wiki/Satisfiability>`_ of the functional specification. 

The functional specification sources are verified by three ways:

1. **syntactically**, the sources syntax is valid;
2. **semantically**,  the sources references are valid;
3. **formally**, the state constraints are satisfiable.

Using this terminology, we say that we *verified* a functional specification
when we succeeded the tree proofs on this latter.

Doing so for each functional specification file that relates that system is called the
*system verification*. 

.. note:: 

    The functional specifications sources verification can be compared program compilation.

.. _book_materials_document_generation:

Document generation
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

The *document generation* of a system names the process of generating documentary output of the system.

The document generation produces a customizable output, in various format, given a functional specification.

.. note:: 

    Output is generated in latex using templates.

.. _book_materials_descriptive_language:


Configuration management
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

The *configuration management* refers to the process performing multiple document generation using the same sources.

This can be achieved by selecting thee specification items to be featured in a generation

This allows slight changes in the functional behavior that is documented according to the selection performed.

Terminology usage
================================================================================================

Engineering usages
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

This terminology is inspired from real world system examples 
where the need for a rigorous specification terminology is critical during solutions design:

* Microelectronics, in components design
* Embedded systems, device interface and behavior specification
* Software, object-oriented application design
* Database, relational database specification
* Web, especially in heterogenous service environment

However, nowadays other domains far from these can benefit from the usage 
of the vocabulary established in :ref:`book_materials_functional_specification`:

* Industry, in multi-domain technical specification
* Logistics systems, supply chain specification
* Research modeling, models specification in verification
* . . .

More generally, any domain that needs advanced technical design or scientific modeling
can use the func language to do it in a concise and human-readable format.

Descriptive Language
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

The func is a *descriptive language*, meaning it is not primarily intended to program but rather to describe systems.

The func language allows to describe systems using a syntax which is *formally progressive*.

This means that the state constraints can by expressed in various ways 
depending on the system verification desired to be performed:

* *semantic*, only natural language
* *algorithmic*, program correctness
* *logic*, propositional logic
* *mathematic*, `ZFC <https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory>`_ based logic

The language allows to specify systems using all these means in a unique functional specification, 
the verification will adapt to prove the system as most formally as possible.

Tutorials
################################################################################################
