from trading212_api_client.paths.api_v0_equity_pies_id.get import ApiForget
from trading212_api_client.paths.api_v0_equity_pies_id.post import ApiForpost
from trading212_api_client.paths.api_v0_equity_pies_id.delete import ApiFordelete


class ApiV0EquityPiesId(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
