1. python -m venv venv

2. venv\Scripts\activate

3. Create one file called app.py

4. Create two folder, one for docs and one for templates.

5. Write the code in app.py 
(Example - Hello world)

Example:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "First flask project"

app.run()
```


6. 
```python
print("Hello")
print("World")
```

7. To preview md file as note 
CTRL + SHIFT + V


8. To run flask code 
python app.py

9. To stop the server
CTRL+C

10. To Automate the Reloading:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "First Flask  project"

app.run(debug=True)

```

or

```python
app.run(debug=True)
```

11.
localhost:5000


12. 
## What is Flask?
* Python Framework
* Flask - Web Framework
* Python WebFramework - Django,Flask etc
* Django - used in instagram,mozilla etc.
* Django - Web Framework
* Django - 2005
* Size of the Django - 8.9 MB
* Flask - micro web framework 
* Flask - 2010 
* Flask - Applications that use the Flask framework include **Pinterest and LinkedIn**.


* CTRL + shift + p
color theme


13. In templates folder
* add login.html file
* add signup.html
* add homepage.html
