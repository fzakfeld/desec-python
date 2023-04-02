# desec-python
# Copyright 2023 Freerk-Ole Zakfeld (github.com/fzakfeld)
# See LICENSE for details.

"""
desec.io Python Client
"""

import requests
from .models import RRSet, Domain

class Client():
    BASE_URL = "https://desec.io/api/v1"

    def __init__(self, token: str):
        self.token = token
        pass

    def get_domains(self) -> list[Domain]:
        data = self.make_request("/domains/")
        results = []
        for x in data:
            results.append(Domain.from_dict(x))
        return results

    def get_domain(self, domain_name: str) -> Domain:
        data = self.make_request(f"/domains/{domain_name}")
        return Domain.from_dict(data)

    def get_rrsets(self, domain_name: str) -> list[RRSet]:
        data = self.make_request(path=f"/domains/{domain_name}/rrsets/")
        results = []
        for x in data:
            results.append(RRSet.from_dict(x))
        return results
    
    def create_rrset(self, domain_name: str, rrset: RRSet):
        self.make_request(path=f"/domains/{domain_name}/rrsets/", method="POST", data=rrset.to_json())

    def update_rrset(self, domain_name: str, rrset: RRSet):
        self.make_request(path=f"/domains/{domain_name}/rrsets/{rrset.subname}/{rrset.type}/", method="PUT", data=rrset.to_json())

    def make_request(self, path: str, method: str = "GET", data = None):
        r = requests.request(
            method=method,
            url=self.BASE_URL + path, 
            headers={
                "Authorization": f"Token {self.token}",
                "Content-Type": "application/json"
            },
            data=data
        )
        return r.json()