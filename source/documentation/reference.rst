.. sectnum::

Introduction
################################################################################################

The reference establishes the core grammar of the language and its semantic rules.
If you are not familiar with the language concepts, you may visit :ref:`book_materials` first 
to get introduced to the vocabulary.

Even thought this section is meant to be a rigorous language specification, 
it is progressive in order to easily explain each element of the grammar using what was already defined.

You can find it useful to have a precise information on the meaning of a particular syntax you encountered.
The examples given here are valid and illustrate the correct syntax.

For each language construct presented a syntax template is provided. 
The templates consist on the comprehensive specification of the language.

Each template figures elements such as ``<some_label>``, these must be replaced with the language
construct corresponding to the given label. 

.. _reference_links:

Links
################################################################################################

A *link* is a reference to a identifier already defined in the code.

Syntax::

    {<quantity>}

.. code-block:: func

    """refer to {my_target_quantity}"""

.. note::
    
    * Links are resolved during semantic verification.
    * Links can only be present in :ref:`reference_comment_block_comment` and :ref:`reference_quantity_constraint`


.. _reference_comment:

Comment
################################################################################################

A *comment* is a primitive composed of plain text.
The comments allows to provide additional information to be included during :ref:`book_materials_document_generation`.

.. _reference_comment_tags:

Tags
================================================================================================

A *tag* is a user-defined identifier suffixed with ``@`` which can be featured in a :ref:`reference_comment_block_comment`.

Syntax::

    @<identifier> <text>

.. code-block:: func

    """
    @rationale This quantity is meat to ...
    @remark Note that ...
    @desc Defines the quantity of ...
    """

.. _reference_comment_inline_comment:

Inline comment
================================================================================================

An *inline comment* is a comment line that can be inserted at **any place in the code**.

Syntax::

    # <text>

.. code-block:: func

    # This is an inline comment.

.. note:: 

    * Inline comments are ignored during document generation.

.. _reference_comment_block_comment:

Block comment
================================================================================================

A *block comment* is a multi-line comment that applies to the **first element below the comment**.

Syntax::

    """<text|link|tag>"""

.. code-block:: func

    """
    @useful something useful...

    represents the principal car of the {system.user}.
    """
    define car: Car;


.. _reference_literals:

Literals
################################################################################################

A *literals* is a built-in language element that allows to specify the most basic language expression, *the constants*.

Literals can be used to build :ref:`book_materials_state_constraint`.

.. note:: 

    * Literals can be compared to programming language literals;
    * Literals are of **arbitrary precision and size**;
    * Literals do not have a type but are constant :ref:`reference_quantity`.

.. _reference_literals_string:

Strings
================================================================================================

A *string* literal is an **immutable character string** provided with a given encoding format.

Character strings
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

A *character string* is a **plain text string** composed of printable and escape ASCII characters.

Syntax::

    <format>'<text>'

.. code-block:: func

    'This is a string literal'
    'This is a string\nliteral'
    utf8'This is a string literal'

.. note:: 
    
    * Only alphanumeric, blanks and escape characters are allowed.
    * Only single quoted string are admissible
    * Strings cannot contain links

Digit strings
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

A *digit string* is a string that encodes a **number in a given numerical basis**.

The list of characters corresponding to the domain are implicitly ordered in ASCII order, starting to 0.

Syntax::

    <basis>'<digits>'

.. code-block:: func

    h'ff0011'
    b'000100' 
    o'002727'

.. note:: 

    Only octal, binary and hexadecimal digit list are allowed

Numerics
================================================================================================

Boolean
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

A *boolean* literal is either **true or false**.

Syntax::

    true|false


.. code-block:: func

    false
    true

Integer
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

An *integer* literal is a **numerical token** expressing a signed integer number.

Syntax::

    [<sign>]<digits>

.. code-block:: func

    122331313
    -1333

Rational
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

A *rational* literal is a **numerical token** expressing a rational number.

Syntax::

    [<sign>]<digits>//<digits>

.. code-block:: func

    1223//4424
    -3//4

.. note:: 

    No spaces are allowed around the ``//`` symbol.

Decimal
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

A *decimal* literal is a **numerical token** expressing a decimal number.

Syntax::

    [<sign>]<digits>[.<digits>][e[<sign>]<digits>]

