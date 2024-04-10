.. local usage instructions

Basic Use
=========

NeuronSphere Modeler uses the freely-available code-generating 
tool *hmd mickey*.  Mickey is a python-based cli that uses the templating
library jinja2.

To render these templates with your data models on your computer:

#.  Install *mickey* 

    .. code:: console

       projects %> pip install hmd-cli-mickey

#.  Clone the template repository

    .. code:: console 

       projects %> git clone https://github.com/NeuronSphere/hmd-tmpl-modeler.git

#.  Add your models - while *hmd mickey* can consume an array  of data formats containing
    essentially any data model(s), the templates in this repository are all designed to 
    consume  NeuronSphere Entity Models and their extensions.  
    
    Use one of these options:
    
    *.  Use the `NeuronSphere Modeler <https://modeler.neuronsphere.io/>`_ to create and collaborate on 
        your data model and export it.  Within the exported zip file there is a 'src' directory containing 
        a 'schemas' folder.  Place that schemas folder within the 'src' folder of this (hmd-tmpl-modeler) repository.
    *.  Manually create the appropriate *.hms* files and place them into 'src/schemas/<namespace>' in 
        this (hmd-tmpl-modeler) repository.  This is possible, but annoying to do manually.
    
#.  Run mickey for all templates 

    .. code:: console 
       
       projects %> cd hmd-tmpl-modeler 
       hmd-tmpl-modeler %> hmd mickey build


Repository Layout
------------------

*  /docs - docs and drawings as code, rendered with *hmd-cli-bartleby*
*  /src - souce code and models 
*  /test - RobotFramework test suites
*  /meta-data - NeuronSphere manifest.json, VERSION file, and other NeuronSphere tooling & project metadata.

This repository is a *NeuronSphere Compliant Repository*.
