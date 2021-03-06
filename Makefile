#J=bundle exec jekyll
J=jekyll

all: site

site: clean
	$J build #--lsi
	chmod -R a+rx ./_site/

clean:
	rm -rf _site/

local_all:
	$J serve --watch --drafts

local:
	$J serve --watch --drafts --limit_posts 300

profile:
	$J build --profile --limit_posts 1000
	
refresh:
	@echo "\nDeleting all posts..."
	rm -rf _posts/*

	@echo "\nGenerating posts..."
	tools/generate_posts.py

	@echo "\nDone."

refresh_push:
	@echo "Updating repo from GitHub..."
	git pull

	@echo "\nDeleting all posts..."
	rm -rf _posts/*

	@echo "\nGenerating posts..."
	tools/generate_posts.py

	@echo "\nAdding any new posts to git..."
	git add _posts/*

	@echo "\nCommitting changes..."
	git commit -a -m 'Refreshed links from Pinboard.'

	@echo "\nPushing to GitHub..."
	git push

	@echo "\nDone."
