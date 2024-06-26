from pydantic import BaseModel, ValidationError
from persona_link.persona_provider.models import VideoFormat, VideoCodecs
from enum import Enum
from typing import Optional
class AzureAvatarStyle(Enum):
    """
    Enum for the style of the Azure Avatar
    
    Attributes:
        GRACEFUL : str
            Graceful style
        CASUAL : str
            Casual style
        TECHNICAL : str
            Technical style
    """
    GRACEFUL = "graceful"
    CASUAL = "casual"
    TECHNICAL = "technical"


class AzureAvatarPose(Enum):
    """
    Enum for the pose of the Azure Avatar
    
    Attributes:
        SITTING : str
            Sitting pose
        STANDING : str
            Standing pose
    """
    SITTING = "sitting"
    STANDING = "standing"


class AzureAvatarSettings(BaseModel):
    """
    Settings for Azure Avatar Provider. Refer to [azure](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/text-to-speech-avatar/what-is-text-to-speech-avatar) for more information.
    
    Attributes:
        voice : str
            Voice of the Avatar.
        character : str
            Character of the Avatar.
        style : AzureAvatarStyle
            Style of the Avatar.
        pose : AzureAvatarPose
            Pose of the Avatar.
        video_format : VideoFormat
            Format of the video.
        background_color : str
            Color of the background.
        video_codec : VideoCodecs
            Codec of the video.
    """
    voice: str = "en-IN-NeerjaNeural"
    character: str = "lisa"
    style: AzureAvatarStyle = AzureAvatarStyle.GRACEFUL
    pose: AzureAvatarPose = AzureAvatarPose.SITTING
    video_format: VideoFormat = VideoFormat.WEBM
    background_color: str = "#00000000"
    video_codec:VideoCodecs = VideoCodecs.VP9
    
    @classmethod
    def validate(cls, settings: dict) -> Optional['AzureAvatarSettings']:
        """
        Validates the settings passed in
        
        Parameters:
            settings (dict): The settings to validate
        Returns:
            Validated azure avatar settings or None if validation fails
        """
        try:
            return cls(**settings)  # Attempts to parse and validate the passed in settings
        except ValidationError as e:
            return None