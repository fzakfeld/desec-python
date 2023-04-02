# desec-python

A desec.io API client for python.

## Installation

```
pip3 install desec
```

## Usage

```
import desec

desec_token = "xxxx"

client = desec.Client(token=desec_token)
```

```
# Get info about a domain
result = client.get_domain("example.com")
print(result)
```

```
# Get all recordsets of a domain
results = client.get_rrsets("example.com")
print(results)
```