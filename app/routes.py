from app import app

@app.route('/')
def hello():
    return "Hello, this is the Blue-Green Deployment App!"

