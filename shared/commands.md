# Common platform commands, one per line; pages include lines 3 to 5.

platformctl status --all
platformctl deploy --service auth-service --version latest
platformctl rollback --service auth-service --to previous
platformctl logs --service auth-service --since 15m
