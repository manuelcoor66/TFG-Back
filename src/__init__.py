import os

from flask import Flask, send_from_directory

from src.services.user_service import UserService

app = Flask(__name__)

userService = UserService()

if __name__ == '__main__':
    app.run(debug=True)


    @app.route('/favicon.ico', methods=['GET'])
    def favicon() -> 'Response':
        """
        Add swagger favicon
        """
        return send_from_directory(os.path.join(app.root_path, 'assets'), 'favicon.ico')
