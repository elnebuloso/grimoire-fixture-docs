This page has no title of its own, so grimoire names it after its path. It collects what the
on-call engineer of the billing team needs during a shift, in the order it is usually needed.

## Payment provider down

Check the status page of the provider first, then the error rate of the payment requests in the
dashboard of `billing-api`. If the provider reports an outage, post the link in `#billing` and
wait; the queue in `billing-api` holds the requests. If it does not, open a ticket with the
provider and attach the request IDs of three failed requests from the last hour.

## Billing run failed

A failed billing run is restarted from the beginning with `billing-api run --month <yyyy-mm>`.
The run is idempotent: invoices already created for that month are kept and not created twice, so
a restart is always safe. If the run fails a second time at the same customer, skip that customer
with `--skip <customer-id>` and open a ticket for the billing team.
