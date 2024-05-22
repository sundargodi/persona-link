from . import AzureTTSVoiceSettings, TTSBase
from persona_link.persona_provider.models import AudioProviderSettings

def tts_factory(settings: AudioProviderSettings) -> TTSBase:
    """
    Factory method to get the TTS provider
    """
    if isinstance(settings, AzureTTSVoiceSettings):
        from persona_link.tts.azure.azure_tts import AzureTTS
        return AzureTTS()
    else:
        raise ValueError("Invalid TTS provider")