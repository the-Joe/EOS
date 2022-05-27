all: eos eos.service
.PHONY: all eos install uninstall
lib_dir=/usr/local/lib/eos
conf_dir=/usr/local/etc/eos
service_dir=/etc/systemd/system
service_lib_dir=/usr/lib/systemd/system
venv=$(lib_dir)/venv

install: $(service_dir) eos.service
	@echo Installing the service files...
	cp eos.service $(service_dir)
	chown root:root $(service_dir)/eos.service
	chmod 644 $(service_dir)/eos.service

	@echo Installing library files...
	mkdir -p $(lib_dir)
	cp eos.py $(lib_dir)
	cp eos_service.py $(lib_dir)
	cp eos_access.py $(lib_dir)
	chown root:root $(lib_dir)/*
	chmod 644 $(lib_dir)/*

	@echo Installing configuration files...
	mkdir -p $(conf_dir)
	cp eos.env $(conf_dir)
	chown root:root $(conf_dir)/*
	chmod 644 $(conf_dir)/*

	@echo Creating python virtual environment and installing packages...
	python3 -m venv $(venv)
	$(venv)/bin/pip3 install -r requirements.txt

	@echo Installation complete...
	@echo run 'systemctl start eos' to start service
	@echo run 'systemctl status eos' to view status

uninstall:
	-systemctl stop eos
	-systemctl disable eos
	-rm -r $(lib_dir)
	-rm -r $(conf_dir)
	-rm -r $(service_lib_dir)/eos.service
	-systemctl daemon-reload
	-systemctl reset-failed
