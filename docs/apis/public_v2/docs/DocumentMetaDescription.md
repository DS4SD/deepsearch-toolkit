# DocumentMetaDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | [**Title**](Title.md) |  | [optional] 
**abstract** | [**Abstract**](Abstract.md) |  | [optional] 
**authors** | [**Authors**](Authors.md) |  | [optional] 
**affiliations** | [**Affiliations**](Affiliations.md) |  | [optional] 
**subjects** | [**Subjects**](Subjects.md) |  | [optional] 
**keywords** | [**Keywords**](Keywords.md) |  | [optional] 
**publication_date** | [**PublicationDate**](PublicationDate.md) |  | [optional] 
**languages** | [**Languages**](Languages.md) |  | [optional] 
**license** | [**DocumentDescriptionLicense**](DocumentDescriptionLicense.md) |  | [optional] 
**publishers** | [**Publishers**](Publishers.md) |  | [optional] 
**url_refs** | [**UrlRefs**](UrlRefs.md) |  | [optional] 
**references** | [**References**](References.md) |  | [optional] 
**publication** | [**Publication1**](Publication1.md) |  | [optional] 
**reference_count** | [**ReferenceCount**](ReferenceCount.md) |  | [optional] 
**citation_count** | [**CitationCount**](CitationCount.md) |  | [optional] 
**citation_date** | [**CitationCountDate**](CitationCountDate.md) |  | [optional] 
**advanced** | [**DocumentDescriptionAdvanced**](DocumentDescriptionAdvanced.md) |  | [optional] 
**analytics** | [**DocumentDescriptionAdvanced**](DocumentDescriptionAdvanced.md) |  | [optional] 
**acquisition** | [**DocumentDescriptionAcquisition**](DocumentDescriptionAcquisition.md) |  | [optional] 

## Example

```python
from deepsearch.cps.apis.public_v2.models.document_meta_description import DocumentMetaDescription

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentMetaDescription from a JSON string
document_meta_description_instance = DocumentMetaDescription.from_json(json)
# print the JSON string representation of the object
print(DocumentMetaDescription.to_json())

# convert the object into a dict
document_meta_description_dict = document_meta_description_instance.to_dict()
# create an instance of DocumentMetaDescription from a dict
document_meta_description_form_dict = document_meta_description.from_dict(document_meta_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


