.. how to add new templates

New Templates
=================
Adding new templates is a simple process:

#.  Add new director(ies) and template(s)

    *  Create a new directory in {project_root}/src/mickey/templates to contain your new 
       templates.  Simple name, no spaces or special characters.
    *  Use *mickey magic folders* such as {{ mickey.src_folder }} as a folder name and 
       it's content will be placed in {project_root}/src.  You may also use: {{ mickey.docs_folder }},
       {{ data.namespace }}, and {{data.name}} (based on template cardinality).

#.  Update manifest configuration

    *  Add a new entry in the file {project_root}/meta-data/manifest.json under the 
       *generate* key.  This is the configuration that maps a logical name in the mickey 
       config section of the manifest to a collection of models, templates, and hooks.

       This example adds a config named *pydantic*

       .. code:: json
          
          "pydantic": {
              "contexts": ["ref:entity_data"],
              "templates": ["hmd-tmpl-modeler/pydantic"],
              "hooks": ["./src/mickey/hooks/add_jinja_filters.py"]
          }


       .. note:: The *contexts* key above determines the *template set cardinality*.  This 
           determines if the templates are rendered once per *Entity* in the data model, or 
           rendered once, with all *Entities'* rendering in a single output.  

           Looking at the examples should clarify this subject.


#.  Execute and test until satisfied with output

    *  Executing *hmd mickey build* will render all configurations in the manifest, 
       but during highly iterative development or for special uses this will wastes time
       rendering configurations that are not needed.

       Instead, execute *hmd mickey build pydantic* to render just the new example added above.


Template Pack Design Guidelines
----------------------------------
#.  Name the folder containing your templates *well*.  What's in a good name?  Short, no special characters, meaningful
    to what the template pack produces.
#.  Decide were the outputs will *go* in your project's source tree and as a part of builds.  Depending on your technology and
    code-generation strategies, it may be easy to place all generated code into a /gen directory at the project root, or 
    in a src/gen directory.
#.  Your templates should almost always output something into /docs via the {{mickey.docs_folder}}.  
    Generating documentation that matches the code, configuration, and data models is a useful and powerful side-effect 
    of model driven development.
#.  Please mind the .gitignore