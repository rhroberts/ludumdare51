# Ludum Dare 51

## Development Setup

```bash
# create virtual environment
python -m venv env
# for bash:
source env/bin/activate
# for powershell:
./scripts/activate
# install dependencies
pip install -r requirements.txt
# run it
python src/main.py
```

## Packaging

The filepaths you specify will be copied into the package app directly, so copying this exactly matters. From the root directory, run

```pyxel package . src/main.py```

`pyxel` will generate an app file named `.pyxapp`. So far, I don't know how to give it a sane name, so rename that file to whatever you like with the `.pyxapp` extension. You know, something like `dug_dirt.pyxapp`..
