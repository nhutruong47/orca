# Knowledge Document: application.properties (Chunk 1/1)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/test/resources/application.properties",
  "language": "properties",
  "module": "resources",
  "business_domain": "admin",
  "tags": [
    "admin",
    "security"
  ],
  "logical_type": "Generic",
  "chunk_index": 0,
  "total_chunks": 1
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in resources.
- **Dependencies**: Refer to module imports.
- **Tags**: admin, security

## Source Code Chunk
```properties
spring.datasource.url=jdbc:h2:mem:testdb;MODE=MYSQL;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=FALSE
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=

spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.H2Dialect
spring.jpa.show-sql=true

app.jwt.secret=bXlTdXBlclNlY3JldEtleUZvckpXVF9QbGVhc2VDaGFuZ2VJblByb2R1Y3Rpb25fQXRMZWFzdDI1NkJpdHMhIQ==
app.jwt.expiration=86400000

spring.mail.host=smtp.gmail.com
spring.mail.port=587
spring.mail.test-connection=false

spring.security.oauth2.client.registration.google.client-id=test-client-id
spring.security.oauth2.client.registration.google.client-secret=test-client-secret
spring.security.oauth2.client.registration.google.scope=email,profile

# ===== PayOS (test mocks) =====
payos.client-id=test
payos.api-key=test
payos.checksum-key=test

# ===== Default Admin Account (tests) =====
app.default-admin.username=admin
app.default-admin.password=Admin@123
app.default-admin.email=admin@orca.local
app.default-admin.full-name=Administrator

# ===== Mail test profile =====
spring.autoconfigure.exclude=org.springframework.boot.autoconfigure.mail.MailSenderAutoConfiguration,org.springframework.boot.autoconfigure.mail.MailSenderValidatorAutoConfiguration

```
