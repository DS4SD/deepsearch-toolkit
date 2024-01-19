# Swagger client generation

## Usage

**Note:** This requires Podman.

To update the Swagger Client with the new API specifications, run:

```bash
# go to repo root dir
cd $(git rev-parse --show-toplevel)

# generate client
# TODO: set base path as needed, as in "https://your-host/api/cps"
./tools/swagger-client-generator/generate-client.sh <BASE_PATH>
```

If you don't want to download the Swagger Specification, and just want to use the local files in `tools/swagger-client-generator`, run:

```bash
./tools/swagger-client-generator/generate-client.sh .
```
