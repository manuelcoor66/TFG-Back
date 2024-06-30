import os

from flask import Flask, send_from_directory

app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)

    @app.route("/favicon.ico", methods=["GET"])
    def favicon():
        """
        Add swagger favicon
        """
        return send_from_directory(os.path.join(app.root_path, "assets"), "favicon.ico")
