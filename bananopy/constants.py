from os import environ

BANANO_HTTP_PROVIDER_URI = environ.get(
    "BANANO_HTTP_PROVIDER_URI", "https://api-beta.banano.cc"
)
PORT = environ.get("PORT", 7072)

print(f"Using {BANANO_HTTP_PROVIDER_URI} as API provider")
