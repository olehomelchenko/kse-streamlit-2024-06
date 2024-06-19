# Define the virtual environment directory
VENV_DIR = venv

# Define the requirements file
REQUIREMENTS_FILE = requirements.txt

# Create the virtual environment
$(VENV_DIR):
	python3 -m venv $(VENV_DIR)

# Activate the virtual environment and install requirements
.PHONY: install
install: $(VENV_DIR)
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS_FILE)

# Clean the virtual environment
.PHONY: clean
clean:
	rm -rf $(VENV_DIR)

# Run a command inside the virtual environment
.PHONY: run
run:
	$(VENV_DIR)/bin/python -m some_module

# Example of running a script inside the virtual environment
.PHONY: run-script
run-script:
	$(VENV_DIR)/bin/python script.py

# Run a Streamlit app inside the virtual environment
.PHONY: run-streamlit
run-streamlit:
	$(VENV_DIR)/bin/streamlit run app.py --server.address=127.0.0.1
