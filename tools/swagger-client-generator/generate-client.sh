#!/usr/bin/env bash

set -e

DOCKER="${DOCKER:-podman}"
DOCKER_OPTS="${DOCKER_OPTS:- --userns=keep-id:uid=\"$(id -u)\",gid=\"$(id -g)\"}"

echo "DOCKER_OPTS=${DOCKER_OPTS}"

curdir=$(dirname $0)
rootdir=$curdir/../../

base_path=${1:?"Please specify a base path. For example https://your-host/api/cps"}

generator_image="openapitools/openapi-generator-cli:v4.3.1"
generator_image_v2="openapitools/openapi-generator-cli:v7.4.0"

# generator_image="openapitools/openapi-generator-cli:v5.2.1"

function download_swagger {
    swagger_url="${1:?"Please specify the swagger.json path"}"
    file_name="${2:?"Please specify a file name."}"

    echo "Downloading swagger.json from ${swagger_url}"

    curl --fail -k -o "${file_name}" "${swagger_url}"
}

if [[ "${base_path}" == http* ]]; then
    download_swagger "${base_path}/public/v1/swagger.json" "${curdir}/swagger-cps.json"
    download_swagger "${base_path}/public/v2/openapi.json" "${curdir}/openapi-ds-v2.json"
    download_swagger "${base_path}/user/v1/swagger.json" "${curdir}/swagger-user.json"
    download_swagger "${base_path}/kg/v1/swagger.json" "${curdir}/swagger-cps-kg.json"
fi

# Make sure we start with a clean slate.
rm -rf .generated/ || true
mkdir -p .generated/

# echo "Generating client for CPS"

# ${DOCKER} run --rm \
#     -v "$(pwd):/local" \
#     ${DOCKER_OPTS} \
#     ${generator_image} generate \
#         -i "/local/tools/swagger-client-generator/swagger-cps.json" \
#         -g python \
#         -o /local/.generated/cps-public \
#         -c /local/tools/swagger-client-generator/openapi-generator-config-cps.json

# echo "Generating client for the User API"

# ${DOCKER} run --rm \
#     -v "$(pwd):/local" \
#     ${DOCKER_OPTS} \
#     ${generator_image} generate \
#         -i "/local/tools/swagger-client-generator/swagger-user.json" \
#         -g python \
#         -o /local/.generated/cps-user \
#         -c /local/tools/swagger-client-generator/openapi-generator-config-user.json

echo "Generating client for DS API v2"

${DOCKER} run --rm \
    -v "$(pwd):/local" \
    ${DOCKER_OPTS} \
    ${generator_image_v2} generate \
        -i "/local/tools/swagger-client-generator/openapi-ds-v2.json" \
        -g python \
        -o /local/.generated/ds-public-v2 \
        -c /local/tools/swagger-client-generator/openapi-generator-config-ds-v2.json

# echo "Generating client for the CPS KG API"
# echo "Currently disabled: TODO FIX API Specs"

# # ${DOCKER} run --rm \
# #     -v "$(pwd):/local" \
# #     --userns=keep-id:uid="$(id -u)",gid="$(id -g)" \
# #     ${generator_image} generate \
# #         -i "/local/tools/swagger-client-generator/swagger-cps-kg.json" \
# #         -g python \
# #         -o /local \
# #         -c /local/tools/swagger-client-generator/openapi-generator-config-cps-kg.json

# # mkdir -p docs/apis/kg/public && mv docs/*.md docs/apis/kg/public/


# echo "Generating client for the KG Query API"
# echo "Disabled since it generated wrong specs. It won't be updated."

# # ${DOCKER} run --rm \
# #     -v "$(pwd):/local" \
# #     --userns=keep-id:uid="$(id -u)",gid="$(id -g)" \
# #     ${generator_image} generate \
# #         -i "/local/tools/swagger-client-generator/swagger-kg-query.json" \
# #         -g python \
# #         -o /local \
# #         -c /local/tools/swagger-client-generator/openapi-generator-config-kg-query.json

# # mkdir -p docs/apis/kg/query && mv docs/*.md docs/apis/kg/query/

# echo "Generating client for the KG Create API"
# echo "Disabled since it won't be updated."

# # ${DOCKER} run --rm \
# #     -v "$(pwd):/local" \
# #     --userns=keep-id:uid="$(id -u)",gid="$(id -g)" \
# #     ${generator_image} generate \
# #         -i "/local/tools/swagger-client-generator/swagger-kg-create.json" \
# #         -g python \
# #         -o /local \
# #         -c /local/tools/swagger-client-generator/openapi-generator-config-kg-create.json

# # mkdir -p docs/apis/kg/create && mv docs/*.md docs/apis/kg/create/

echo "Merging packages..."

# Remove generated API client code
# rm -rf $rootdir/deepsearch/cps/apis/public || true
# rm -rf $rootdir/deepsearch/cps/apis/user || true
rm -rf $rootdir/deepsearch/cps/apis/public_v2 || true
# rm -rf $rootdir/deepsearch/cps/apis/kg || true

mkdir -p $rootdir/deepsearch/cps/apis
touch $rootdir/deepsearch/cps/apis/__init__.py

# cp -R .generated/cps-public/deepsearch/cps/apis/ $rootdir/deepsearch/cps/apis/
# cp -R .generated/cps-user/deepsearch/cps/apis/ $rootdir/deepsearch/cps/apis/
cp -R .generated/ds-public-v2/deepsearch/cps/apis/ $rootdir/deepsearch/cps/apis/
# cp -R .generated/cps-kg-create/deepsearch/cps/apis/ $rootdir/deepsearch/cps/apis/
# cp -R .generated/cps-kg-query/deepsearch/cps/apis/ $rootdir/deepsearch/cps/apis/

echo "Copying documentation files..."

# Remove generated Documentation code.
rm -rf $rootdir/docs/apis/kg || true
rm -rf $rootdir/docs/apis/public || true
rm -rf $rootdir/docs/apis/user || true
rm -rf $rootdir/docs/apis/public_v2 || true

mkdir -p $rootdir/docs/apis/public
mkdir -p $rootdir/docs/apis/public_v2
mkdir -p $rootdir/docs/apis/user
mkdir -p $rootdir/docs/apis/kg/query
mkdir -p $rootdir/docs/apis/kg/create

# cp -R .generated/cps-public/docs/README.md $rootdir/docs/apis/public/
# cp -R .generated/cps-public/docs $rootdir/docs/apis/public/
# cp -R .generated/cps-user/docs/README.md $rootdir/docs/apis/user/
# cp -R .generated/cps-user/docs $rootdir/docs/apis/user/
cp -R .generated/ds-public-v2/README.md $rootdir/docs/apis/public_v2/
cp -R .generated/ds-public-v2/docs $rootdir/docs/apis/public_v2/
# cp -R .generated/cps-kg-query/docs/README.md $rootdir/docs/apis/kg/create/
# cp -R .generated/cps-kg-query/docs $rootdir/docs/apis/kg/create/
# cp -R .generated/cps-kg-create/docs/README.md $rootdir/docs/apis/kg/query/
# cp -R .generated/cps-kg-create/docs $rootdir/docs/apis/kg/query/

# Delete the staging directory.
rm -rf .generated/
