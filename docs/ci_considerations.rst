.. how to think about CI

SCM & CI 
============
When using code generators in the software development process 
one should consider source control and *Continuous Integration* (CI).

Most all software development tooling is some form of code-generator, 
at least in an abstract sense.  We take *source code* in one language,
supply it to a *compiler*, and it produces some output, often either 
more source code or a *binary* of some kind (which is actually just more *code*,
though usually for the machine and not human consumption).

Source Control Management (SCM) tools (e.g.: *git* [hub/lab/etc]) are designed to store 
multiple versions of our code over time, like an extra-fancy shared file system.

*Generally*, we don't store the results of code compilation in SCM, rather storing 
those results in some kind of artifact distribution system e.g.: docker's image repositories,
maven repositories, Pypi for python, etc.  

With code-generation this presents a challenge as the outputs may not always be a package
based on a technology with a distribution ecosystem.  There are a few ways to handle this:

#.  Model & Build -> Discard Models, hand-modify output -> Check in output : This is *Full Self-Flagelation**
#.  Model & Build -> Check in Models, check in output(unchanged) : Let's call this *Manual Automation*
#.  Model & Build -> Check in Models, *CI* pipeline renders output -> package/tag/compile/publish results : 
    *Model Driven Development*

*NeuronSphere Artifact Librarian* can be used as a repository for these model driven outputs, with cli tools for packaging
and publishing available.  