# Unshortener Resolver API
Simple FastAPI app to resolve links behind shortened URLs.

**Supported sites**:
- t.co
- tinyurl.com

## Usage
Build and run the Docker container:

```shell
make build
docker -d --name unshortener -p 8000:8000 unshortener-api
```