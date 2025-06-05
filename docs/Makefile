# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Custom target to regenerate API docs
.PHONY: apidoc
apidoc:
	@echo "Regénération de la documentation API..."
	@rm -rf $(SOURCEDIR)/modules/
	@sphinx-apidoc -f -o $(SOURCEDIR)/modules .. \
		--separate \
		--maxdepth 2 \
		../venv \
		../manage.py \
		../migrate_data.py \
		../utils \
		../.git
	@echo "Documentation API régénérée avec succès !"
	@echo "Nettoyage des fichiers migrations et tests..."
	@find $(SOURCEDIR)/modules/ -name "*migrations*" -delete 2>/dev/null || true
	@find $(SOURCEDIR)/modules/ -name "*test*" -delete 2>/dev/null || true

# Custom target to clean and rebuild everything
.PHONY: rebuild
rebuild: clean apidoc html
	@echo "Documentation complètement reconstruite !"

.PHONY: help Makefile clean

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
