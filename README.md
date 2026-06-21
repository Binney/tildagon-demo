# Tildagon Badge App Demo

This is an example app for Tildagon, the EMF badge.

## How to use this app

Hit the big green "Code" button on Github and download a ZIP of this folder. Unzip it onto your computer and follow the instructions [here](https://tildagon.badge.emfcamp.org/tildagon-apps/run-on-badge/) to get it running on your badge. Then, hack away!

Alternatively, if you don't have a badge handy, you can use the simulator. Follow the instructions [here](https://tildagon.badge.emfcamp.org/tildagon-apps/simulate/) to get the simulator up and running. Copy this entire demo app folder into the `sim/apps/` folder. Restart the simulator and you'll see the Demo App there in the main menu.

If you're comfortable with Git, why not fork this repository and clone into it instead of downloading as a ZIP, treat yourself ;)

## Structure

Your app lives in `app.py`. Read more [here](https://tildagon.badge.emfcamp.org/tildagon-apps/development/). Or look up the more complete reference docs [here](https://tildagon.badge.emfcamp.org/tildagon-apps/reference/reference/).

`tildagon.toml` is where your app's publish metadata lives. When you want to publish your app to the store, you'll need to update that to get the app to show up just the way you want in the store.

`metadata.json` helps your badge to load your app while you're developing it, before submitting to the store. It's only used for local development with [the simulator](https://tildagon.badge.emfcamp.org/tildagon-apps/simulate/) or while running the app directly on your badge with [mpremote](https://tildagon.badge.emfcamp.org/tildagon-apps/run-on-badge/).

We've also got a `.gitattributes` file to tell the store that some files in this folder shouldn't be included in the download to the store - like this README file! Remember to keep the app download nice and small so there's more room for juicy apps on users' devices.

