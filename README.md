# Onion index
Use elasticsearch to index content and filter specific .onion sites.

## Installation
Please install elastic search from the official repository thanks to the [official guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-repositories.html)


## Init mappings
Please do this when running for the first time

```sh
$ curl -XPUT -i "localhost:9200/crawl/" -d "@./mappings.json"
```