.. code-block:: func

    1500.75
    23e6
    1e-6
    -1.75
    -2.

.. note:: 
    
    * The count of significant digits must be correct.
    * No spaces are allowed around the ``e`` symbol.

Special
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

A *special* number literal is a **literal token** reserved for mathematical constants such as pi,
or Euler's number.


.. code-block:: func

    PI
    EULER
    IM

.. _reference_quantity:

Quantity
################################################################################################

A *quantity* is a component of the state defined in the :ref:`book_materials_functional_specification`.

A quantity is expected to belong to a certain domain via a :ref:`reference_quantity_constraint`.

The general syntax to define a quantity is the following:

Syntax::

    define <modifier> <identifier> [: <constraint> <constraint> ...]

.. code-block:: func

    define status: integer [[ = 0 ]];
    define input temperature: real;
    define output message; # belongs to any

.. note:: 
    
    * If no constraint is specified the quantity implicitly belongs to ``any``
    * Quantities can also be domains and there it is possible to write ``define q1: q2``

Explanations
================================================================================================

The most simple example for a state constraint is the equality between quantities:

.. code-block:: func

    define sensor_temperature: real;
    define cabin_temperature: [[ = sensor_temperature ]];

In the above example we can observe that:

* ``cabin_temperature`` is constrained to be equal to the ``sensor_temperature``;
* ``cabin_temperature`` implicitly belongs to the singdefineon set composed of ``sensor_temperature``.

.. note::

    * The above syntax is especially convenient for simple constraints
    * Complex constraints should be expressed using :ref:`reference_components_constraint`

Modifier
================================================================================================

The quantity *modifiers* are statements about the scope of a certain quantity,
they allow to differentiate between internals and external system state components.

Syntax::

    [constant] [input|output|buffer]

.. code-block:: func

    define input sensor_temperature: real;
    define output cabin_temperature: real;
   
.. _reference_quantity_constraint:

Constraint
================================================================================================

A *constraint* is an assertion about a certain quantity restricting its domain of belonging.
A constraint can itself be seen as a domain, which is the domain of validity of the constraint.

These can be listed by separating each constraint with a blank.
Doing so is equivalent to require that each constraint is met during verification.

.. code-block:: func

    define input sensor_temperature: real [[ > 10 ]];

.. _reference_quantity_constraint_domain:

Domain
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

The *domains* constraint are the most simple form of constraints.
These assert that a quantity belongs to a previously defined domain.

.. code-block:: func

    define issue_point: PointBlades

Builtin
------------------------------------------------------------------------------------------------

The language provide *builtin* domains such as ``real``, ``integer``, ...

Syntax::

    boolean|integer|rational|decimal|real|complex|empty|any


.. code-block:: func

    define friction_area: real;
    define current: complex;

Explicit
------------------------------------------------------------------------------------------------

An *explicit* domain is an explicit enumeration of primitives composing the domain.
These primitives must be heterogeneous.

Syntax::

    (( <literal>, <literal>, ... ))

.. code-block:: func

    define Spin: (( 'Up', 'Down', 'Strange' ));
    define Opcode: (( h'ff00', h'ff01', h'ff02' ));
    define Temperature: (( 90.0, 110, 200 ));

Intervals
------------------------------------------------------------------------------------------------

An *interval* is a continuous part of a straight.
It correspond to the notion of `mathematical intervals <https://en.wikipedia.org/wiki/Interval_(mathematics)>`_.

Syntax::

    <<|>> <real>:<real> <<|>>

.. code-block:: func

    define OneOne: <<-1:1>>;
    define ExclOneOne: >>-1.:1.>>;

Product
------------------------------------------------------------------------------------------------

The *product* matches the mathematical `cartesian product <https://en.wikipedia.org/wiki/Cartesian_product>`_.

Syntax::

    <domain> * <domain> * ...

.. code-block:: func

    define RealPair: real * real;
    define Rectangle: <<-1:1>> * <<0:2>>;


Union
------------------------------------------------------------------------------------------------

The *union* matches the mathematical `union binary operator <https://en.wikipedia.org/wiki/Union_(set_theory)>`_.

Syntax::

    <domain> || <domain> || ...

.. code-block:: func

    define NotZero: <<-1:0<< || >>0:1>>;
    define MinusOneTwo: <<-1:1>> || <<0:2>>;


