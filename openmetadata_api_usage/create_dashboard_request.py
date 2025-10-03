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

service_entity = metadata.get_by_name(entity=DashboardService, fqn='ServicePowerBiPerformanceAnalysis', fields=None)

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
