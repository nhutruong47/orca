# Knowledge Document: SecurityConfig.java (Chunk 3/3)

## Metadata
```json
{
  "file_path": "orca-backend-main/backend/src/main/java/org/example/backend/security/SecurityConfig.java",
  "language": "java",
  "module": "security",
  "business_domain": "factory",
  "tags": [
    "factory",
    "payment",
    "security",
    "authentication"
  ],
  "logical_type": "Generic",
  "chunk_index": 2,
  "total_chunks": 3
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Generic in security.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, payment, security, authentication

## Source Code Chunk
```java
tMatchers("/ws/**").permitAll()
                        .anyRequest().authenticated())
                .oauth2Login(oauth2 -> oauth2
                        .successHandler(oAuth2LoginSuccessHandler))
                .authenticationProvider(authenticationProvider())
                .addFilterBefore(jwtAuthenticationFilter, UsernamePasswordAuthenticationFilter.class);

        return http.build();
    }

    @Bean
    public CorsConfigurationSource corsConfigurationSource() {
        CorsConfiguration configuration = new CorsConfiguration();
        configuration.setAllowedOriginPatterns(
                List.of(
                        "http://localhost:*",
                        "http://127.0.0.1:*",
                        frontendUrl,
                        "https://*.vercel.app",
                        "https://*.ngrok-free.app"));
        configuration.setAllowedMethods(List.of("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"));
        configuration.setAllowedHeaders(List.of("*"));
        configuration.setAllowCredentials(true);
        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/**", configuration);
        return source;
    }
}

```
