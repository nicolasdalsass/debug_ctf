```bash
pyenv virtualenv 3.9 debug_ctf
pyenv activate debug_ctf
pip install -r requirements.txt
```
Add the virtualenv you just created as the python SDK of the debug_ctf module, 
If you're using the default Dataiku setup, the virtualenv should be should be in
```bash
ls "/Users/$USER/.pyenv/x86/versions/debug_ctf/bin/python"
```

In each script, debug it so that it executes the line printing "Flag captured"

You're not allowed to add anything to the code itself (much like when debugging in a lib).