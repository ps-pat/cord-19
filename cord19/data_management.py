from urllib import request

def _make_request(root, date, filename):
    return request.Request("/".join([root, date, filename]))

def fetch_data(date):
    ## Helper variables.
    root = "https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com"

    ## Requests.
    requests = [_make_request(root,
                              date,
                              "all_sources_metadata_"
                              + date
                              + ".csv"),
                _make_request(root,
                              date,
                              "comm_use_subset.tar.gz"),
                _make_request(root,
                              date,
                              "noncomm_use_subset.tar.gz"),
                _make_request(root,
                              date,
                              "pmc_custom_license.tar.gz"),
                _make_request(root,
                              date,
                              "biorxiv_medrxiv.tar.gz")]

    return [request.urlopen(req).read() for req in requests]





## Local Variables:
## python-shell-interpreter: "ipython3"
## End:
