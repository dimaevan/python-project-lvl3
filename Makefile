install:
	@poetry install
build:
	@poetry build
publish:
	@poetry publish --dry-run
activate:
	@poetry shell
test:
	@poetry run pytest
lint:
	@poetry run flake8 page_loader/