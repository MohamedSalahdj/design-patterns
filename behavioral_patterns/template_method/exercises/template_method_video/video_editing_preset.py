from abc import ABC, abstractmethod
from typing import final

from .video import Video

class VideoEditingPreset(ABC):
    @final
    def edit(self, video: Video):
        print(f"\n=== Editing '{video.title}' with {type(self).__name__} ===")
        self._enhance_video_quality(video)
        self._apply_color_correction(video)
        self._enhance_audio_quality(video)
        self._apply_filters(video)
        self._render(video)
        return video

    def _enhance_video_quality(self, video: Video) -> None:
        print("Enhancing video quality (denoise, stabilize)")
        video.applied_steps.append("video_enhanced")

    def _apply_color_correction(self, video: Video) -> None:
        print("Applying color correction")
        video.applied_steps.append("color_default")

    def _enhance_audio_quality(self, video: Video) -> None:
        print("Enhancing audio quality (denoise, normalize)")
        video.applied_steps.append("audio_enhanced")

    def _apply_filters(self, video: Video) -> None:
        print("No filters applied")

    @abstractmethod
    def _render(self, video: Video) -> None:
        ...