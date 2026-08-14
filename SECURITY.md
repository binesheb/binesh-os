# Security Policy

## Supported versions

Security fixes are applied to the latest release and the active development branch where practical.

## Reporting a vulnerability

Please do not open a public Issue for an undisclosed security vulnerability. Use GitHub's private security reporting mechanism for this repository when available. Include affected version, impact, reproduction details and a suggested mitigation if known.

## Secrets

Never commit passwords, API keys, private certificates, production credentials, device provisioning secrets or OTA signing keys.

Use environment variables, local configuration, a secret manager or device provisioning mechanisms instead.

## Security design principles

- Least privilege.
- Secure defaults.
- Authentication before privileged operations.
- TLS for sensitive network traffic.
- Signed firmware for production OTA.
- Tamper-evident audit records where required.
- No sensitive data in normal logs.
