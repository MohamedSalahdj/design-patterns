from .video import Video
from .rendering_presets import FHDPreset


class CinematicFHDPreset(FHDPreset):
    def _apply_color_correction(self, video: Video) -> None:
        print("Applying cinematic color grading (teal & orange)")
        video.applied_steps.append("color_cinematic")

    def _apply_filters(self, video: Video) -> None:
        print("Applying filters: film grain, letterbox")
        video.applied_steps.extend(["film_grain", "letterbox"])