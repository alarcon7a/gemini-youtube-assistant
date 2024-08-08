import google.generativeai as genai
import time
from typing import Tuple, Optional
import constants


def configure_genai(api_key: str) -> None:
    genai.configure(api_key=api_key)

def process_media(file_path: str, model_name: str, is_audio_only: bool):
    print(f"Uploading file...")
    media_file = genai.upload_file(path=file_path)
    print(f"Completed upload: {media_file.uri}")

    while media_file.state.name == "PROCESSING":
        print('.', end='')
        time.sleep(10)
        media_file = genai.get_file(media_file.name)

    if media_file.state.name == "FAILED":
        raise ValueError(media_file.state.name)

    print(f"Retrieved file '{media_file.display_name}' as: {media_file.uri}")

    model = genai.GenerativeModel(model_name=model_name)

    system_instruction = constants.SYSTEM_INSTRUCTION_BASE
    if is_audio_only:
        system_instruction = constants.SYSTEM_INSTRUCTION_AUDIO

    total_tokens = model.count_tokens(media_file).total_tokens

    if total_tokens > constants.MAX_TOKENS:
        print(f"Total tokens: {total_tokens}. Using cached content instead...")
        cache = genai.caching.CachedContent.create(
            model=model_name+"-001",
            system_instruction=system_instruction,
            contents=[media_file],
        )
        media_model = genai.GenerativeModel.from_cached_content(cached_content=cache)
        type_model = 'cache_model'
        media_file = None
    else:
        print(f"Total tokens: {total_tokens}. Generating content...")
        media_model = model
        type_model = 'generated_model'

    return media_model, type_model, media_file