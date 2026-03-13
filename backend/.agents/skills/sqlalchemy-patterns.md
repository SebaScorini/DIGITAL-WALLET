# SQLAlchemy Patterns

Repositories handle database access.

Avoid embedding SQL inside routers or services.

Example repository responsibilities:

- get_user_by_email
- create_user
- get_wallet_by_user_id
- update_wallet_balance
- create_transaction