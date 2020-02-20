install:
	poetry install

publish_test:
	poetry config repositories.kotano-brain-games https://test.pypi.org/legacy/
	poetry publish -r kotano-brain-games

lint:
	poetry run flake8 brain_games