## Build environment

```json sdlc-env
{
  "schemaVersion": 1,
  "toolchain": [
    "node --version"
  ],
  "deps": [
    {
      "name": "postgres",
      "setup": [
        "docker pull postgres@sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
      ],
      "start": [
        "docker run -d --name sdlc-pg postgres@sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
      ],
      "ready": [
        "docker exec sdlc-pg pg_isready"
      ],
      "reset": [],
      "stop": [
        "docker rm -f sdlc-pg"
      ]
    }
  ],
  "passEnv": [
    "AD_BIND_DN"
  ],
  "prove": [],
  "test": "npm test"
}
```
