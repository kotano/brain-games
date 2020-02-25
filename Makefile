install:
	poetry install

publish_test:
	poetry config repositories.kotano-brain-games https://test.pypi.org/legacy/
	poetry publish -r kotano-brain-games

lint:
	poetry run flake8 brain_games

install_from_pip:
	pip install -i https://test.pypi.org/simple --extra-index-url https://pypi.org/simple kotano-brain-games --upgrade