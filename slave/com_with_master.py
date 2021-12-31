import requests
r = requests.post("http://52.170.64.22:1234", data={'me': 'mario'})
# And done.
print(r.text) # displays the result body.