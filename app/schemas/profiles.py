from pydantic import BaseModel, HttpUrl, validator
from typing import Optional, Dict

class ProfileCreate(BaseModel):
    first_name: str
    last_name: str
    social_links: Optional[Dict[str, str]] = None  # Example: {"github": "https://github.com/user"}
    website_link: Optional[HttpUrl] = None  

    @validator("social_links")
    def validate_social_links(cls, v):
        if v:
            for key, url in v.items():
                if not isinstance(url, str) or not url.startswith("http"):
                    raise ValueError(f"Invalid URL for {key}")
        return v
