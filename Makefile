run: venv/bin/activate
	echo "Running the application"
	./venv/bin/python3 ft_linear_regression/ft_linear_regression.py

venv/bin/activate: requirements.txt
	test -d venv || python3 -m venv venv
	./venv/bin/pip3 install -r requirements.txt

clean:
	rm -rf venv

.PHONY: run clean