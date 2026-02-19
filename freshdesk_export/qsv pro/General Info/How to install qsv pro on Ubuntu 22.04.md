---
title: "How to install qsv pro on Ubuntu 22.04"
tags: []
created_at: 2024-09-08T20:39:14Z
updated_at: 2024-09-08T20:50:51Z
---

# How to install qsv pro on Ubuntu 22.04

1. Navigate to [qsvpro.dathere.com](https://qsvpro.dathere.com) in your web browser.

![](images/KJUWJFOoznTxzIxoF7oMr-la0OOuee2bDQ.PNG)

2. Click on the **Linux (AppImage)** button to begin downloading the qsv pro AppImage file.

![](images/nJOyM7lsTUlmkvNqvw95Vlq-4mbur6IA0g.png)

3. Open the folder in your file explorer to where the AppImage is located. By default this should be in **~/Downloads**. Your version of qsv pro may be different.

![](images/kT3GbIVd2rt3KSV9ru6ATnfE0hlmWoJTyg.PNG)

4. Right click the AppImage file and click **Properties**.

![](images/zeT_r9He1_zCsRgVDtrFrJZiwviOiE2y4Q.png)

5. Navigate to the **Permissions tab** and click the **Execute** checkbox where it states **Allow executing file as program** to make sure that execution is enabled as indicated by the checkmark.

![](images/fyP0d1EIus4rAecywJqXzBlNxc13614LmQ.png)

6. Double left click the AppImage file and qsv pro should now launch.

![](images/IZh4QUvCbD4FNhYtieul0W8yC5R-UfiPwQ.png)

Note: If your app isn't launching you might not have FUSE 2 installed (which may be required for running an AppImage). [Click here](https://github.com/AppImage/AppImageKit/wiki/FUSE) to follow the instructions for installing FUSE 2 then rerun the AppImage once you've installed FUSE 2.