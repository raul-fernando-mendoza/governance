from metadata.ingestion.ometa.ometa_api import OpenMetadata
from metadata.generated.schema.entity.services.connections.metadata.openMetadataConnection import (
    OpenMetadataConnection, AuthProvider,
)
from metadata.generated.schema.security.client.openMetadataJWTClientConfig import OpenMetadataJWTClientConfig

server_config = OpenMetadataConnection(
    hostPort="http://openmetadata-prd-101:8585/api",
    authProvider=AuthProvider.openmetadata,
    securityConfig=OpenMetadataJWTClientConfig(
        jwtToken="eyJraWQiOiJHYjM4OWEtOWY3Ni1nZGpzLWE5MmotMDI0MmJrOTQzNTYiLCJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJvcGVuLW1ldGFkYXRhLm9yZyIsInN1YiI6ImFkbWluIiwicm9sZXMiOlsiQWRtaW4iXSwiZW1haWwiOiJhZG1pbkBvcGVuLW1ldGFkYXRhLm9yZyIsImlzQm90IjpmYWxzZSwidG9rZW5UeXBlIjoiUEVSU09OQUxfQUNDRVNTIiwiaWF0IjoxNzU2OTQyMjE4LCJleHAiOjE3NjQ3MTgyMTh9.vtoRcoeeL-5xEo61NcUMm-6prej5lFuGrda2uLrBGgOnJ9dGE5ETg9h1fZUT6QMD8xHI0aTGkMHZlxhJorDTNUXyal9JT4t6E8WxBgS2nQU-toABG9kApS_Bew36WJdMhCYYWUFopDoQAljDydIxUl7I4oRN0jyFruQGU_KAdhAuzWGuNrFgGvk-hb0h5SEnsup_vlLxWkFeQqm869G90mptbwatFZuVCTJk_rD9v1xHka-pMMQ7VnuaXA6tmMokzsCrMOMddSyNCmmHNLC0VmJ7p_YJ2ZxuOdZBDpx7EKJ5uJaEi-8ZNgPOK9VeJwKJhEgNRtvFZxs22GTI6QZ2JA",
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

service_entity = metadata.get_by_name(entity=DatabaseService, fqn='DAP', fields=None)

from metadata.generated.schema.api.data.createTable import CreateTableRequest
from metadata.generated.schema.entity.data.table import (
    Column,
    DataType,
    Table
)

from metadata.generated.schema.api.lineage.addLineage import AddLineageRequest
from metadata.generated.schema.type.entityLineage import (
    ColumnLineage,
    EntitiesEdge,
    LineageDetails,
)
from metadata.generated.schema.type.entityReference import EntityReference

allEntities = metadata.list_all_entities( Table)
for table_a_entity in allEntities:
    if not table_a_entity.fullyQualifiedName.root.startswith("DAP"):
        continue
#    print(e)
    print( table_a_entity.fullyQualifiedName.root )

#table_a_entity = metadata.get_by_name(entity=Table, fqn='DAP.DA_PRD_V1.DA_DW.DIM_LEAD', fields=None)

    lineage=metadata.get_lineage_by_id(
        entity = Table,
        entity_id= table_a_entity.id,
        up_depth=  1,
        down_depth= 1
    )
    for downstream in lineage["upstreamEdges"]:
        #print(downstream["fromEntity"])
        fromtable = metadata.get_by_id(entity=Table, entity_id=downstream["fromEntity"], fields=None)
        if fromtable == None:
            continue
        print( "\t" + fromtable.fullyQualifiedName.root + "," + table_a_entity.fullyQualifiedName.root )



print( "done" )
