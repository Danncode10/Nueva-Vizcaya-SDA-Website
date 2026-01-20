from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://lesterdannlopez@localhost/nv_sda_db"
    cognito_user_pool_id: str = ""
    cognito_client_id: str = ""
    aws_region: str = "ap-southeast-1"
    secret_key: str = "your-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
