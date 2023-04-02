import desec

desec_token = "xxxx"

client = desec.Client(token=desec_token)


result = client.get_domain("example.com")

print(result)
