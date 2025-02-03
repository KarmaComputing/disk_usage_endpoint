from flask import Flask, jsonify
import os
import sys
import shutil

app = Flask(__name__)


@app.route("/disk_space", methods=["GET"])
def disk_space():
    total, used, free = shutil.disk_usage("/")
    return jsonify({"total": total, "used": used, "free": free})


if __name__ == "__main__":
    port = (
        int(sys.argv[1])
        if len(sys.argv) > 1
        else int(os.getenv("DISK_USAGE_ENDPOINT_PORT", 5000))
    )
    app.run(host="0.0.0.0", port=port)
