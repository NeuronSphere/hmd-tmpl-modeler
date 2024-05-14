.. describes the basis of the model branching user experiences

Model Collaboration via Branching 
===========================================
A core capability of NeuronSphere Modeler is collaboration using a 
technique called *branching*.

The general flow for model collaboration is: 

#.  When a model owner[fn1] wishes to collaborate with someone, they *share a 
    collaboration link*.  This is similar to creating a *public read-only* link, 
    but requires the addition of the collaborating users' email address(es).

    #.  For each email address entered, Modeler will create a collaboration link that 
        is only accessible by that user.  Note the user may not exist at the time of
        link creation.  
    #.  The collaboration links show up in the same place as the read-only links a 
        model owner has created, and click tracking, aging, etc are all equally 
        available for collaboration links as for read-only.
    #.  Link owner needs to be able to "re-copy link to clipboard" from link listing, or have the 
        option to "re-send collaboration email" (ideally both).
    #.  A baseline of 1 *Collaboration Credit* is assigned to the link at creation time.  If the 
        collaborating user exists and is a Professional user, no credit is used, else standard credit 
        (less promotion) rate applies to the link. 

#.  When a *collaborator* clicks a collabortion link, in addition to regular link-tracking
    activity, the following *branching* activities occur.

    #.  A new *Branch* object is created, named by default "yyyy_mmm_dd_<collabo_user_email>" 
        where the datestamp is the date the target collaboration user clicked the link.
    #.  The new Branch is linked to the collaboration target user as the 
        branch owner.
    #.  The branch is also tied to the model that is being collaborated on.


What is stored in a Branch?  A *model-delta* (as a blob) containing changes from the source model 
at a given point in time.  When a collaborating user is working on editing a model, their
changes result in a new model-state and that model-state has a delta calculated against the 
baseline model, and that delta is stored as the updated model-delta.  This may also be 
refered to as a *model diff* as it is the logical difference between any 2 models, 
or the same model at 2 points in time.  

Note when the collaborating user comes back to a branch, an auto-baseline to current model state
should be done, and the user presented with the applied changes.



In the overview graph user interface, if there are branches for a model, a drop-down 
list of checkboxes is displayed at the top of the canvas with the *Open* branches 
listed in sorted order.  

When the checkbox next to a branch is selected, its model-diff is applied to the current model state.
Where the model-diff is producing changes, the UI should highlight theses areas.

*  New entities should be boldy outlined in the branch's color 
*  Removed entities should be shown partially transparent, with their 
   outlines replaced as dotted lines
*  New or changed attributes have bold text and branch color bold 
   outlines around their containing cells.  This applies to any attribute change.
*  Hovering over a new or updated entity header should show the diff, and similarly 
   hovering over a changed attribute should show details of attribute diff 
   (e.g. 'description changed' or 'extension added')




[fn1]the single owner of a model or a member of the group that owns a model

.. note:: Developers should be very familiar with these ideas as they logically
          mirror what source control systems do for line-oriented source files.