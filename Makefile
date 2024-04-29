seed:
	python manage.py seed_superuser && python manage.py seed_users && python manage.py seed_customers && python manage.py seed_manufacturers && python manage.py seed_vessels && python manage.py seed_products && python manage.py seed_cases

test-dev:
	python manage.py test --settings=project.settings-test

