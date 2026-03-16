---
title: "Secure by Choice: OAuth2 and JWKS in FHIR Architectures"
date: 2026-03-16T10:08:00+01:00
draft: false
author: "Gjergj Sheldija"
tags: ["FHIR", "Security", "OAuth2", "JWT", "JWKS", "Architecture"]
categories: ["Engineering", "Healthcare"]
description: "Protecting patient data is non-negotiable. Learn how to implement industry-standard Bearer token validation using external Identity Providers."
featured_image: "/images/hapi-fhir.png"
---

# Secure by Choice: OAuth2 and JWKS in FHIR Architectures

In the healthcare world, the security design usually follows a strict pattern: **Identity is external**. Your FHIR server shouldn't be managing passwords. Instead, it should trust an authoritative Identity Provider (IdP) like Keycloak, Auth0, or Okta.

In this tutorial, we’ll explore the **Security Layer** implemented in [hapi-fhir-groovy](https://github.com/gjergjsheldija/hapi-fhir-groovy).

## The Security Flow
1. **User Login**: The client app authenticates with the IdP and receives a **JWT Bearer Token**.
2. **FHIR Request**: The client sends the token in the `Authorization` header to the FHIR server.
3. **Validation**: The FHIR server fetches the public keys (JWKS) from the IdP and verifies the token's signature and expiration.
4. **Access**: If valid, the request proceeds.

## Tutorial: Enabling Security

### Step 1: Configure your Identity Provider
Ensure you have an OpenID Connect (OIDC) realm created. Note down your **JWKS URL** (e.g., `http://keycloak/realms/demo/protocol/openid-connect/certs`).

### Step 2: Update Server Configuration
In your FHIR server’s environment or `application.yaml`, toggle security on:

```yaml
security:
  enabled: true
  server: "http://keycloak/realms/demo"
  jwks: "http://keycloak/realms/demo/protocol/openid-connect/certs"
```

### Step 3: Deployment
When you start the server with `SECURITY_ENABLED=true`, the `SecurityInterceptor` is automatically registered. Any request without a valid token will now return a `401 Unauthorized` status.

## Tutorial: Custom Authentication Logic
What if you need to extract specific claims (like "Clinic ID") from the token and use them as a "Tenant ID" for multi-tenancy? 

Our `AccessTokenValidation` service exposes the JWT claims, making it easy to build custom logic:

```java
@Autowired
private AccessTokenValidation tokenValidator;

// Inside an interceptor
public void handle(HttpServletRequest request) {
    var claims = tokenValidator.getClaimsFromToken(token);
    var clinicId = claims.get("clinic_id");
    // Secure the request context based on clinicId
}
```

## The Architect's Design: SMART on FHIR Scopes
In a real-world ecosystem, security is more than just "logged in". We use **Scopes** to limit what an application can do.
- **`patient/Patient.read`**: Allows the app to read the patient's record but not modify it.
- **`user/Observation.write`**: Allows the practitioner to record new vitals.
- Our `SecurityInterceptor` can be extended via Groovy to inspect these scopes in the JWT and enforce granular access control at the resource level.

## The Architect's Verdict: From Authn to Authz
By using **JWKS (JSON Web Key Sets)**, the FHIR server doesn't need to store any secrets. It simply validates signatures using public keys provided by the IdP. This "Stateless Security" pattern is highly scalable and adheres to SMART on FHIR principles, ensuring your patient data stays safe without adding administrative overhead.

---
*For more, check [`doc/security.md`](https://github.com/gjergjsheldija/hapi-fhir-groovy/blob/main/doc/security.md).*
