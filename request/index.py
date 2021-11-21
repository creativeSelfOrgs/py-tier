
def load_config(name_key):
    from os import environ, path
    from dotenv import load_dotenv

    # Find .env file
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, '.env'))

    return environ.get(name_key)


def post_method():
    import requests
    import json

    url = 'https://tracking85020.com/api/v2'

    headers = {'Content-type': 'application/json'}

    API_KEY_NETWORK_REPORT = load_config('API_KEY_NETWORK_REPORT_CONVERSIONS')

    params_request_post = {
        'api-key': API_KEY_NETWORK_REPORT,
        'lang': 'en',
        'sortField': 'added_timestamp',
        'sortDirection': 'desc',
        'perPage': 10000,
        'page': 1
    }

    data = {
        "rangeFrom": "2021-10-01",
        "rangeTo": "2021-10-22",
        "columns": "transaction_id,conversion_status,added_timestamp,time_difference,advertiser_id,advertiser,affiliate_id,affiliate,offer_id,offer,goal_id,goal,ip,advertiser_track_id,sub_id1,revenue,payout,profit,currency,click_id,deep_link_url",
        "filters": {
            "statuses": "2"
        }
    }

    response_data_post = requests.post(
        url + '/network/reports/conversions', params=params_request_post, data=json.dumps(data), headers=headers)
    print(response_data_post.elapsed.total_seconds())
    return response_data_post.json()


def format_json(json_thing, ascii=False, sort=True, indents=4):
    import json

    if type(json_thing) is str:
        return (json.dumps(json.loads(json_thing),
                           ensure_ascii=ascii, sort_keys=sort, indent=indents))
    else:
        return (json.dumps(json_thing, ensure_ascii=ascii, sort_keys=sort, indent=indents))


def save_data(data, destination_file='raw.txt', modes='a', obs_to_json_parser=False):
    import os
    import io

    if (os.path.exists(destination_file) == False):
        open(destination_file, 'w').close

    with io.open(destination_file, mode=modes, encoding='utf-8') as fw:
        if (obs_to_json_parser == True):
            fw.write(format_json(data))
        else:
            fw.write(data)


def main():
    data = format_json(post_method(), False, False, 3)
    # print(data)
    save_data(data, file_path)


if __name__ == "__main__":
    file_path = './../data_json.txt'
    main()
