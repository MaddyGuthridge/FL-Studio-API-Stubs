# Gather code coverage display results in a web browser
coverage run -m pytest \
&& coverage report \
&& coverage html \
&& python -m webbrowser htmlcov/index.html > /dev/null 2>&1
