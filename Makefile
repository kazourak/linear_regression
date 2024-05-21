run: venv/bin/activate
	echo "Running the application"

predict: venv/bin/activate
	echo "Running the prediction program"
	./venv/bin/python3 predict_program.py

train: venv/bin/activate
	echo "Running the training program"
	./venv/bin/python3 train_program.py

venv/bin/activate: requirements.txt
	test -d venv || python3 -m venv venv
	./venv/bin/pip3 install -r requirements.txt

clean:
	rm -rf venv

.PHONY: run clean
