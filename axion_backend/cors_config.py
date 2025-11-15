from flask_cors import CORS


def configure_cors(app):
    """Configure CORS for the Flask app.

    - Allows Vercel preview/production domains and the Render backend domain.
    - Enables support for credentials (cookies) when needed.
    - Ensures preflight (OPTIONS) requests are handled automatically.
    """

    # Allow localhost and common dev hosts plus Vercel/Render domains
    origin_patterns = [
        r"http://localhost(:\d+)?",
        r"http://127\.0\.0\.1(:\d+)?",
        r"https://[a-z0-9-]+\.vercel\.app",
        r"https://axion-digitaverse(-[a-z0-9]+)?\.vercel\.app",
        r"https://axion-network\.onrender\.com",
        r"https://axion-backend(-[a-z0-9]+)?\.onrender\.com",
    ]

    # Use a compiled regex by joining patterns
    origin_regex = "^(" + "|".join(origin_patterns) + ")$"

    CORS(
        app,
        resources={r"/*": {"origins": origin_regex}},
        expose_headers=["Content-Disposition"],
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization", "X-Requested-With", "Origin"],
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    )
