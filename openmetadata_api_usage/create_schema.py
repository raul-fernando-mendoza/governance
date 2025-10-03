from metadata.ingestion.ometa.ometa_api import OpenMetadata
from metadata.generated.schema.entity.services.connections.metadata.openMetadataConnection import (
    OpenMetadataConnection, AuthProvider,
)
from metadata.generated.schema.security.client.openMetadataJWTClientConfig import OpenMetadataJWTClientConfig

server_config = OpenMetadataConnection(
    hostPort="http://192.168.1.5:8585/api",
    authProvider=AuthProvider.openmetadata,
    securityConfig=OpenMetadataJWTClientConfig(
        jwtToken="",
    ),
)
metadata = OpenMetadata(server_config)

print(metadata)

from metadata.generated.schema.api.services.createDatabaseService import (
    CreateDatabaseServiceRequest,
)
from metadata.generated.schema.entity.services.databaseService import (
    DatabaseService,
    DatabaseServiceType,
    DatabaseConnection,
)
from metadata.generated.schema.entity.services.connections.database.common.basicAuth import (
    BasicAuth,
)
from metadata.generated.schema.entity.services.connections.database.snowflakeConnection import (
    SnowflakeConnection,
)

create_service = CreateDatabaseServiceRequest(
    name="da_dw",
    serviceType=DatabaseServiceType.Snowflake,
    connection=DatabaseConnection(
        config=SnowflakeConnection(
            username="DA_DBT_DEV_SVC",
            password="password",
            account="http://localhost:1234",
            warehouse="dw",
        )
    ),
)

from metadata.generated.schema.api.data.createDatabaseSchema import (
    CreateDatabaseSchemaRequest,
)

service_entity = metadata.create_or_update(data=create_service)
print( service_entity )

create_schema = CreateDatabaseSchemaRequest(
    name="DA_RAW_HASH", database="da_dw.DA_DEV"
)

schema_entity = metadata.create_or_update(data=create_schema)

print(schema_entity)