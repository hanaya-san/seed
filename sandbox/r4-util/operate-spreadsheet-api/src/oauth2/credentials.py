from oauth2client import file, client, tools

_token_path = './config/token.json'
_creds_path = './config/credentials.json'

def get_credentials(scope):
    store = file.Storage(_token_path)
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(
            _creds_path,
            scopes
        )
        creds = tools.run_flow(flow, store)
    return creds
