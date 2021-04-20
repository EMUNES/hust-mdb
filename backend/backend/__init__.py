"""Always add static files, templates and templates files in
subfolder for each app, because django will merge all those files 
into the same folder so if you don't put them in subfolder there will
be troublesome overriden file problems.
"""