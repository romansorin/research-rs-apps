from urllib.parse import parse_qs, quote_plus
from future.standard_library import install_aliases
from botocore.vendored import requests
import getopt
import logging
import sys
import os
from dotenv import load_dotenv
load_dotenv()


install_aliases()

# ************* REQUEST VALUES *************
host = 'ats.stage.api.alexa.com'
endpoint = 'https://' + host
method = 'GET'
logging.basicConfig()
log = logging.getLogger("ats")
content_type = 'application/json'
local_tz = "America/New_York"
api_key = os.getenv('API_KEY')


###############################################################################
# usage                                                                       #
###############################################################################
def usage():
    sys.stderr.write("""
Usage: main.py [options]

  Make a signed request to Alexa Top Sites API service

  Options:
     -a, --action            Service Action
     -k, --key               API Key
     -c, --country           2-letter Country Code (ie. US, CN, BR)
     -o, --options           Service Options
     -?, --help              Print this help message and exit.

  Examples:
     TopSites by country: main.py -k 98hu7.... --action TopSites --country=US --options "&Count=100&Output=json"
""")


###############################################################################
# parse_options                                                               #
###############################################################################
def parse_options(argv):
    """Parse command line options."""

    opts = {}

    urlargs = {}

    try:
        user_opts, user_args = getopt.getopt(
            argv,
            'k:a:c:o:?',
            ['key=', 'action=', 'country=', 'options=', 'help='])
    except Exception as e:
        print('Command parse error:', e)
        log.error("Unable to parse command line")
        return None

    if ('-?', '') in user_opts or ('--help', '') in user_opts:
        opts['help'] = True
        return opts

    #
    # Convert command line options to dictionary elements
    #
    for opt in user_opts:
        if opt[0] == '-k' or opt[0] == '--key':
            opts['key'] = opt[1]
        elif opt[0] == '-a' or opt[0] == '--action':
            opts['action'] = opt[1]
        elif opt[0] == '-c' or opt[0] == '--country':
            opts['country'] = opt[1]
        elif opt[0] == '-o' or opt[0] == '--options':
            opts['options'] = opt[1]
        elif opt[0] == '-a' or opt[0] == '--action':
            opts['action'] = opt[1]
        elif opt[0] == '-v' or opt[0] == '--verbose':
            log.verbose()

    if 'key' not in opts or \
            'action' not in opts or \
            'country' not in opts:
        return None

    #
    # Return a dictionary of settings
    #
    success = True
    return opts


###############################################################################
# sortQueryString                                                             #
###############################################################################
def sort_query_string(query_string):
    query_tuples = parse_qs(query_string)
    sorted_query_string = ""
    sep = ""
    for key in sorted(query_tuples.keys()):
        sorted_query_string = sorted_query_string + sep + \
            key + "=" + quote_plus(query_tuples[key][0])
        sep = "&"
    return sorted_query_string


###############################################################################
# main                                                                        #
###############################################################################
if __name__ == "__main__":

    opts = parse_options(sys.argv[1:])

    if not opts:
        usage()
        sys.exit(-1)

    if 'help' in opts:
        usage()
        sys.exit(0)

    canonical_uri = '/api'

    canonical_querystring = 'Action=' + opts['action']
    canonical_querystring += "&" + 'CountryCode=' + opts['country']
    canonical_querystring += "&" + 'ResponseGroup=Country'
    if 'options' in opts:
        canonical_querystring += "&" + opts['options']
    canonical_querystring = sort_query_string(canonical_querystring)

    headers = {'Accept': 'application/json',
               'Content-Type': content_type,
               'x-api-key': opts['key']
               }

    # ************* SEND THE REQUEST *************
    request_url = endpoint + canonical_uri + "?" + canonical_querystring

    print('\nBEGIN REQUEST++++++++++++++++++++++++++++++++++++')
    print('Request URL = ' + request_url)
    r = requests.get(request_url, headers=headers)

    print('\nRESPONSE++++++++++++++++++++++++++++++++++++')
    print('Response code: %d\n' % r.status_code)
    print(r.text)
