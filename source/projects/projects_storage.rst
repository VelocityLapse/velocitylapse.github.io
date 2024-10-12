########################
Changing Project Storage
########################

By default, projects will be saved to your device internal storage. If you would like to change this to an external storage location, simply tap the Storage Selector button to bring up a menu to choose between internal and, if an SD card is inserted and mounted, external storage. The Storage Selector button will display how much storage is remaining at the currently set project storage location.

When set to internal storage, projects will be saved to ``/storage/emulated/0/Android/com.velocitylapse.velocitylapse/data/``.

When set to external storage, projects will be saved to ``/storage/<external_storage_name>/Android/com.velocitylapse.velocitylapse/data/``.

.. note::
    Generally, you will not be able to access these directories due to Android security policies so it is best to export your project to an Image Sequence if you want to access the images.