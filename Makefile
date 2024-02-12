INSTALL_PATH = "$${HOME}/git/iscls/iscls.github.io/docs/"

serve:
	bundle exec jekyll serve

setup:
	bundle install

schedule:
	cd _scripts/ && python build_schedule.py && xelatex schedule.tex && cp schedule.pdf ../assets/files/

build:
	export JEKYLL_ENV="production" && bundle exec jekyll build

publish: build
	rsync -avzc --delete _site/ ${INSTALL_PATH}
