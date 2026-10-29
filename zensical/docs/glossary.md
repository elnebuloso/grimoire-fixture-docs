# Glossary

The words the platform team uses in its runbooks and channels. A **deploy** puts a new version of
a service into production; a **rollback** returns a service to the version it ran before. The
**on-call engineer** is the person who answers pages for the platform during one week. A
**replica** is one running copy of a service; every platform service runs at least three. The
**service mesh** routes traffic between services and enforces that only services with a valid
token from `auth-service` talk to each other.
