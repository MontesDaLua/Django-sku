PYTHON	:= /usr/bin/python
EGREP	:= /bin/egrep
SED	:= /bin/sed
RM	:= rm -f 
BINDIR	:= ~/bin
GIT	:= /usr/bin/git
VALIDATOR	:= $(BINDIR)/HTMLvalidator.py

clean:
	$(RM) *.pyc

commitlocal:
	$(GIT) commit -a -m '$(GITCOMMITMESSAGE)'

commitremote:
	$(GIT) push origin --tags
	$(GIT) push origin development	

test:
	cd $(DEVSITE); python manage.py test $(APP); cd $(APP)

validate: 
	cd $(DEVSITE)/$(APP); for i in `find . -type f -print | grep \.css$$`; do  $(VALIDATOR) $$i; done
	for i in $(DEVSITE)/$(APP)/$(APPSNAPHTMLDIR)/*; do $(VALIDATOR) $$i ; done

admin.py: models.py
	@echo "############# creating admin.py "
	$(BINDIR)/auto_admin.sh
	cd $(DEVSITE) ; $(PYTHON) manage.py validate; cd $(APP)
	cd $(DEVSITE) ; $(PYTHON) manage.py syncdb ; cd $(APP)
	@echo "############# end creating admin.py "


$(DISTFILE):
	@echo "############# creating distribution for $(APP) "
	mkdir -p dist.old
	touch $(DISTDIR)/MARK
	mv dist/* dist.old
	# ftp test site 
	$(PYTHON) setup.py sdist
	$(BINDIR)/dist_ftp.sh
	@echo "############# end creating distribution for $(APP) "

messages:
	for i in $(APPLANGUAGES); do django-admin makemessages --locale $$ii --extension=html,txt,py; done
	echo "consider to translate via Google at http://translate.google.com/toolkit/list?hl=pt_PT#translations/active "
	django-admin  compilemessages 

all : $(PYTHONFILES) 
	@echo "############# making everything for  $(APP) "
	@echo "# sql can be checked with cd $(DEVSITE); $(PYTHON) manage.py  sql $(APP); cd $(APP)"
	@echo "# interactive test with cd $(DEVSITE); $(PYTHON) manage.py shell; cd $(APP)"
	@echo "#online test with python cd $(DEVSITE); $(PYTHON) manage.py runserver localhost:8080; cd $(APP)"
	@echo "############# end making everything for  $(APP) "



