while :; do
  curl --location --request POST 'https://api.telegram.org/bot{}/sendMessage?parse_mode=markdown&chat_id={}&text=Go%20Away!!'
  sleep 1
done
