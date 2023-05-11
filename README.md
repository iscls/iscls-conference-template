# Jekyll-based Conference Template

An academic conference website template built using Jekyll.

## Configuration

Data Files under `_data` to configure all conference related information.

- `conference.yml`
  - `full_title`: conference fullname e.g., First xxx conference on xxxx, 2017.
  - `short_title`: conference shortname e.g., xxxx2017
  - `description`: short description about the conference (< 160 char)
  - `location`: conference location
  - `logo_path`: conference logo
  - `slideshow`: images slideshow
  - `navbar`: navigation menu.
  - `sponsors`: sponsor section.
  - `deadlines`: important dates of deadlines, pass-due date will be automatically printed with del line.
  - `social_media`: social media on the navbar. (current support facebook and twitter.)
- `news.yml`: news section
- `organization.yml`: committees
  - `programm_chair`: program chair
  - `organizing_committees`: organizing committees
  - `steering_committees`: steering committees
  - `technical_program_committees`: technical program committees
- `venue.yml`: information about venue
  - `address`: full address
  - `accommodation`: accommodation details
  - `direction`: path to image containing directions
- `submission.yml`: submission instructions
- `registration.yml`: registration information

- Google Analytics: in `_config.yml`

## Deployment

### Manual

* Setup Ruby, RVM, Jeykyll, Bundler.
  - Check installation instructions at [INSTALL.md](INSTALL.md).
* Remove `.github/workflows/`
* Change target of the symbolic `Gemfile` to `Gemfile.local`
  ```
  rm Gemfile
  ln -s Gemfile.local Gemfile
  ```
* Adjust release path in `Makefile`
* Test locally, `make serve`
* Build and copy to publish location, `make publish`
* Commit changes to the publish location

### GitHub Pages

* Ensure that the repository is public and GitHub Pages are enabled and set to use GitHub Actions.
* Create `.github/workflows`
* Copy `workflows/release.yml` to `.github/workflows/release.yml`
* Change target of the symbolic `Gemfile` to `Gemfile.github`
  ```
  rm Gemfile
  ln -s Gemfile.github Gemfile
  ```