Intersection
------------------------------------------------------------------------------------------------

The *intersection* matches the mathematical `intersection binary operator <https://en.wikipedia.org/wiki/Intersection_(set_theory)>`_.

Syntax::

    <domain> && <domain> && ...

.. code-block:: func

    define Empty: <<-1:0<< && >>0:1>>;
    define ZeroOne: <<-1:1>> && <<0:2>>;

Power set
------------------------------------------------------------------------------------------------
    
The *power set* of a domain matches the mathematical `power set <https://en.wikipedia.org/wiki/Power_set>`_.

Syntax::

    <domain>**
    
.. code-block:: func

    define SetsOfReal: real**;
    define SetsOfIssue: (( 'A', 'B', 'C' ))**;


Algebraical
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

An *algebraical* domain is a :ref:`reference_quantity_constraint_domain`  
that is provided with an additional algebraical structure.
It can be a vector or tensor space, or any user-defined algebraical construct.

Syntax::

    <identifier> <arguments> (<domain>)

.. code-block:: func

    define position: vector<2>(real);
    define multi_pole: matrix<12, 12>(complex);
    define metric_tensor: tensor<3, -3>(real);

.. note:: 
    
    * Elements of numeric domain can be featured in algebraical expressions; 
    * ``identifier`` must match a previously defined *structure constructor*.

Arguments
------------------------------------------------------------------------------------------------

The *arguments* of an algebraical are "template" parameters are passed to the structure to specify
numerical information on the algebraical structure:

* **dimension**, tuple representing the `mathematical dimension <https://en.wikipedia.org/wiki/Dimension>`_
* **variance**, dimension with signed indexes to specify the `tensor variance <https://en.wikipedia.org/wiki/Covariance_and_contravariance_of_vectors>`_
* **degrees**, such as polynomial or Galois fields degrees


Syntax::

    <integer, integer, ...>

.. _reference_quantity_numerics_dimension:

Scalar
------------------------------------------------------------------------------------------------

A *scalar* is a quantity constrained to be an algebraical of dimension 1.

.. code-block:: func

    define light_status: boolean;
    define score: integer;
    define pizza_slice: rational;
    define plane_distance: real;
    define electric_current: complex;

.. note::

    Scalar algebras are the canonical ones by default

Vector
------------------------------------------------------------------------------------------------

A *vector* is a quantity constrained to belong to a **finite dimension vector space**.

.. code-block:: func

    define buffer_state: vector<256>(boolean);
    define car_speed: vector<2>(real);
    define quad_speed: vector<4>(complex);


.. note::

    * components can be **indexed by only one natural number**.

Matrix
------------------------------------------------------------------------------------------------

A *matrix* is a quantity constrained to belong to a **finite dimension matrix space**.

.. code-block:: func

    define probability_matrix: matrix<40, 60>(real);
    define inertia_matrix: matrix<3>(real); # square matrix

Tensor
------------------------------------------------------------------------------------------------

A *tensor* is a quantity constrained to belong to a **finite dimension tensor space**.

.. code-block:: func

    define quad_speed: tensor<4>(complex);
    define metric_tensor: tensor<4, 4>(complex);
    define curvature_tensor: tensor<4, -4, -4, -4>(complex);

.. note::

    * Matrices and vectors are special kind of tensors providing more algebraical features.
    * Indices signs stands for the variance of the tensor.

.. _reference_quantity_blocks:

Blocks
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

A *block* constraint is an **expression block that produces a constraint**.

A constraint block can be expressed in a mathematical, algorithmic or semantic way.

Blocks are formally checked during :ref:`book_materials_system_verification`.

.. note::

    Constraint blocks can make usage of any previously defined quantity.

Semantic
------------------------------------------------------------------------------------------------

A *semantic block* is similar to a :ref:`reference_comment_block_comment`
but is used to textually specify a constraint.

Syntax::

    ""<text|link>""

.. code-block:: func

    define good_slices:
    ""
        equal to the {pizza_slices} such that ...
    "";

.. note:: 

    Semantic blocks are convenient for systems that do not require formal behavior validation.

Algorithmic
------------------------------------------------------------------------------------------------

An *algorithmic block* is an expression block that allows to define an algorithm and
therefore programmatically specify a constraint.

Syntax::

    {{
        <instruction>;
        <instruction>; 
        ... 
        <operator> <expression>
    }}

