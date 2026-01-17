# Security utilities
# For now, this is a placeholder as per requirements "Seguridad básica (placeholder)"
# Even with no auth, headers validation or similar could go here.

from fastapi import Header, HTTPException

async def verify_esp_token(x_esp_token: str = Header(None)):
    """
    Placeholder for ESP32 authentication.
    In a real scenario, compare against a secret token.
    """
    if not x_esp_token:
        # For now, allow open access or just log warning
        pass
    return x_esp_token
