from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return '''<html>
					<body bgcolor='gray' text='white'>
						<h1>Secure CI/CD Pipeline Demo</h1>
							<ul>
								<li> Setup a basic CI/CD pipeline with GitHub Actions </li>
								<li> Integrate security scanning into the pipeline </li>
								<li> Automate security checks on every push </li>
								<li> Bonus: Deploy to DockerHub </li>
							</ul>
					</body>'''

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)