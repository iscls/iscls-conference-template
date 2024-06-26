# Install

The template is powered by Jekyll and tuned to work with GitHub workflows.

For local deployment, use `Gemfile.local`

## Requirements

* Ruby (`v3.2.1`)
* Gems:
  - Bundler
  - Jekyll

## Instructions

* Install **rvm** (Ruby Version Manager) by following the instructions from https://rvm.io/
  - `rvm use 3.2.1`
* Install Jekyll
  - `gem update --system`
  - `gem install sass-embedded`
  - `gem install bundler jekyll`
* Repository setup
  - Clone the repository
  - Change directory to the clone location
  - `make setup` OR `bundle install`
* Configure
  - Edit `_config.yml`
  - Edit `_data/*.yml` for conference configuration
  - Edit `index.md`
  - Edit `history.md`
* Test
  - `make serve`
* Build
  - `make build`
* Publish (Currently, copy the built directory to install location)
  - Edit `Makefile` to set your install path
  - `make publish`
  - **NOTE**: You will need to manually commit the code for the website.
