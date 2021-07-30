# specchecker
checking specs
Steps installing on IIS
	1. Install python to c:\python39\
	2. c:\ mkdir pythonsites, cd pythonsites
	3. Confirm python --version
	4. Python -m venv specchecker
	5. Cd specchecker
	6. Scripts/activate
	7. Copy into specchecker, app.py, checkprj.py, flask_app.py, requirements.txt, spectools.py, web.config
	8. Pip install wfastcgi
	9. Run wfastcgi-enable
		a. Copy text for handler mapping in iis
	10. Pip install Flask
	11. Pip install -r requirements.txt
	12. Open IIS
	13. Create new site for specchecker
  14. Handler mappings > add module mapping
  15. Application settings > set 2 vars
  16. Tool will be available at localhost\tool
