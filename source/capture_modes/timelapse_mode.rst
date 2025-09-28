##############
Timelapse Mode
##############

The Timelapse mode screen allows you to create time-lapses using a set interval to capture images automatically, with manual camera controls, an optional frame limit, delay, and other features. 

Create beautiful time-lapses of subjects like clouds, sunrises, sunsets, city life, studying, art processes, and more. Watch the changes of the world around you over time, condensed into a few seconds through time-lapse photography.


Top Bar
-------

In Timelapse mode, at the bottom of the screen (or at the left side of the screen when in landscape orientation) is the top bar. From left to right (or bottom to top in landscape mode):

Time Delay Before Start
^^^^^^^^^^^^^^^^^^^^^^^

Delay up to 1 minute before actually starting the capture after the capture button is tapped. 

.. hint::
    This is useful for avoiding shakes and bumps of the phone when turning off the screen, etc. immediately after starting the capture.

Display Options
^^^^^^^^^^^^^^^

Switch between 4 different camera grid styles, or turn the grid off.

Toggle showing capture info onscreen even when the capture settings are not shown.

Capture Resolution
^^^^^^^^^^^^^^^^^^

Change the resolution of the captured photos from preset options. If the selected resolution preset is not available on the device, it will automatically drop down to the next highest supported resolution. Max available resolution looks for the highest supported resolution available to third-party devices.

Bottom Bar
----------

In Timelapse mode, at the bottom of the screen (or at the right side of the screen when in landscape orientation) is the bottom bar. 

From left to right (or bottom to top in landscape mode):

Capture Settings Button
^^^^^^^^^^^^^^^^^^^^^^^

Opens the Capture Settings.

Capture Button
^^^^^^^^^^^^^^

Starts the Timelapse capture.

Camera Settings Button
^^^^^^^^^^^^^^^^^^^^^^

Opens the Camera Settings.


Capture Settings
----------------

The Timelapse capture settings control the length and timing of the capture, and the speed and length of the final time-lapse.

Interval
^^^^^^^^

Interval sets how often an image is captured. It controls how fast and how smooth your final time-lapse will be. The proper Interval to set is highly dependent on the subject and the creative effect you are trying to achieve. Experimentation is key. :)

Velocity
^^^^^^^^

Velocity changes the speed of the final time-lapse. This is another way of setting the Interval, which is useful if you have a certain target speed in mind. For example, set Velocity to 30 and a time-lapse interval corresponding to 30 times the speed of normal video with be automatically set.

Frames
^^^^^^

Frames set the limit (total number) of images that will be captured before automatically stopping the capture. If set to infinity, the capture will continue until the stop capture button is tapped.

Duration
^^^^^^^^

Duration sets the capture time, the amount of time to capture before automatically stopping the capture. If set to infinity, the capture will continue until the stop capture button is tapped. This is another way of setting Frames, which is useful if you have a specific amount of time you want the capture to last.

Playback
^^^^^^^^

Playback sets the final playback time of the time-lapse video when exported to video with the current framerate and settings. This is another way of setting Frames, which is useful if you have a specific target final video length in mind.

Schedule
^^^^^^^^

Enabling Schedule will schedule the time-lapse capture for a period of time from Start time to Stop time. This is useful for setting a future time to automatically start and end the capture.


Camera Settings
---------------

.. warning::
    If you see a star (*) beside the shutter/ISO/focus/white balance values, then your device reports that the current lens **does not** support manual camera settings. Velocity Lapse allows you to set them anyway because sometimes the manual camera settings will work despite the device not reporting it. However, please note that in this case there is no guarantee and the controls may not work as expected or at all.

Flip Camera Direction
^^^^^^^^^^^^^^^^^^^^^

Flip the direction of the camera from back to front or vice-versa. The available lenses (see below) will be updated to reflect the current camera direction.

Available Lenses
^^^^^^^^^^^^^^^^

The available lenses for the current camera direction are displayed. Tapping on a lens will switch the current camera preview to that lens. 

.. note::
    If only one lens is displayed, your device may not support other lenses or the device does not give access to other lenses to third-party apps through the standard camera API. You can also try adjusting the camera zoom which will automatically switch between lenses on many devices.

Flashlight
^^^^^^^^^^

Turn on the camera flashlight. If Flashlight Auto Mode is enabled in settings, the flashlight will automatically turn on and off for intervals longer than 2 seconds to save battery.

Zoom
^^^^

Control the current camera zoom.

Focus
^^^^^

Set the camera focus distance manually. A lower focus distance value will focus on close objects (the foreground) and blur the background. Setting a higher focus distance value will focus on objects far away and blur any objects close to the lens.

White Balance
^^^^^^^^^^^^^

Set the camera white balance to auto, to a specific Kelvin scale value manually via a slider, or by selecting one of the white balance presets.

Shutter Speed
^^^^^^^^^^^^^

Set how long the camera lens stays open to gather light into the lens. 

.. hint::
    Please note that shutter speed and ISO will both be set to manual when in manual mode for devices running Android 15 or lower. Starting with Android 16, Velocity Lapse takes advantage of new APIs for shutter and ISO priority modes so that you can set one manually while keeping the other in auto. **(Note: As of 8/21/2025 this feature is not yet available to the public.)**

.. note::
    The shutter speed and ISO ranges are dependent on what your device allows third-party apps to access. This can be very different than what the device native stock camera can access, unfortunately. You can double-check what shutter speed range a particular device allows third-party apps to access by looking at `this device camera database <https://www.camerafv5.com/devices/manufacturers/>`_. 
    
.. note::
    Experimental feature: Velocity Lapse extends the shutter speed range past the normal amounts for certain device models, but again, this still depends on the device.

Following the standard behavior of camera apps, the normal camera preview is limited to 1/5 of a second of shutter speed. This means that when setting shutter speeds longer than 1/5 of a second, it would not be WYSIWYG in the normal preview. 

For this reason, Velocity Lapse has a special preview called the **Long Exposure Preview**. Enabling this preview will enable you to see an accurate, but not real-time, photo preview with the current long-exposure settings.

ISO
^^^

Set the camera ISO, which controls the brightness of the image at the cost of more noise. 

.. hint::
    Please note that shutter speed and ISO will both be set to manual when in manual mode for devices running Android 15 or lower. Starting with Android 16, Velocity Lapse takes advantage of new APIs for shutter and ISO priority modes so that you can set one manually while keeping the other in auto. **(Note: As of 8/21/2025 this feature is not yet available to the public.)**


AE Button
^^^^^^^^^

The AE button toggles between auto and manual exposure.

Exposure Lock
^^^^^^^^^^^^^

When exposure lock is enabled (the lock icon is locked), the exposure will be locked during the capture. This option is only available when in the ISO, SS, or EV tabs.

AF Button
^^^^^^^^^

The AF button toggles between auto and manual focus.

Focus Lock
^^^^^^^^^^

When focus lock is enabled (the lock icon is locked), the focus will be locked during the capture. This option is only available when in the AF (auto focus) tab.

Exposure Value
^^^^^^^^^^^^^^

The EV (exposure value) slider adjusts the camera auto exposure, making the image brighter or darker. Setting this will set the camera back to auto exposure.


Bluetooth/Volume Button Capture
-------------------------------

With Velocity Lapse PRO you can start and stop captures with a Bluetooth remote or your device volume buttons.