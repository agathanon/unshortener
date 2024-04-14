# Unshorten
Firefox Extension and API server for revealing links behind shortened URLs.

## Usage
In order to deal with CORS, Unshorten must send links to a resolver API. 

```shell
cd server
make build
docker -d --name unshortener -p 8000:8000 unshortener-api
```

Build the extension and import into Firefox. Right click on a link and choose 
"Unshorten Link". The result will be copied to the clipboard.

```shell
cd extension
make zip
```

## Supported Sites
- t.co
- tinyurl.com
