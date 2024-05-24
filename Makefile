run: venv/bin/activate
	echo "Running the application"

predict:
	echo "Running the prediction program"
	./venv/bin/python3 predict_program.py

train:
	echo "Running the training program"
	./venv/bin/python3 train_program.py
	
evaluate:
	echo "Running the evaluate program"
	./venv/bin/python3 evaluate_program.py
	
venv/bin/activate: requirements.txt
	test -d venv || python3 -m venv venv
	./venv/bin/pip3 install -r requirements.txt

clean:
	rm -rf venv

test:
	./venv/bin/pytest tests

.PHONY: run clean predict train evaluate test
