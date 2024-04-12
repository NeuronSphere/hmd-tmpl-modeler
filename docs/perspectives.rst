.. perspectives and extensions

Perspectives and Extensions - Infinite Modeling
===================================================
One way to discect software is into 2 primary parts:

#.  Defining data models and structures 
#.  Defining actions, behaviors, and logic that interacts with the defined models

This useful lens can be applied across a vast number of technologies - examples include:

*.  Object Oriented Programming specifically grounds itself in modeling *state* and *behavior*
*.  SQL subdivides into Data *Definition* Language (DDL) and Data *Manipulation* Language (DML)
*.  Libraries such as python's Pydantic, or the Lombok library in java serve as advanced ways to 
    represent object models with validation and standardized behaviors 
*.  RCP definition specs such as OpenAPI or Protobuf allow definitions of rich object models 
    and language agnostic function definitions that use these models 


Model Impedence Mismatches
-----------------------------------------------------------
The base modeling construct in NeuronSphere Modeler is 
a labeled property graph with an intentionally simplified type & relationship system.

*Entities*, specifically *Nouns* and *Relationships* form a basic underlying
structure that can be used to implement a vast number of more specific data modeling 
and governance capabilities.

Across technologies, there is over and over a repeated demand to use metadata
to generate data representations, but there are 2 primary challenges.

#.  Type system mismatches happen between any 2 tech stacks or systems
#.  Relationship representations vary broadly, but an attribute-carrying 
    relationship in a property graph allows maximum flexibility across 
    manifestations

.. note:: Why not an existing schema such as json?  Ironically, schema is too powerful, 
   too expressive.  Use of a schema 'anchors' so strongly that entire ecosystems will 
   be *off-limits* due to complexity/mismatch.

   Put another way, detailed object schema systems are challenged as a lowest-common-denominator 
   as input to an *easily* extensible data modeling & Model Driven Engineering framework.



Perspectives 
--------------
Perspectives are the named visual display variations used in Modeler 
to adapt the user experience to a more specific data modeling paradigm.

Different roles in an organization will use different perspectives to update the 
relevant parts of a model based on the project and technology chosen.  

Examples include:

*  There is a "Base SQL" perspective that allows adding 
   metadata about tables and SQL datatypes to entities and their attributes.
*  A programmer might want to generate python dataclasses or pydantic models using the 
   python-dataclass and python-pydandic perspectives respectively.
*  A data quality perspective allows logical constraint capture, while perspectives 
   allow seeing the implementation in multiple manifestations.  We'd like to see that 
   an attribute will materialize as "Not Null" in a database, but will have a similar constraint 
   declaration in programatic data models and APIs based on the same conceptual model.
*  We might add a perspective for a particular company or project to allow collaboration on additional 
   data governance metadata that can be output into custom documentation or downstream systems.

In a *SQL Centric* modeling paradigm, we pass from *Conceptual Modeling* into *Logical Modeling* and then 
*Physical Modeling*.  Perspectives on a base conceptual model allows this progression, but also allows 
similar progressions into other modeling paradigms.

What does this look like?  We can have a discussion about a few new entities and attribute changes in a data 
model, and then percolate those changes through multiple technology stakeholders for 
feedback, and instantiate any collection of custom data models into git for further 
analysis.

Entity Graph Overall Display
++++++++++++++++++++++++++++++
We *switch to a perspective* in the main graph UI, and it impacts the display 
of all Nouns and Relationships.

Noun Display 
++++++++++++++++
Currently, the behavior of the UI is such that switching perspectives updates the displayed 
information in the headers, and styles, of all *Nouns* in the display.

The visual format of the attribute list is also dependent on the perspective in effect.

Relationship Display 
++++++++++++++++++++++
The visual representation of relationships is a key differentiator between perspectives.  

Showing a relationship as a visual rectangle between the Nouns it joins versus visualizing
the relationship as a line and using hover/click interactions to access the relationship editor.

