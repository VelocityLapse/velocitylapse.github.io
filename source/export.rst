######
Export
######

Velocity Lapse can export projects to either MP4 video or an image sequence. 

Select either the :guilabel:`MP4 video` or :guilabel:`Image Sequence` option to set the export format.


MP4 Video
---------

MP4 video is a widely used video file format (called a "container"). Velocity Lapse exports ``AVC/H.264``, ``HEVC/H.265``, ``AV1 (AOMedia Video 1)`` or ``APV (Advanced Professional Video)`` MP4 video, depending on which video codec option you set in Settings.

The settings from top to bottom:

Resolution
^^^^^^^^^^

The output resolution of the video. Some options may be disabled if the resolution of the images are not high enough to export at the a certain video resolution. (e.g: If the images are HD, the 4K option will be disabled.) If options are not shown, your device hardware does not support it.

Bitrate
^^^^^^^

Bit-rate controls the quality of the output video. Specifically, it controls the data rate of bits per second. Higher values result in more data per second, but also result in larger video file sizes. The actual bit-rate the selected option in Mbps is shown above the Export video button.

FPS
^^^

FPS refers to "frames per second", meaning how many images will be shown per second of video playback time. This changes the length of the final video. Some devices and resolutions do not support 60fps so the option may be disabled or not shown.

Effect
^^^^^^

Apply an effect to be applied during export. None (the default) doesn't apply any effect. Motion Blur applies a smoothing effect simulating long-exposure blurring. Light Trails applies an effect tracing the lightest points of the images, which is especially useful for creating star trail time-lapses.


Image Sequence
--------------

Velocity Lapse captures JPG and/or RAW (DNG) images on supported devices so you have full control over your project. You can then export the image sequence for use in other applications.

Location
^^^^^^^^

The output location where the JPG and/or RAW (DNG) image sequence will be saved. This can be changed by setting the folder of the :guilabel:`Image Export Save Location` setting.

Frames
^^^^^^

The number of images that will be exported as an image sequence.

Storage Required
^^^^^^^^^^^^^^^^

The amount of storage required to export the project as an image sequence.
