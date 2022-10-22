# Voter
With great power comes great responsibility.

## Prerequisite
- Microsoft Edge is needed

## Install
- Run `pip install -r requirements.txt`

## Configure
- Set `url` in `config.py`
- (Optional) Toggle `headless` in `config.py` if you like
- (Optional) Check `config.py` and adjust other configurations

## Run
- Just run `python main.py`

## Run GUI
- Just run `python gui.py`

## (CAUTION!!!) Run INFINITE
- Just run `python infinite.py`

## Develop & Distribute
- Run `pip install -r requirements-dev.txt`
- Run `black .` to reformat code
- Run `pyinstaller .\main.spec` and find the script app in `dist/`
- Run `pyinstaller .\gui.spec` and find the GUI app in `dist/`