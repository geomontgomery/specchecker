# specchecker

checking specs, here are the steps to installing on IIS
```bash
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
	13. [Create new site for specchecker](https://imgur.com/a/qliUdYf)
  14. Handler mappings > add module mapping
  15. Application settings > set 2 vars
  16. Tool will be available at localhost\tool
```
![13. Create new site for specchecker](https://user-images.githubusercontent.com/33534161/127656369-4d3dd48e-e884-4f26-9960-8ac33dfc6249.png)
![14.Handler Mappings > add module mappings](https://user-images.githubusercontent.com/33534161/127656219-3c259494-883c-4121-af06-c87724a06132.png)
![15. Application Settings > set 2 vars](https://user-images.githubusercontent.com/33534161/127656279-5d674bb9-8a14-425e-b6c6-b3a3d9a6c7bc.png)
![image](https://user-images.githubusercontent.com/33534161/127656499-f72de272-c93f-4b42-abad-0e0f23c8f727.png)
