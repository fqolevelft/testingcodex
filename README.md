# Admin Dashboard Example

This repository contains a minimal skeleton of a FastAPI backend with an
Nginx front-end serving static pages. It demonstrates how a super admin can
create admins and how admins can manage companies.

## Development

Build and run the services with docker-compose:

```bash
docker-compose up --build
```

The web interface is served on `http://localhost` and the API is available
under `/api`.
