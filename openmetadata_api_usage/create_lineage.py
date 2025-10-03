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

service_entity = metadata.get_by_name(entity=DatabaseService, fqn='da_dw', fields=None)

from metadata.generated.schema.api.data.createTable import CreateTableRequest
from metadata.generated.schema.entity.data.table import (
    Column,
    DataType,
    Table,
    Dashboard
)

from metadata.generated.schema.api.lineage.addLineage import AddLineageRequest
from metadata.generated.schema.type.entityLineage import (
    ColumnLineage,
    EntitiesEdge,
    LineageDetails,
)
from metadata.generated.schema.type.entityReference import EntityReference

table_a_entity = metadata.get_by_name(entity=Table, fqn='da_dw.DA_DEV.DA_DW.DIM_LEAD', fields=None)
table_b_entity = metadata.get_by_name(entity=Table, fqn='da_dw.DA_DEV.DA_DW.DIM_CLUB', fields=None)

column_lineage = ColumnLineage(
    fromColumns=["da_dw.DA_DEV.DA_DW.DIM_LEAD.CLUB_ID"],
    toColumn="da_dw.DA_DEV.DA_DW.DIM_CLUB.CLUB_ID"
)

lineage_details = LineageDetails(
    sqlQuery="SELECT * FROM DIM_CLUB",
    columnsLineage=[column_lineage],
)

add_lineage_request = AddLineageRequest(
    edge=EntitiesEdge(
        fromEntity=EntityReference(id=table_a_entity.id, type="table"),
        toEntity=EntityReference(id=table_b_entity.id, type="table"),
        lineageDetails=lineage_details,
    ),
)



created_lineage = metadata.add_lineage(data=add_lineage_request)

print( created_lineage )
