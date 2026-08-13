from flasgger import Swagger
from app import create_app

app = create_app()

swagger = Swagger(app, template={
    "info": {
        "title": "Comment Service API",
        "version": "1.0.0",
        "description": "Izohlar servisi"
    }
})

if __name__ == '__main__':
    app.run(port=8003, debug=True)