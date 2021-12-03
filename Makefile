install:
	poetry install
check:
	poetry check
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	pip install --user dist/*.whl
activate:
	poetry shell
test:
	poetry run pytest
lint:
	poetry run flake8 page_loader/ tests/