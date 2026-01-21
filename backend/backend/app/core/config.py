from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql://lesterdannlopez@localhost/nv_sda_db"
    cognito_user_pool_id: str = ""
    cognito_client_id: str = ""
    aws_region: str = "ap-southeast-1"
    s3_bucket_name: str = "nv-sda-bucket"
    aws_access_key_id: str = ""
    aws_secret_access_key: str = ""
    secret_key: str = "your-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    frontend_url: str = "http://localhost:3000"
    port: int = 8000
    react_app_api_url: str = "http://localhost:8000"
    react_app_aws_region: str = "ap-southeast-1"
    react_app_cognito_user_pool_id: str = ""
    react_app_cognito_client_id: str = ""

    @property
    def cognito_jwks_url(self) -> str:
        return f"https://cognito-idp.{self.aws_region}.amazonaws.com/{self.cognito_user_pool_id}/.well-known/jwks.json"

    class Config:
        env_file = ".env"

settings = Settings()
