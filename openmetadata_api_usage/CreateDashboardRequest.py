from metadata.ingestion.ometa.ometa_api import OpenMetadata
from metadata.generated.schema.entity.services.connections.metadata.openMetadataConnection import (
    OpenMetadataConnection, AuthProvider,
)
from metadata.generated.schema.security.client.openMetadataJWTClientConfig import OpenMetadataJWTClientConfig

server_config = OpenMetadataConnection(
    hostPort="http://openmetadata-prd-101:8585/api",
    authProvider=AuthProvider.openmetadata,
    securityConfig=OpenMetadataJWTClientConfig(
       #jwtToken="eyJraWQiOiJHYjM4OWEtOWY3Ni1nZGpzLWE5MmotMDI0MmJrOTQzNTYiLCJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJvcGVuLW1ldGFkYXRhLm9yZyIsInN1YiI6ImFkbWluIiwicm9sZXMiOlsiQWRtaW4iXSwiZW1haWwiOiJhZG1pbkBvcGVuLW1ldGFkYXRhLm9yZyIsImlzQm90IjpmYWxzZSwidG9rZW5UeXBlIjoiUEVSU09OQUxfQUNDRVNTIiwiaWF0IjoxNzUyMDA1ODE1LCJleHAiOjE3NTk3ODE4MTV9.adVxJuXYRVe5m_CqGZggDEM6Z-Is2ScSzGfSqmW2aJAgDu7mkws338BoxGr_VLCHpPHb8Z3u-f_LbKMmKtNPNaajWaIflCHfkscfo3yZiSs-tYzq3Cnd05d364M9uUejZLU4Pa6TlWDvpIh4qebH1SgJq8ehjAfmxgt6peQJHhKM0rDbrI4gNBT_XDe4TIJWEImBaqjVl_nqZcfot_bn0eIUbVZ-M-UaDP2EQNXtK19PVXEMExVLn_9S52TrmC9y-pgonPPyc2bksBKmV38gOfeQVNNzKUIgTYN5fG6PbcaLop216rlGjBGZlOu7k2Ys6_MVosVBezlcfI1PtdwlcQ",
        jwtToken="eyJraWQiOiJHYjM4OWEtOWY3Ni1nZGpzLWE5MmotMDI0MmJrOTQzNTYiLCJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJvcGVuLW1ldGFkYXRhLm9yZyIsInN1YiI6ImFkbWluIiwicm9sZXMiOlsiQWRtaW4iXSwiZW1haWwiOiJhZG1pbkBvcGVuLW1ldGFkYXRhLm9yZyIsImlzQm90IjpmYWxzZSwidG9rZW5UeXBlIjoiUEVSU09OQUxfQUNDRVNTIiwiaWF0IjoxNzUzMzc2NjY3LCJleHAiOjE3NTU5Njg2Njd9.H0AT9RMxZ9Q0ygdZEE4fglXnaht7jEiTpdmn-Uy3bcoTwbvSZmgP5Xsj9pfNdniynKrzqTq4QWWOWny3EdJYBOGoxdcn3Ai-r10P0O-VxncTBmy5TljHG6y8QTB-oV8L5yx_rBjm5DGeTnyo34ikd4xhpSMmUPo3I1w2RqruOlkon5iqvU9Rz-nLUPHwj2fyWUL4djyeqe50ERnkLTLZWKCT9lAgt2wZBRlzUmI1YZxCtaaW9o3FhG2i-mkOVBmxl5MD5iDU9dYgWdjQ9JMSB6oTlvqacdAIVOW_pHCR0nNVA0Rvd5v6sApacQZl0g9VDqDv1Psi4BLaM28d_DBaNw"
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
