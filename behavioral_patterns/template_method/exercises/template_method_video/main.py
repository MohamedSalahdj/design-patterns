from .video import Video
from .rendering_presets import FHDPreset, HDPreset, SDPreset
from .custom_presets import CinematicFHDPreset


if __name__ == "__main__":
    presets = [FHDPreset(), HDPreset(), SDPreset(), CinematicFHDPreset()]

    for preset in presets:
        video = preset.edit(Video(title="Trip to Dahab"))
        print(f"Result: {video.resolution} | steps: {video.applied_steps}")