import requests
import os
import sys
import time
import json
import itertools

BASE_URL = "https://graph.facebook.com/"

class Endpoint(object):
    def __init__(self, path, params):
        self.path = path
        self.params = params

    def call(self, path):
        sys.stderr.write(".")
        sys.stderr.flush()
        while True:
            try:
                if path[:len(BASE_URL)] == BASE_URL:
                    path = path[len(BASE_URL):]
                url = os.path.join(BASE_URL, path)
                res = requests.get(url, params=self.params, timeout=10)

            except Exception as e:
                sys.stderr.write("\nERROR: {0} \n".format(e))
                sys.stderr.flush()
                time.sleep(10)
                continue

            if res.status_code != 200:
                sys.stderr.write("STATUS CODE {0} @ {1}\n".format(
                    res.status_code,
                    path,
                ))
                json.dump(res.json(), sys.stderr, indent=4)
                if res.status_code in [ 400, 404 ]:
                    return { "data": [] }
                time.sleep(10)
                continue

            return res.json()

    def iter_results(self, max_results=None):
        n_results = 0
        first_page = self.call(self.path)
        for r in first_page["data"]:
            yield r
            n_results += 1
            if max_results != None and n_results >= max_results:
                return
        previous_page = first_page
        while True:
            if max_results != None and n_results >= max_results:
                break
            next_path = previous_page.get("paging", {}).get("next", False)
            if next_path:
                new_page = self.call(next_path)
                for r in new_page["data"]:
                    yield r
                    n_results += 1
                    if max_results != None and n_results >= max_results:
                        return
                previous_page = new_page
            else:
                break

    def get(self, max_results=None):
        return list(self.iter_results(max_results=max_results))
