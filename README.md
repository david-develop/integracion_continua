# Integración Continua

Proyecto de demostración con dos contenedores Docker que se comunican entre sí mediante una red interna de Docker.

---

## Estructura del proyecto

```
integracion_continua/
├── servidor/
│   ├── app.py            # API FastAPI con endpoint /mensaje
│   ├── requirements.txt
│   └── Dockerfile
├── cliente/
│   ├── app.py            # Script que consulta al servidor cada 5 segundos
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml    # Orquesta ambos contenedores
└── README.md
```

---

## Cómo funciona la comunicación

```
┌─────────────────────────────────────────────┐
│              Red Docker: red_app            │
│                                             │
│   ┌─────────────┐       ┌───────────────┐   │
│   │   servidor  │◄──────│    cliente    │   │
│   │ FastAPI+uvi │       │  Python loop  │   │
│   │  puerto 5000│       │               │   │
│   └─────────────┘       └───────────────┘   │
│                                             │
└─────────────────────────────────────────────┘
          │
          │ (también accesible desde tu máquina)
    localhost:5000
```

- Docker Compose crea una **red bridge** llamada `red_app`.
- Dentro de esa red, cada contenedor es accesible por su **nombre de servicio** (`servidor`, `cliente`).
- El cliente llama a `http://servidor:5000/mensaje` — Docker resuelve `servidor` como la IP interna del contenedor del
  servidor.
- El puerto `5000` también queda expuesto en tu máquina local para que puedas probarlo con el navegador.

---

## Requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y en ejecución.

---

## Cómo correr los contenedores

### 1. Construir y levantar ambos contenedores

Desde la raíz del proyecto, ejecuta:

```bash
docker compose up --build
```

- `--build` hace que Docker construya las imágenes desde cero la primera vez (o cuando cambies el código).
- Verás los logs de ambos contenedores en la misma terminal.

### 2. Verificar que funciona

Mientras los contenedores corren, abre otra terminal o tu navegador y visita:

```
http://localhost:5000/mensaje
```

Deberías ver una respuesta JSON como:

```json
{
  "mensaje": "Hola desde el servidor!",
  "hora": "2026-05-24T10:30:00.123456"
}
```

En la terminal donde corre Docker Compose, verás el cliente imprimiendo mensajes cada 5 segundos:

```
cliente  | [Cliente] Iniciando. Consultando al servidor cada 5 segundos...
cliente  | [Cliente] Respuesta recibida: {'mensaje': 'Hola desde el servidor!', 'hora': '...'}
```

### 3. Detener los contenedores

```bash
docker compose down
```

---

## Comandos útiles

| Comando                     | Descripción                                        |
|-----------------------------|----------------------------------------------------|
| `docker compose up --build` | Construye imágenes y levanta los contenedores      |
| `docker compose up -d`      | Levanta en segundo plano (sin ver logs)            |
| `docker compose logs -f`    | Ver logs en tiempo real (si está en segundo plano) |
| `docker compose down`       | Detiene y elimina los contenedores                 |
| `docker compose ps`         | Ver estado de los contenedores                     |