.. warning:: In the core entity model, we are allowed to model attributes on relationships and create
   a proper logical model.  When visualizing this model directly in the tabular perspective, 
   there may be "mismatches" in the cardinalities vs properties vs mapping to physical table that 
   may not be visually obvious at this time.

   The simple example is mapping a relationship with several attributes onto a 1-n physical relationship.
   Placement of the relationship attributes is more naturally in a 1-n/m-1 bridging table.


Attribute Editor 
+++++++++++++++++
When editing an entity, (noun or relationship), there are several places where the applicaiton 
of a perspective changes the UI.  

A perspective might add *extension* data for all entities, but more often will be applied to 
nouns or all relationships in a perspective.  Examples include:

#.  The "table_name" extension available as a property to all entities 
    when using any of the SQL-based perspectives.  This is an entity-level extension.
#.  A "rel_type" extension available as a property to relationships in a SQL-based perspective.

More common and powerful are *attribute extensions* that are available when a perspective is active in the 
attribute editor.  This presents as new columns to the right of the existing columns in the attribute editor.

Consider the basic attributes:

========  ========  ==========
Name      Desc      Type
========  ========  ==========
fname     False     String
salary    False     Float
height    True      Int
faves     True      Collection
========  ========  ==========

If we activate the python-dataclass perspective when editing the attribute list, we get the option to edit the 
metadata for each attribute that is specific to the perspective.

========  ========  ==========  ==============
Name      Desc      Type        DataclassType
========  ========  ==========  ==============
fname     False     String      string 
salary    False     Float       float
height    True      Int         integer
faves     True      Collection  list 
========  ========  ==========  ==============

If we activate the SQL2023 perspective when editing the attribute list, we see several other more advanced options:

========  ========  ==========  ================  =============
Name      Desc      Type        Sql2023.Type      Sql.Nullable
========  ========  ==========  ================  =============
fname     False     String      varchar({p0})     false 
salary    False     Float       float({p0},{p1})  true
height    True      Int         int               false
faves     True      Collection  array             true
========  ========  ==========  ================  =============


.. note:: Much of the purpose of this ability is to allow collecting the broadly polyglot metadata 
   and making it available in the templates associated with the perspective.

.. TODO: "Allow model ref for attribute type"

Extensions (Perspective Data Storage)
----------------------------------------
Perspectives define how a specific modeling construct visually appear, and control 
what additional metadata may be stored at various levels of the model.

*Extensions* describe where additional metadata will be stored in the json 
representation of an object model.


Import vs Inheritance
-------------------------------------
We hate to repeat ourselves, and programmers even have a nifty little acronym - 
:abbr:`DRY (Don't Repeat Yourself)`.  In data modeling, it is the repeating ourselves 
in impossible-to-track ways that are the roots of many problems.

*  **Import** is to copy an existing Noun, Relationship, or colleciton thereof into another model.
   This is a *copy* operation, and the new Entities can be freely edited, snapshotted, and modified.
   A reference to the original entity is tracked, and a *reconcile with ancestor* function allows 
   tracking the delta between versions of entities across models, assuming access.
   This is repeating yourself, but is often a reasonable approach for rapid development or high domain-cardinality 
   data models.  Changes to original models are not propagated/notified.
*  **Inherit** is to create an Entity based on an existing Entity, with the ability to add new 
   attributes and perspectives, but not change existing attributes or extensions.  Changes to 
   source models can be automatically applied.  Multi-inheritence is allowed/encouranged as a pattern.
*  **Attribute References** allow the re-use of individual governed attributes from existing models in a new model.

A programmer might want to start with an existing entity, add several new 
attributes, and then generate python dataclasses or pydantic models using the 
python-dataclass and python-pydandic perspectives respectively.


Defining Perspectives as Metadata 
------------------------------------------
Shows explicit structures for perspective definitions, specifically how 
the various types/enums are defined.

Examples of the basic SQL perspective:

.. uml:: sql_perspective.puml
   :align: center


.. literalinclude:: sql_perspective.json
   :language: json
