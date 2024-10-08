# ds-public
API for Deep Search.

**WARNING**: This API is subject to change without warning!

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 3.0.0
- Package version: 2.0.0
- Generator version: 7.4.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import deepsearch.cps.apis.public_v2
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import deepsearch.cps.apis.public_v2
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import deepsearch.cps.apis.public_v2
from deepsearch.cps.apis.public_v2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api/cps/public/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = deepsearch.cps.apis.public_v2.Configuration(
    host = "/api/cps/public/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'


# Enter a context with an instance of the API client
with deepsearch.cps.apis.public_v2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = deepsearch.cps.apis.public_v2.ContentManagerApi(api_client)
    index_key = 'index_key_example' # str | 
    proj_key = 'proj_key_example' # str | 
    page = 1 # int |  (optional) (default to 1)
    page_size = 25 # int |  (optional) (default to 25)

    try:
        # Get All Project Data Index Documents
        api_response = api_instance.get_all_project_data_index_documents(index_key, proj_key, page=page, page_size=page_size)
        print("The response of ContentManagerApi->get_all_project_data_index_documents:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentManagerApi->get_all_project_data_index_documents: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to */api/cps/public/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ContentManagerApi* | [**get_all_project_data_index_documents**](docs/ContentManagerApi.md#get_all_project_data_index_documents) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/ | Get All Project Data Index Documents
*ContentManagerApi* | [**get_project_agents**](docs/ContentManagerApi.md#get_project_agents) | **GET** /project/{proj_key}/data_indices/documents/agents | Get Project Agents
*ContentManagerApi* | [**get_project_conversion_statistics**](docs/ContentManagerApi.md#get_project_conversion_statistics) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/statistics | Get Project Conversion Statistics
*ContentManagerApi* | [**get_project_data_index_document_artifacts**](docs/ContentManagerApi.md#get_project_data_index_document_artifacts) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/{document_hash}/artifacts | Get Project Data Index Document Artifacts
*ContentManagerApi* | [**get_project_data_index_document_events**](docs/ContentManagerApi.md#get_project_data_index_document_events) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/{document_hash}/doc_events | Get Project Data Index Document Events
*ContentManagerApi* | [**get_project_data_index_document_markdown**](docs/ContentManagerApi.md#get_project_data_index_document_markdown) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/{document_hash}/Markdown | Get Project Data Index Document Markdown
*ContentManagerApi* | [**get_project_data_index_document_metadata**](docs/ContentManagerApi.md#get_project_data_index_document_metadata) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/{document_hash}/metadata | Get Project Data Index Document Metadata
*ContentManagerApi* | [**get_project_data_index_documents**](docs/ContentManagerApi.md#get_project_data_index_documents) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/agent/{agent_name} | Get Project Data Index Documents
*ContentManagerApi* | [**get_project_data_index_grouped_documents**](docs/ContentManagerApi.md#get_project_data_index_grouped_documents) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/agent/{agent_name}/grouped | Get Project Data Index Grouped Documents
*ContentManagerApi* | [**get_project_data_index_json_document**](docs/ContentManagerApi.md#get_project_data_index_json_document) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/{document_hash}/JSON | Get Project Data Index Json Document
*ContentManagerApi* | [**get_project_data_index_pdf_document**](docs/ContentManagerApi.md#get_project_data_index_pdf_document) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/{document_hash}/PDF | Get Project Data Index Pdf Document
*ContentManagerApi* | [**get_project_documents_by_transaction**](docs/ContentManagerApi.md#get_project_documents_by_transaction) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/transactions/{transaction_id} | Get Project Documents By Transaction
*ContentManagerApi* | [**get_project_index_upload_jobs**](docs/ContentManagerApi.md#get_project_index_upload_jobs) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/upload_jobs | Get Project Index Upload Jobs
*DataIndicesApi* | [**create_project_data_index**](docs/DataIndicesApi.md#create_project_data_index) | **POST** /project/{proj_key}/data_indices | Create Project Data Index
*DataIndicesApi* | [**create_project_data_index_delete_token**](docs/DataIndicesApi.md#create_project_data_index_delete_token) | **POST** /project/{proj_key}/data_indices/{index_key}/delete_token | Create Project Data Index Delete Token
*DataIndicesApi* | [**delete_project_data_index**](docs/DataIndicesApi.md#delete_project_data_index) | **DELETE** /project/{proj_key}/data_indices/{index_key} | Delete Project Data Index
*DataIndicesApi* | [**get_project_data_index**](docs/DataIndicesApi.md#get_project_data_index) | **GET** /project/{proj_key}/data_indices/{index_key} | Get Project Data Index
*DataIndicesApi* | [**get_project_data_indices**](docs/DataIndicesApi.md#get_project_data_indices) | **GET** /project/{proj_key}/data_indices | Get Project Data Indices
*DataIndicesApi* | [**update_project_data_index**](docs/DataIndicesApi.md#update_project_data_index) | **PATCH** /project/{proj_key}/data_indices/{index_key} | Update Project Data Index
*DataIndicesUploadApi* | [**ccs_convert_file_project_data_index**](docs/DataIndicesUploadApi.md#ccs_convert_file_project_data_index) | **POST** /project/{proj_key}/data_indices/{index_key}/actions/ccs_convert | Ccs Convert File Project Data Index
*DataIndicesUploadApi* | [**ccs_convert_upload_file_project_data_index**](docs/DataIndicesUploadApi.md#ccs_convert_upload_file_project_data_index) | **POST** /project/{proj_key}/data_indices/{index_key}/actions/ccs_convert_upload | Ccs Convert Upload File Project Data Index
*DataIndicesUploadApi* | [**get_attachment_upload_data**](docs/DataIndicesUploadApi.md#get_attachment_upload_data) | **GET** /project/{proj_key}/data_indices/{index_key}/documents/{index_item_id}/attachment_url/{filename} | Get Attachment Upload Data
*DataIndicesUploadApi* | [**html_print_convert_upload**](docs/DataIndicesUploadApi.md#html_print_convert_upload) | **POST** /project/{proj_key}/data_indices/{index_key}/actions/html_print_convert_upload | Html Print Convert Upload
*DataIndicesUploadApi* | [**load_project_data_index_files_elastic**](docs/DataIndicesUploadApi.md#load_project_data_index_files_elastic) | **POST** /project/{proj_key}/data_indices/{index_key}/actions/load_elastic | Load Project Data Index Files Elastic
*DataIndicesUploadApi* | [**register_attachment**](docs/DataIndicesUploadApi.md#register_attachment) | **POST** /project/{proj_key}/data_indices/{index_key}/documents/{index_item_id}/attachment | Register Attachment
*DataIndicesUploadApi* | [**upload_project_data_index_file**](docs/DataIndicesUploadApi.md#upload_project_data_index_file) | **POST** /project/{proj_key}/data_indices/{index_key}/actions/upload | Upload Project Data Index File
*DataIndicesUploadApi* | [**upload_register_project_documents**](docs/DataIndicesUploadApi.md#upload_register_project_documents) | **POST** /project/{proj_key}/data_indices/{index_key}/actions/upload_register_documents | Upload Register Project Documents
*KnowledgeGraphsApi* | [**backend_list_project_kgs**](docs/KnowledgeGraphsApi.md#backend_list_project_kgs) | **GET** /backend/project/{proj_key}/bags | Backend List Project Kgs
*KnowledgeGraphsApi* | [**create_project_knowledge_graph**](docs/KnowledgeGraphsApi.md#create_project_knowledge_graph) | **POST** /backend/project/{proj_key}/bags | Create Project Knowledge Graph
*KnowledgeGraphsApi* | [**list_public_knowledge_graphs**](docs/KnowledgeGraphsApi.md#list_public_knowledge_graphs) | **GET** /project/public/bags | List Public Knowledge Graphs
*KnowledgeGraphsApi* | [**update_project_knowledge_graph_metadata**](docs/KnowledgeGraphsApi.md#update_project_knowledge_graph_metadata) | **PATCH** /backend/project/{proj_key}/bags/{bag_key} | Update Project Knowledge Graph Metadata
*ProjectApi* | [**check_wait_ccs_task_task**](docs/ProjectApi.md#check_wait_ccs_task_task) | **GET** /project/{proj_key}/convert_tasks/{task_id} | Check Wait Ccs Task Task
*ProjectApi* | [**convert_pdf_document**](docs/ProjectApi.md#convert_pdf_document) | **POST** /project/{proj_key}/convert | Convert Pdf Document
*ProjectApi* | [**delete_project_integration_config_genai**](docs/ProjectApi.md#delete_project_integration_config_genai) | **DELETE** /project/{proj_key}/integrations/genai | Delete Project Integration Config Genai
*ProjectApi* | [**get_project_default_values**](docs/ProjectApi.md#get_project_default_values) | **GET** /project/{proj_key}/default_values | Get Project Default Values
*ProjectApi* | [**get_project_integration_config_genai**](docs/ProjectApi.md#get_project_integration_config_genai) | **GET** /project/{proj_key}/integrations/genai | Get Project Integration Config Genai
*ProjectApi* | [**provision_project_packages**](docs/ProjectApi.md#provision_project_packages) | **POST** /project/{proj_key}/packages | Provision Project Packages
*ProjectApi* | [**update_project_default_values**](docs/ProjectApi.md#update_project_default_values) | **POST** /project/{proj_key}/default_values | Update Project Default Values
*ProjectApi* | [**update_project_integration_config_genai**](docs/ProjectApi.md#update_project_integration_config_genai) | **POST** /project/{proj_key}/integrations/genai | Update Project Integration Config Genai
*SemanticApi* | [**ingest**](docs/SemanticApi.md#ingest) | **POST** /project/{proj_key}/semantic/ingest | Ingest
*SystemApi* | [**get_system_information**](docs/SystemApi.md#get_system_information) | **GET** /system/info | Get System Information
*SystemApi* | [**get_system_modules_configuration**](docs/SystemApi.md#get_system_modules_configuration) | **GET** /system/modules/configuration | Get System Modules Configuration
*SystemApi* | [**get_system_modules_tasks**](docs/SystemApi.md#get_system_modules_tasks) | **GET** /system/modules/tasks | Get System Modules Tasks
*SystemApi* | [**list_packages**](docs/SystemApi.md#list_packages) | **GET** /system/packages | List Packages
*SystemApi* | [**list_system_knowledge_graphs**](docs/SystemApi.md#list_system_knowledge_graphs) | **GET** /system/kgs | List System Knowledge Graphs
*SystemApi* | [**system_get_all_dcs_admin**](docs/SystemApi.md#system_get_all_dcs_admin) | **GET** /system/admin/get_all_dcs | System Get All Dcs Admin
*SystemApi* | [**system_get_all_kgs_admin**](docs/SystemApi.md#system_get_all_kgs_admin) | **GET** /system/admin/get_all_kgs | System Get All Kgs Admin
*SystemFlavoursApi* | [**delete_flavour**](docs/SystemFlavoursApi.md#delete_flavour) | **DELETE** /system/admin/delete_flavour/{flavour_name} | Delete Flavour
*SystemFlavoursApi* | [**get_flavour**](docs/SystemFlavoursApi.md#get_flavour) | **GET** /system/admin/get_flavour/{flavour_name} | Get Flavour
*SystemFlavoursApi* | [**list_all_flavours**](docs/SystemFlavoursApi.md#list_all_flavours) | **GET** /system/admin/list_all_flavours | List All Flavours
*SystemFlavoursApi* | [**list_flavours_by_project**](docs/SystemFlavoursApi.md#list_flavours_by_project) | **GET** /system/admin/get_project_flavours/{proj_key} | List Flavours By Project
*SystemFlavoursApi* | [**list_projects_flavours**](docs/SystemFlavoursApi.md#list_projects_flavours) | **GET** /system/admin/list_projects_flavours | List Projects Flavours
*SystemFlavoursApi* | [**save_flavour**](docs/SystemFlavoursApi.md#save_flavour) | **PUT** /system/admin/save_flavour | Save Flavour
*SystemFlavoursApi* | [**save_project_flavours**](docs/SystemFlavoursApi.md#save_project_flavours) | **PUT** /system/admin/save_project_flavours | Save Project Flavours
*SystemQuotasApi* | [**get_flavours_default_quotas**](docs/SystemQuotasApi.md#get_flavours_default_quotas) | **GET** /system/admin/get_flavours_default_quota | Get Flavours Default Quotas
*SystemQuotasApi* | [**get_project_flavour_total_kgs**](docs/SystemQuotasApi.md#get_project_flavour_total_kgs) | **GET** /system/admin/get_project_flavour_total_kgs/{proj_key}/{flavour_name} | Get Project Flavour Total Kgs
*SystemQuotasApi* | [**get_project_flavours_quota**](docs/SystemQuotasApi.md#get_project_flavours_quota) | **GET** /system/admin/get_project_flavours_quota/{proj_key} | Get Project Flavours Quota
*SystemQuotasApi* | [**get_projects_flavours_quota**](docs/SystemQuotasApi.md#get_projects_flavours_quota) | **GET** /system/admin/get_projects_flavours_quota | Get Projects Flavours Quota
*SystemQuotasApi* | [**save_flavours_default_quotas**](docs/SystemQuotasApi.md#save_flavours_default_quotas) | **PUT** /system/admin/save_flavours_default_quota | Save Flavours Default Quotas
*SystemQuotasApi* | [**save_project_flavours_quota**](docs/SystemQuotasApi.md#save_project_flavours_quota) | **PUT** /system/admin/save_project_flavours_quota | Save Project Flavours Quota
*SystemSummaryApi* | [**system_get_cps_summary**](docs/SystemSummaryApi.md#system_get_cps_summary) | **GET** /system/admin/summary | System Get Cps Summary
*SystemSummaryApi* | [**system_get_dc_storage_summary_async**](docs/SystemSummaryApi.md#system_get_dc_storage_summary_async) | **GET** /system/admin/dc_storage_summary/{dc_key} | System Get Dc Storage Summary Async
*SystemSummaryApi* | [**system_get_kg_storage_summary_async**](docs/SystemSummaryApi.md#system_get_kg_storage_summary_async) | **GET** /system/admin/kg_storage_summary/{kg_key} | System Get Kg Storage Summary Async
*TasksApi* | [**abort_project_task**](docs/TasksApi.md#abort_project_task) | **POST** /project/{proj_key}/tasks/{task_id}/actions/abort | Abort Project Task
*TasksApi* | [**get_project_celery_task**](docs/TasksApi.md#get_project_celery_task) | **GET** /project/{proj_key}/celery_tasks/{task_id} | Get Project Celery Task
*TasksApi* | [**get_project_task**](docs/TasksApi.md#get_project_task) | **GET** /project/{proj_key}/tasks/{task_id} | Get Project Task
*TasksApi* | [**list_project_tasks**](docs/TasksApi.md#list_project_tasks) | **GET** /project/{proj_key}/tasks | List Project Tasks
*UploadApi* | [**create_project_scratch_file**](docs/UploadApi.md#create_project_scratch_file) | **POST** /project/{proj_key}/scratch/files/upload/{filename} | Create Project Scratch File
*UploadApi* | [**list_project_scratch_files**](docs/UploadApi.md#list_project_scratch_files) | **GET** /project/{proj_key}/scratch/files | List Project Scratch Files
*UploadApi* | [**list_project_scratch_files_paginated**](docs/UploadApi.md#list_project_scratch_files_paginated) | **GET** /project/{proj_key}/scratch/files_paginated | List Project Scratch Files Paginated


## Documentation For Models

 - [AssembleMode](docs/AssembleMode.md)
 - [AssembleSettings](docs/AssembleSettings.md)
 - [AttachmentUploadData](docs/AttachmentUploadData.md)
 - [AttachmentUploadRequestBody](docs/AttachmentUploadRequestBody.md)
 - [BagFlavourFullData](docs/BagFlavourFullData.md)
 - [CCSProject](docs/CCSProject.md)
 - [CPSPackage](docs/CPSPackage.md)
 - [CPSSummary](docs/CPSSummary.md)
 - [CcsTask](docs/CcsTask.md)
 - [CollectionMetadataSettings](docs/CollectionMetadataSettings.md)
 - [Config](docs/Config.md)
 - [ConvertDocumentRequest](docs/ConvertDocumentRequest.md)
 - [ConvertDocumentsRequestBody](docs/ConvertDocumentsRequestBody.md)
 - [ConvertDocumentsSources](docs/ConvertDocumentsSources.md)
 - [ConvertUploadDocumentsRequestBody](docs/ConvertUploadDocumentsRequestBody.md)
 - [CpsTask](docs/CpsTask.md)
 - [Data](docs/Data.md)
 - [DataFlow](docs/DataFlow.md)
 - [DataIndexUploadFileSource](docs/DataIndexUploadFileSource.md)
 - [DefaultValues](docs/DefaultValues.md)
 - [Deployment](docs/Deployment.md)
 - [DirectModelConfig](docs/DirectModelConfig.md)
 - [DocumentArtifacts](docs/DocumentArtifacts.md)
 - [DocumentArtifactsItem](docs/DocumentArtifactsItem.md)
 - [DocumentArtifactsPageItem](docs/DocumentArtifactsPageItem.md)
 - [DocumentStatistics](docs/DocumentStatistics.md)
 - [ElasticIndexPropertyObject](docs/ElasticIndexPropertyObject.md)
 - [ElasticIndexPropertyPrimitive](docs/ElasticIndexPropertyPrimitive.md)
 - [ElasticIndexSearchQueryOptions](docs/ElasticIndexSearchQueryOptions.md)
 - [ElasticIndexSource](docs/ElasticIndexSource.md)
 - [ElasticInstanceDataIndex](docs/ElasticInstanceDataIndex.md)
 - [ElasticMetadata](docs/ElasticMetadata.md)
 - [FileSource](docs/FileSource.md)
 - [Flavour](docs/Flavour.md)
 - [FlavoursDefaultQuota](docs/FlavoursDefaultQuota.md)
 - [FlavoursQuota](docs/FlavoursQuota.md)
 - [GenAIAWSBedrock](docs/GenAIAWSBedrock.md)
 - [GenAIAWSBedrockConfig](docs/GenAIAWSBedrockConfig.md)
 - [GenAIBAM](docs/GenAIBAM.md)
 - [GenAIBAMConfig](docs/GenAIBAMConfig.md)
 - [GenAIHFInferenceApi](docs/GenAIHFInferenceApi.md)
 - [GenAIHFInferenceApiConfig](docs/GenAIHFInferenceApiConfig.md)
 - [GenAIParams](docs/GenAIParams.md)
 - [GenAIPartialParams](docs/GenAIPartialParams.md)
 - [GenAIWatsonx](docs/GenAIWatsonx.md)
 - [GenAIWatsonxConfig](docs/GenAIWatsonxConfig.md)
 - [GroupedProjectDocuments](docs/GroupedProjectDocuments.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [HttpSource](docs/HttpSource.md)
 - [InternalUrl](docs/InternalUrl.md)
 - [JsonUploadRequestBody](docs/JsonUploadRequestBody.md)
 - [ListProjectFlavours](docs/ListProjectFlavours.md)
 - [ModelPipelineSettings](docs/ModelPipelineSettings.md)
 - [ModelPipelineSettingsClustersInner](docs/ModelPipelineSettingsClustersInner.md)
 - [ModulesConfig](docs/ModulesConfig.md)
 - [OcrSettings](docs/OcrSettings.md)
 - [Package](docs/Package.md)
 - [PartialDirectConversionParameters](docs/PartialDirectConversionParameters.md)
 - [ProjectAgent](docs/ProjectAgent.md)
 - [ProjectAgents](docs/ProjectAgents.md)
 - [ProjectDataIndexNonView](docs/ProjectDataIndexNonView.md)
 - [ProjectDataIndexSource](docs/ProjectDataIndexSource.md)
 - [ProjectDataIndexView](docs/ProjectDataIndexView.md)
 - [ProjectDataIndexWithStatus](docs/ProjectDataIndexWithStatus.md)
 - [ProjectDocument](docs/ProjectDocument.md)
 - [ProjectDocumentURL](docs/ProjectDocumentURL.md)
 - [ProjectDocuments](docs/ProjectDocuments.md)
 - [ProjectFlavourTotalKgs](docs/ProjectFlavourTotalKgs.md)
 - [ProjectFlavoursQuota](docs/ProjectFlavoursQuota.md)
 - [ProjectPackageInstalationManifest](docs/ProjectPackageInstalationManifest.md)
 - [ProjectScratchFiles](docs/ProjectScratchFiles.md)
 - [ProjectScratchFilesPaginated](docs/ProjectScratchFilesPaginated.md)
 - [ProjectSourceDataIndex](docs/ProjectSourceDataIndex.md)
 - [ProjectsFlavours](docs/ProjectsFlavours.md)
 - [Properties](docs/Properties.md)
 - [ReferenceToModel](docs/ReferenceToModel.md)
 - [ResponseDocumentArtifacts](docs/ResponseDocumentArtifacts.md)
 - [ResponseGetProjectIntegrationConfigGenai](docs/ResponseGetProjectIntegrationConfigGenai.md)
 - [ResponseGroupedDocuments](docs/ResponseGroupedDocuments.md)
 - [ResponseUploadJobs](docs/ResponseUploadJobs.md)
 - [S3Coordinates](docs/S3Coordinates.md)
 - [S3DocumentSource](docs/S3DocumentSource.md)
 - [SemanticIngestReqParams](docs/SemanticIngestReqParams.md)
 - [SemanticIngestRequest](docs/SemanticIngestRequest.md)
 - [SemanticIngestSourcePrivateDataCollection](docs/SemanticIngestSourcePrivateDataCollection.md)
 - [SemanticIngestSourcePrivateDataDocument](docs/SemanticIngestSourcePrivateDataDocument.md)
 - [SemanticIngestSourcePublicDataDocument](docs/SemanticIngestSourcePublicDataDocument.md)
 - [SemanticIngestSourceUrl](docs/SemanticIngestSourceUrl.md)
 - [Source](docs/Source.md)
 - [Source1](docs/Source1.md)
 - [StorageSummaryTask](docs/StorageSummaryTask.md)
 - [SystemInfo](docs/SystemInfo.md)
 - [TargetConversionParameters](docs/TargetConversionParameters.md)
 - [TaskContext](docs/TaskContext.md)
 - [TaskResult](docs/TaskResult.md)
 - [TemporaryUploadFileResult](docs/TemporaryUploadFileResult.md)
 - [TemporaryUrl](docs/TemporaryUrl.md)
 - [TemporaryUrlFields](docs/TemporaryUrlFields.md)
 - [TokenResponse](docs/TokenResponse.md)
 - [UploadDate](docs/UploadDate.md)
 - [UploadElasticRequestBody](docs/UploadElasticRequestBody.md)
 - [UploadJob](docs/UploadJob.md)
 - [Urls](docs/Urls.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)
 - [ViewOf](docs/ViewOf.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Bearer"></a>
### Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




