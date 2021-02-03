mkdir -p ~/.streamlit/
echo "[general]
email = \"ram20.91999@gmail.com\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml