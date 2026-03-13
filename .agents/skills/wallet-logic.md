# Wallet Business Logic

Deposits:

- amount must be positive
- increase wallet balance
- create transaction

Transfers:

1. validate sender wallet
2. validate receiver wallet
3. validate balance
4. subtract sender balance
5. add receiver balance
6. create transaction

Transfers must run in a database transaction.