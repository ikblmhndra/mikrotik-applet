## Custom Winbox Applet Documentation

  

### Overview

This document provides instructions on creating a custom Winbox applet for JumpServer.

  

### Steps to Deploy the Applet

  

1.  **Download a Winbox**

- Create folder in `C:\Program Files\Winbox`

- Move your `winbox66.exe` to `C:\Program Files\Winbox`

  

1.  **Create Directory Structure**:

- Create a directory for the Winbox applet.

- Inside, create the `main.py`, `icon.png`, `manifest.yml`, and `setup.yml` files.

  

2.  **Upload the Applet to JumpServer**:

- Follow the JumpServer documentation to upload and register the applet.

- Here's the documentation [Jumpeserve Docs](https://docs.jumpserver.org/zh/v4/guide/system/remoteapp/#54-mainpy)

  

3.  **Test the Applet**:

- Ensure the applet works by launching it from the JumpServer interface and verifying it opens Winbox and connects to the specified router.