from fastapi import FastAPI
from app.api import routes_auth, routes_predict
from app.core.exceptions import register_exception_handler
from app.middleware.logging_middleware import LoggingMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI('Car Price Prediction API')

# link middleware
app.add_middleware(LoggingMiddleware)

# link endpoints
app.include_router(routes_auth.router, tags=['Auth'])
app.include_router(routes_predict.router, tags=['Prediction'])

# moitoring using Prometheus
Instrumentator().instrument(app).expose(app)

# add exception handler
register_exception_handler(app)

