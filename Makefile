publish:
	python setup.py register
	python setup.py sdist upload
	python setup.py bdist_wheel --universal upload
	rm -fr build dist .egg cmp_dict.egg-info
