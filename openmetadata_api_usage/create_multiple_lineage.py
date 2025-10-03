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
    Table
)

from metadata.generated.schema.api.lineage.addLineage import AddLineageRequest
from metadata.generated.schema.type.entityLineage import (
    ColumnLineage,
    EntitiesEdge,
    LineageDetails,
)
from metadata.generated.schema.type.entityReference import EntityReference

def add_lineage( fromTable, toTable ):
    fromTable = fromTable.upper()
    toTable = toTable.upper()

    if fromTable.startswith(tuple(["Z_","PS_","FF_","CIAM_","MI9_","TFGO_","CRM_"])):
        fromTableQualified = 'da_dw.DA_DEV.DA_RAW_HASH.' + fromTable.upper()
    elif fromTable.endswith("_VW"):    
        fromTableQualified = 'da_dw.DA_DEV.DA_SMT.' + fromTable.upper()        
    else:
        fromTableQualified = 'da_dw.DA_DEV.DA_DW.' + fromTable.upper()

    if toTable.endswith("_VW"):    
        toTableQualified = 'da_dw.DA_DEV.DA_SMT.' + toTable.upper()
    else:
        toTableQualified = 'da_dw.DA_DEV.DA_DW.' + toTable.upper()

    table_a_entity = metadata.get_by_name(entity=Table, fqn=fromTableQualified, fields=None)

    if not table_a_entity:
        print("not found:" + fromTableQualified)
        return
        

    table_b_entity = metadata.get_by_name(entity=Table, fqn=toTableQualified, fields=None)

    if not table_b_entity:
        print("not found:" + toTableQualified)
        return
        
    
    

    add_lineage_request = AddLineageRequest(
        edge=EntitiesEdge(
            fromEntity=EntityReference(id=table_a_entity.id, type="table"),
            toEntity=EntityReference(id=table_b_entity.id, type="table")
        ),
    )
    
    created_lineage = metadata.add_lineage(data=add_lineage_request)
    print( fromTableQualified + " to " + toTableQualified + " completed" )


#add_lineage('z_debitmemo','fact_debit_memo_month')
    

