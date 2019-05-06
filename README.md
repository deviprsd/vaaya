# Vaaya
An inteligent journal, doing emotional analysis on texts. To use this app you need to have
`pipenv` which can be downloaded from this website https://pipenv.readthedocs.io/en/latest/

# Installations
Once you have pipenv installed run the following commands
```bash
vaaya> pipenv install #one time
vaaay> pipenv shell # everytime a new terminal is opened
vaaya> pipenv update # one time
vaaya> cd ..
> python -m vaaya # to start the program
```

# Know Issues
There is one issue, when you run it for the first time it will
download a dependency of size 800mb. After downloading, it tried to 
load it for usage (often times failing). It works after the program is restarted,
couldn't find a band-aid for now :(