up-local-server:
	docker-compose -f docker-compose.yml up -d web

down-local-server:
	docker-compose -f docker-compose.yml down web

migration-file:
	@if [ -z "$(MIGRATION_MESSAGE)" ]; then \
		echo "MIGRATION_MESSAGE is not set"; \
		exit 1; \
	fi
	docker-compose run --rm migration \
	/bin/bash -c " \
	python -m poetry install && \
	poetry run alembic revision --autogenerate -m ${MIGRATION_MESSAGE}"

run-migration:
	docker-compose run --rm migration \
	/bin/bash -c " \
	python -m poetry install && \
	poetry run alembic upgrade head"


test:
	docker-compose -f docker-compose.yml -f docker-compose.test.yml build
	docker-compose -f docker-compose.yml -f docker-compose.test.yml run --rm web 
	docker-compose -f docker-compose.yml -f docker-compose.test.yml down
	docker image  prune -f
