The read also records:

1. The one model credential that enters the runner home (a login file
   or an API-key variable), its scope, and how to revoke it.
2. The exact endpoints the runner reaches, a login-refresh endpoint
   included.
3. That any session-sharing feature is off.
4. That no language server or plugin is downloaded.
5. The installed version, as recorded for each run. Never pin a
   version; host updates stay on.
6. Any UI or socket the runner serves, and its bind: loopback only. Any
   other bind is `security-hardening` Ask first.
7. Where the runner keeps session state: inside the runner home.
8. That no front end needs a login of its own.
9. For a paid key: that the provider-side credit limit is set. That
   limit is the operator's, not this procedure's.

A run finds an installed version that differs from the one the last
read recorded → before the run, recheck and record settings 1–4, 6
and 7. A changed setting is a runner change and needs a new read.
