# Custom Credential Types

## Azure

Input configuration

```yaml
fields:
  - id: AZURE_RESOURCE_GROUP
    type: string
    label: AZURE_RESOURCE_GROUP
  - id: AZURE_SUBSCRIPTION_ID
    type: string
    label: AZURE_SUBSCRIPTION_ID
    secret: true
  - id: AZURE_CLIENT_ID
    type: string
    label: AZURE_CLIENT_ID
    secret: true
  - id: AZURE_CLIENT_SECRET
    type: string
    label: AZURE_CLIENT_SECRET
    secret: true
  - id: AZURE_TENANT_ID
    type: string
    label: AZURE_TENANT_ID
    secret: true
```

Injector configuration

```yaml
env:
  AZURE_CLIENT_ID: '{{ AZURE_CLIENT_ID }}'
  AZURE_TENANT_ID: '{{ AZURE_TENANT_ID }}'
  AZURE_CLIENT_SECRET: '{{ AZURE_CLIENT_SECRET }}'
  AZURE_RESOURCE_GROUP: '{{ AZURE_RESOURCE_GROUP }}'
  AZURE_SUBSCRIPTION_ID: '{{ AZURE_SUBSCRIPTION_ID }}'
```
