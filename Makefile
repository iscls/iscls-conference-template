INSTALL_PATH = "/home/hrishirt/git/iscls/iscls.github.io/docs/"

setup:
	bundle install

serve:
	bundle exec jekyll serve

build:
	export JEKYLL_ENV="production" && bundle exec jekyll build

publish: build
	rsync -avzc --delete _site/ ${INSTALL_PATH}
