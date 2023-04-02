import desec

desec_token = "xxxx"

client = desec.Client(token=desec_token)


results = client.get_rrsets("example.com")

print(results)
