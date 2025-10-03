from metadata.ingestion.ometa.ometa_api import OpenMetadata
from metadata.generated.schema.entity.services.connections.metadata.openMetadataConnection import (
    OpenMetadataConnection, AuthProvider,
)
from metadata.generated.schema.security.client.openMetadataJWTClientConfig import OpenMetadataJWTClientConfig

server_config = OpenMetadataConnection(
    hostPort="http://openmetadata-prd-101:8585/api",
    authProvider=AuthProvider.openmetadata,
    securityConfig=OpenMetadataJWTClientConfig(
       #jwtToken="",
        jwtToken=""
    ),
)
metadata = OpenMetadata(server_config)

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

from metadata.generated.schema.entity.services.dashboardService import (
    DashboardService,
)
from metadata.generated.schema.api.data.createDashboard import CreateDashboardRequest

from metadata.generated.schema.entity.data.dashboard import Dashboard

allEntities = metadata.list_entities(Dashboard, limit=10000)


for e in allEntities:
    dashboards = e[1]
    if type(e[1]) is list:
        with open('output.json', 'w') as f:
            for d in e[1]:
                if d.project == "Field Operations V1":
                    f.write(f"{d.id} {d.fullyQualifiedName.root } - {d.displayName} - {d.project}\n")
                    
                else:
                    byid = metadata.get_by_id(Dashboard, d.id)
                    if byid != None:
                        print(f"{byid.fullyQualifiedName.root } - {byid.displayName} - {byid.project}\n")
                        metadata.delete(Dashboard, d.id, hard_delete=True)
#use the id inside the UUID from the previous 
d = metadata.get_by_id(Dashboard, 'eb6cc899-0b6e-422c-bba3-e051d620b1aa')

print(d)
"""
dashboard_request = CreateDashboardRequest(
                        name="Performance_Analysis_V1",
                        displayName="Performance Analysis V1",
                        description="This is the first try",
                        project="24HR",
                        charts=[],
                        dataModels=[],
                        tags=[],
                        sourceUrl='https://app.powerbi.com/groups/04fda0cd-b7ba-4df1-8359-57b65cbc6adb/reports/e99b8956-3148-48b4-9478-5677859df7be/ReportSectiona56e9bcf70bbe708d71a?redirectedFromSignup=1&experience=power-bi',
                        service="ServicePowerBiPerformanceAnalysis",
                    )

dashboar_entity = metadata.create_or_update(data=dashboard_request)

print( dashboar_entity )
"""
