# Ludum Dare 51 - It's Doug Dirt!

<img src="./assets/opening_screenshot.png" alt="Opening Screen Image" width="450" height="450">

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

`pyxel` will generate an app file named `..pyxapp`. So far, I don't know how to give it a sane name, so rename that file to whatever you like with the `.pyxapp` extension. You know, something like `doug_dirt.pyxapp`..

## Deployment

We use github pages to host, so the game is hosted at `https://rhroberts.github.io/ludumdare51/`. To deploy, package up the game and push it to the `gh-pages` branch. That's it!

## Gameplay

<img src="./assets/gameplay.gif" alt="Gameplay Example" width="450" height="450">

Find the buried treasure! Memorize the terrain and avoid obstacles! Use the radar to your advantage!

Utilize `WASD` for movement and `R` to restart.