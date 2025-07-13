# RailSathi Django Dockerization Assignment

## Setup Instructions

1. **Clone the repository**
2. **Copy `.env.example` to `.env` and update values if needed**
3. **Build and start containers:**
   ```bash
   docker-compose up --build
   ```
4. **Access the app:**
   - Visit [http://localhost:8000/items/](http://localhost:8000/items/) for the items API
   - Django admin at [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Project Structure

- Django project: `railsathi`
- Main app: `railsathi`
- Dockerfile, docker-compose.yml, .env.example included

## API Usage

- **GET /items/**: Returns a list of items (id, name, description)

## Database

- Uses PostgreSQL (containerized)
- DB settings are loaded from `.env`

## Development Notes

- Code hot-reloading enabled via Docker volume
- Migrations run automatically on container startup

## Assumptions & Design Decisions

- Basic Item model for demonstration
- Environment variables for secrets and DB config
- Admin enabled for easy data management

## Bonus Features

- Ready for Django admin and superuser creation
- Easy extension for more APIs

---

For any issues, check container logs or ensure Docker Desktop is running.