.. code-block:: func

    define good_slices:
    {{
        let a = pizza_slices;
        let b;

        b = 2 * a;
        a += b;
        = (b + a) * 5
    }};

.. note:: 

    Algorithmic blocks are convenient for systems that require a formal validation simpler than a formal proof.

Mathematic
------------------------------------------------------------------------------------------------

A *mathematic block* is an expression block that allows to define literal variables 
and use mathematical language to state properties about the variables.

A mathematical constraint allows to define

Syntax::

    [[
        <expression>;
        <expression>; 
        ... 
        <operator> <expression>
    ]]

.. code-block:: func

    define good_slices:
    [[
        let a = pizza_slices + b;
        let b = 2 * a;
        = (b + a) * 5
    ]];

In the above example, the existence of ``a`` and ``b`` is verified during system verification.

.. note:: 
    
    Mathematic blocks are convenient for systems that require a mathematical validation of behavior.

Function
================================================================================================

A *function* is analogous to a `mathematical function <https://en.wikipedia.org/wiki/Function_(mathematics)>`_.
It is a special quantity belonging to a functional domain.

Functions can be used to define **relationships between input and output quantities**.

A function can be defined using the keyword ``function``:

Syntax::

    function <identifier>(<parameter>, <parameter>, ...) 
        [: <constraint> <constraint> ... ;]

.. code-block:: func

    function euclidean_distance(
        x: vector<2>(real); 
        y: vector<2>(real);
        ): 
        real [[ = ((x - y) ^ 2) ^ (1//2) ]];

Functions can take *parameters* and specifies a template constraint.
The parameters can latter be specified to instantiate the constraint.

.. note:: 

    Constraint blocks of a function can make usage of the provided parameters.

.. _reference_components:

Components
################################################################################################

The *components* are the elementary building blocks of the func language.

Components are all gathered in a source file consists on a system as defined in :ref:`book_materials_functional_specification`.

Components can be provided with a block comment immediately above the component definition.

Syntax::

    <block|quantity|requirement>

.. note::

    A system can contain multiple sub-systems. Therefore:

    * Sources files can be included within each other
    * The language must be provided a component that can embed components

Block
================================================================================================

A *block* is the base container for other components of the language.
Blocks can be nested, a block can contain any component.

Syntax::

    block {
        <component>
        <component>
        ...
    }

.. code-block:: func

    block car_control {
        # ...
        block car_dynamics {
            # ...
        }
        # ...
    }

Scope
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

The components that are in *scope* of a block are:

* The components of the parent block
* The components explicitly imported

If a component is not in scope of a block, then it will not be possible reference inside the block.

In particular, if a quantity is not in scope, it will not be possible to import it in constraints.

A block can be brought in scope using the keyword ``import``.

Syntax::

    import <identifier> [as <alias>]

.. code-block:: func

    block mozzarella {
        # ...
    }

    block pizza {
        import mozzarella
        # ...
    }

.. note::

    If no root block is provided within a source file,
    then components are considered inside a default root block named after the file name of the source.

Quantity
================================================================================================

A *quantity* is defined as specified in :ref:`reference_quantity`.
All the quantities under a block form the *state of the block*.

Quantities can be gathered in more complex structures using the ``{}`` notation:

Syntax::

    define <identifier> { 
        [<identifier>[: <constraint> <constraint> ...];]
        [<identifier>[: <constraint> <constraint> ...];]
        ... 
    }

This notation provides syntactic sugar to build quantities with labeled field ``structure.element``.

.. code-block:: func

    define Car {
        position: vector<2>(real);
        speed: vector<2>(real);
        direction: Direction;
    }

.. _reference_components_constraint:

Requirement
================================================================================================

A *requirement* is a labeled constraint, it is syntactic sugar meant to postpone the constriction of
a quantity by labeling a list a constraints that applies to that quantity.

Syntax::

    require <identifier> on <quantity>: <constraint> [<constraint> ...];

.. code-block:: func

    require object_distance on distance_to_target:
    [[ 
        > minimal_distance_to_target 
    ]]
    [[
        = euclidean_distance(object.position, target.position)
    ]];

If a quantity is immediately constrained during its definition as saw in :ref:`reference_quantity`,
then way say the quantity is *anonymously constrained*.

Architecture
################################################################################################
