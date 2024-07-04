```bash
pyenv virtualenv 3.9 debug_ctf
pyenv activate debug_ctf
pip install -r requirements.txt
```
Add the virtualenv you just created as the python SDK of the debug_ctf module, 
If you're using the default Dataiku setup, the virtualenv should be in
```bash
ls "/Users/$USER/.pyenv/x86/versions/debug_ctf/bin/python"
```

In each script, debug it so that it executes the line printing "Flag captured"

You're not allowed to add anything to the code itself (much like when debugging in a lib).

The goal is not to nerd snipe people, but to maybe expand a bit our horizons on the things you can do with a debugger.
In that sense, challenges 02 and 04 are probably the most important. But I added the others because I think it's fun :-D 

PRs welcome if you have additional ideas in the same format !