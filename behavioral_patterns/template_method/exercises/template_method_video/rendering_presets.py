from .video import Video
from .video_editing_preset import VideoEditingPreset


class FHDPreset(VideoEditingPreset):
    def _render(self, video):
        print("Rendering in FHD (1920x1080, high bitrate)")
        video.resolution = "1920x1080"
        video.applied_steps.append("rendered_fhd")
    

class HDPreset(VideoEditingPreset):
    def _render(self, video: Video) -> None:
        print("Rendering in HD (1280x720, medium bitrate)")
        video.resolution = "1280x720"
        video.applied_steps.append("rendered_hd")


class SDPreset(VideoEditingPreset):
    def _render(self, video: Video) -> None:
        print("Rendering in SD (640x480, low bitrate)")
        video.resolution = "640x480"
        video.applied_steps.append("rendered_sd")