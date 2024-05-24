from persona_link.persona_provider.models import VideoProviderSettings
from typing import Optional
from pydantic import ValidationError
    
class HeygenAvatarSettings(VideoProviderSettings):
    heygen_id: str
    avatar_style: str
    voice_id: str
    background_color: Optional[str] = None
    background_type: str = "color"
    background_asset_id: Optional[str] = None
    test: bool = True
    api_token: str
    
    @classmethod
    def validate(cls, settings: dict) -> Optional['HeygenAvatarSettings']:
        try:
            return cls(**settings)  # Attempts to parse and validate the passed in settings
        except ValidationError as e:
            return None
        
    
    

    # @model_validator(mode="after")
    # def validate_background_settings(cls, values):
    #     background_color, background_type, background_asset_id = values.get('background_color'), values.get('background_type'), values.get('background_asset_id')
    #     if background_type == "color" and not background_color:
    #         raise ValueError('background_color must be provided for color background type')
    #     if (background_type == "image" or background_type == "video") and not background_asset_id:
    #         raise ValueError('background_asset_id must be provided for asset background type')
    #     if background_type not in ["color", "image", "video"]:
    #         raise ValueError('background_type must be one of color, image or video')
        
    #     avatar_style = values.get('avatar_style')
    #     if avatar_style not in ["normal", "circle", "closeUp"]:
    #         raise ValueError('avatar_style must be one of normal, circle or closeUp')
    #     return values
