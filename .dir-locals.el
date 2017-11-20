;; Emacs django-mode settings
((python-mode
  (python-shell-interpreter . "python3")
  (python-shell-interpreter-args . "/home/wsg/hack/python/rest_app/manage.py shell")
  (python-shell-prompt-regexp . "In \\[[0-9]+\\]: ")
  (python-shell-prompt-output-regexp . "Out\\[[0-9]+\\]: ")
  (python-shell-completion-setup-code . "from IPython.core.completerlib import module_completion")
  (python-shell-completion-module-string-code . "';'.join(module_completion('''%s'''))\n")
  (python-shell-completion-string-code . "';'.join(get_ipython().Completer.all_completions('''%s'''))\n")
  (python-shell-extra-pythonpaths "/home/wsg/hack/python-venv/rest-app/movies")
  (python-shell-virtualenv-root . "/home/wsg/hack/python-venv/rest-app")))
