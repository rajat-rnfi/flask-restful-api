import os
from . import app  # from __init__ file
from . import urls

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True if os.getenv(
        "APP_ENV") == 'local' else False)
