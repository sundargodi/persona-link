from persona_link.persona_provider.base import AvatarType, PersonaBase
from persona_link.cache.models import ContentType, DataToStore, Metadata
from persona_link.persona_provider.models import AudioInstance, AudioProviderSettings
from persona_link.tts import tts_factory
from persona_link.persona_provider import persona_link_provider
@persona_link_provider
class SpriteAvatar(PersonaBase):
    """
    Sprite Avatar takes a series of images as a sprite image where each sub image in the reel represent a visual
    lip position as illustrated [here](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-speech-synthesis-viseme?tabs=visemeid&pivots=programming-language-python#map-phonemes-to-visemes)
    
    The provider will generate the audio and the visemes for the avatar such that the frontend can play the audio and 
    animate the avatar based on the visemes.
    """
    name = "Sprite"
    description = "Sprite Avatar"
    
    @classmethod
    def validate(cls, settings: dict) -> AudioProviderSettings:
        """
        Validate the settings for the provider. This method should return the settings object if the settings are valid
        
        Parameters:
            settings (dict): The settings for the provider
                
        Returns:
            audio provider settings if the settings are valid otherwise None
        """
        return AudioProviderSettings.get_provider(settings)
    
    
        
    async def generate(self, text: str, settings: AudioProviderSettings) -> DataToStore:
        """
        Generate the audio and visemes for the sprite avatar
        
        Parameters:
            text (str): The text to be spoken by the avatar
            settings (AudioProviderSettings): The settings for the provider
                
        Returns:
            the data to store for the audio, visemes and/or word timestamps along with other metadata
        """
        
        audio: AudioInstance = await tts_factory(settings).synthesize_speech(text, settings=settings)
        
        return DataToStore(
            binary_data=audio.content,
            content_type=ContentType.MP3,
            data_type=AvatarType.AUDIO,
            visemes=audio.visemes,
            word_timestamps=audio.word_timestamps,
            metadata = Metadata(
                bit_rate_kbp = settings.bit_rate_kbps,
                sampling_rate_hz = settings.sampling_rate_hz,
                duration_seconds = audio.duration_seconds
            )
        )
        

        