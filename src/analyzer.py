from typing import Optional


def get_timestamps(media_model, is_audio_only: bool, media_file, language: str) -> str:
    prompt = f"""Act as an expert YouTube content creator. Provide timestamps for the most important moments of the video. 
    Use few words to describe each timestamp. 
    Do not mention the creator; speak in the first person. 
    Provide a maximum of 10 timestamps, excluding the introduction and conclusion. 
    Respond in {language}.
    Response format: [minute] Description.
    
    Example:
    MARCAS DE TIEMPO: 
    0:00 Intro
    2:45 Benchmark
    3:39 RT-EDTR tutorial
    10:45 Inferencia en un video
    13:24 Detección en tiempo real con camara
    16:17 Conclusión
    """
    if media_file:
        response = media_model.generate_content([prompt, media_file])
    else:
        response = media_model.generate_content(prompt)
    return response.text

def get_seo_info(media_model, is_audio_only: bool, media_file, language: str) -> str:
    prompt = f"""Act as an expert YouTube content creator and SEO specialist. 
    Provide 5 different optimized options of title for YouTube and a description based on the content of the video. 
    Additionally, provide tags for YouTube. 
    Respond in {language}."""
    if media_file:
        response = media_model.generate_content([prompt, media_file])
    else:
        response = media_model.generate_content(prompt)
    return response.text

def get_social_media_post(media_model, is_audio_only: bool, media_file, language: str) -> str:
    prompt = f"""Create a social media promotional post for the video optimized for Twitter and LinkedIn.
    Respond in {language}."""
    if media_file:
        response = media_model.generate_content([prompt, media_file])
    else:
        response = media_model.generate_content(prompt)
    return response.text