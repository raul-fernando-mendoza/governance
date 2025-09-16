from metadata.ingestion.ometa.ometa_api import OpenMetadata
from metadata.generated.schema.entity.services.connections.metadata.openMetadataConnection import (
    OpenMetadataConnection, AuthProvider,
)
from metadata.generated.schema.security.client.openMetadataJWTClientConfig import OpenMetadataJWTClientConfig


server_config = OpenMetadataConnection(
    hostPort="http://openmetadata-prd-101:8585/api",
    authProvider=AuthProvider.openmetadata,
    securityConfig=OpenMetadataJWTClientConfig(
        jwtToken="eyJraWQiOiJHYjM4OWEtOWY3Ni1nZGpzLWE5MmotMDI0MmJrOTQzNTYiLCJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJvcGVuLW1ldGFkYXRhLm9yZyIsInN1YiI6ImFkbWluIiwicm9sZXMiOlsiQWRtaW4iXSwiZW1haWwiOiJhZG1pbkBvcGVuLW1ldGFkYXRhLm9yZyIsImlzQm90IjpmYWxzZSwidG9rZW5UeXBlIjoiUEVSU09OQUxfQUNDRVNTIiwiaWF0IjoxNzU3OTY3Mjc2LCJleHAiOjE3NjU3NDMyNzZ9.KwWeKEUZ5lBkZZQtt1hVxRbLFnXPdsQAcsYfFztJt8ufJDgf5jMTHi7z_bp-U2PuwKtXmyQnoDA-addgC-8vohu6QCroWDvMkDSGl8Sds8qyi3cxFknuVd4MP1Q6aNYJpNNkgO33-Vy9t0WrR5IDqWUlaGDEFL9fVVqB9TAKl--pMZIxCP2ke_J9MXOZvsVamsXs1BCNQe2OAuZl3ggnjRZHVVGT7I7aXdgg1r95T8owCCF8b1IlHp5gr7Fkplze8Rh6ij9JuG9jzk0n_uoigy2ME3LRJc9DcsG067pJmMPCwTJ82ydbp15qivXvYgX_xencEWMlful_LIkXTQhOHg",
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
    DatabaseConnection
)
from metadata.generated.schema.entity.services.connections.database.common.basicAuth import (
    BasicAuth,
)
from metadata.generated.schema.entity.services.connections.database.snowflakeConnection import (
    SnowflakeConnection,
)

from metadata.generated.schema.entity.services.dashboardService import DashboardService


service_entity = metadata.get_by_name(entity=DashboardService, fqn='DAP_PowerBI', fields=None)

from metadata.generated.schema.api.data.createTable import CreateTableRequest
from metadata.generated.schema.entity.data.table import (
    Column,
    DataType,
    Table
)

from metadata.generated.schema.entity.data.dashboardDataModel import DataModelType 
from metadata.generated.schema.api.lineage.addLineage import AddLineageRequest
from metadata.generated.schema.type.entityLineage import (
    ColumnLineage,
    EntitiesEdge,
    LineageDetails,
)
from metadata.generated.schema.entity.data.dashboard import Dashboard



#from metadata.ingestion.source.dashboard.powerbi import PowerbiSource
import json

allEntities = metadata.list_entities(Dashboard, limit=10000)


for e in allEntities:
    dashboards = e[1]
    if type(e[1]) is list:
        with open('output.json', 'w') as f:
            for d in e[1]:
                if d.project == "Field Operations V1":
                    f.write(f"{d.fullyQualifiedName.root } - {d.displayName} - {d.project}\n")
                    
                else:
                    byid = metadata.get_by_id(Dashboard, d.id)
                    if byid != None:
                        print(f"{byid.fullyQualifiedName.root } - {byid.displayName} - {byid.project}\n")
                        metadata.delete(Dashboard, d.id, hard_delete=True)

#DashboardDataModel
from metadata.generated.schema.entity.data.dashboardDataModel import DashboardDataModel
allDashboardDataModel = metadata.list_entities(DashboardDataModel, limit=10000)
for e in allDashboardDataModel:
    dashboardsDataModel = e[1]
    if type(dashboardsDataModel) is list:
        with open('output.json', 'w') as f:
            for d in dashboardsDataModel:
                if d.project == "Field Operations V1":
                    f.write(f"{d.fullyQualifiedName.root } - {d.displayName} - {d.project}\n")
                    
                else:
                    byid = metadata.get_by_id(DashboardDataModel, d.id)
                    if byid != None:
                        print(f"{byid.fullyQualifiedName.root } - {byid.displayName} - {byid.project}\n")
                        metadata.delete(DashboardDataModel, d.id, hard_delete=True)


print("end")
 