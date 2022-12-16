# System for remote meter points - Django Framework
## Business logic
,,System for remote meter points" is a software, built on Django and designed for employees in energy sector.
Business clients has a opportunity to use meter device who can measure electricity remotely - connection between meter device and system for monitoring is realize with modem and SIM card.
The software contains information about remote meter points - virtual points, a combination of SIM card, modem and meter device.
One meter point has exatly one modem, one SIM card and one meter device - the relation between each of the components are one-to-one.
The system allows to create, update and delete users and every user have a permission depends on his role:
  - Team Leader - superuser, have full CRUD functionalities
  - Department Employee - staff user, have limited CRUD functionalities - not permission to see ,,Analyses" section and CRUD operations to others tasks
  - Аuditor and Other - have strictly limited functionalities (only read).
### Every CRUD operation on a meter points creates a task - it gives a information why meter device is visited (problem with communication or data), when is visited, who communicate with person in place and what is the result of visitation (failed, successful or in progress).
## Details
The software is based on Django MTV structure + HTML + CSS + JavaScript + Bootstrap + DataTables (responsive design) + Chart.js (free JavaScript library for making HTML-based charts).
 - it has a database
 System for remote meter points supports the following operations:
  - Login page: /
  - Registration: /register
  - Edit profile: /profile/:id/edit/
  - Delete profile: /profile/:id/delete
  - Dashboard: /analyses/dashboard
  - Meter point list: /meter-points
  - Add meter point: /meter-points - with modal dialog
  - Edit meter point: /meter-points/:id/edit
  - Delete meter point: /meter-points/:id/delete
  - Meter device list: /meter-devices
  - Add meter device: /meter-devices - with modal dialog
  - Edit meter device: / meter-device/:id/edit
  - Delete meter device: /meter-device/:id/delete
  - SIM list: /SIM
  - Add SIM: /SIM - with modal dialog
  - Edit SIM: /SIM/:id/edit
  - Delete SIM: /SIM/:id/delete
  - Modem list: /modems
  - Add modem: /modems - with modal dialog
  - Edit modem: /modems.:id/edit
  - Delete modem: /modems/:id/delete
  - Task list: /tasks
  - Edit task: /tasks/:id/edit
  - Delete task: /tasks/:id/delete
  - Analyses: /analyses
 ## Screenshots
![analyses1](https://user-images.githubusercontent.com/59261346/207970981-b64c3ce2-80e1-4326-ab0c-2ce9d4e9b955.png)
![analyses2](https://user-images.githubusercontent.com/59261346/207970983-43c7135f-0447-4039-9387-70e61ab66d81.png)
![analyses3](https://user-images.githubusercontent.com/59261346/207970985-912f846e-d075-420b-90d0-45e9d1412c67.png)
![dashboard](https://user-images.githubusercontent.com/59261346/207970987-df801a1c-f487-4b60-bb5a-6e86be1c3247.png)
![delete-meter-device](https://user-images.githubusercontent.com/59261346/207970990-df5e589b-e5b0-4ca2-a4de-cf68b0ca00b4.png)
![delete-meter-point](https://user-images.githubusercontent.com/59261346/207970994-83e17d6d-cd29-4a5d-ad15-9127ac3e056e.png)
![delete-modem](https://user-images.githubusercontent.com/59261346/207970996-e0655f1b-1e98-4845-86a8-6424eb3d86af.png)
![delete-SIM](https://user-images.githubusercontent.com/59261346/207971000-6ad19020-6aa5-491e-80bc-7e3dd188cf93.png)
![delete-task](https://user-images.githubusercontent.com/59261346/207971003-5ecb051d-6e41-476f-b0dd-dd49891405e6.png)
![details-meter-point](https://user-images.githubusercontent.com/59261346/207971004-7b4dee77-9a76-42d0-abe3-d7f44b8deb8d.png)
![details-task](https://user-images.githubusercontent.com/59261346/207971008-c89e4220-1263-4740-bca9-0c3dbcfb5527.png)
![edit-meter-device](https://user-images.githubusercontent.com/59261346/207971010-57dc6770-2fa3-49fd-b176-67022b61e6cf.png)
![edit-meter-point](https://user-images.githubusercontent.com/59261346/207971013-c396916e-7f08-4a7e-9c16-bb2420560978.png)
![edit-modem](https://user-images.githubusercontent.com/59261346/207971014-f69122ad-edcf-419c-b5a3-f0368c608314.png)
![edit_profile](https://user-images.githubusercontent.com/59261346/207971015-d4b38893-deb9-4dfc-bec9-e38c2e5f8cfd.png)
![edit-SIM](https://user-images.githubusercontent.com/59261346/207971019-518c0b35-90df-4839-ac55-f7918a82f9de.png)
![edit-task](https://user-images.githubusercontent.com/59261346/207971023-f0d8e7c4-8c75-4119-8d14-8b605243d1f2.png)
![login](https://user-images.githubusercontent.com/59261346/207971025-133cf998-4322-474f-a6ce-369941195001.png)
![meter-device-list](https://user-images.githubusercontent.com/59261346/207971029-67e530cb-c525-4aa3-a98a-08dc335b2038.png)
![meter-point-list](https://user-images.githubusercontent.com/59261346/207971033-100b9646-c350-44a5-b99c-05c1cfa70353.png)
![modem-list](https://user-images.githubusercontent.com/59261346/207971038-efcba095-9ee1-4ba1-a215-eedef1d6f026.png)
![register](https://user-images.githubusercontent.com/59261346/207971039-72b07e44-9577-4e97-a2cb-f24663ee8269.png)
![add-meter-device](https://user-images.githubusercontent.com/59261346/207970968-294c2818-8224-433a-b23c-bc7b9b746749.png)
![add-meter-point](https://user-images.githubusercontent.com/59261346/207970975-85cfe1f0-3706-4953-8045-b1abe420f789.png)
![add-modem](https://user-images.githubusercontent.com/59261346/207970979-9f2d223f-7d35-4561-bd0b-ca49db23f89a.png)
![add-SIM](https://user-images.githubusercontent.com/59261346/207970980-5d56dcaa-3cd5-4337-aa22-b08e447bfa31.png)
![task-list](https://user-images.githubusercontent.com/59261346/207971044-55cf676a-9209-4b1b-a97c-37dd4cbed24f.png)
