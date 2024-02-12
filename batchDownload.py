'''
    ---------------------------------------------------------------------------
    OpenCap processing: batchDownload.py
    ---------------------------------------------------------------------------

    Copyright 2022 Stanford University and the Authors
    
    Author(s): Antoine Falisse, Scott Uhlrich
    
    Licensed under the Apache License, Version 2.0 (the "License"); you may not
    use this file except in compliance with the License. You may obtain a copy
    of the License at http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''

from utils import download_session
import os

#os.getcwd()

# List of sessions you'd like to download. They go to the Data folder in the 
# current directory.
sessionList = ['3bbb6d25-c405-4bc8-bec8-135706916abd',
               '3f93b027-db2e-4755-90c1-187b94f12e76',
               '3828a067-5f06-456f-8177-0b47f9d3d6f7',
               '78f80e0d-624a-461d-9780-1f73ba3867db',
               '68f9f53b-3829-4a56-bd21-2d3955ec2421',
               '7e3e9647-115d-411d-8ab5-30d58c5d089d',
               '35b9eec6-8502-438c-8c2f-c27ce507d856',
               '35f59e64-4af5-45c4-bf17-dd28d42cad3d',
               '3266599d-c6d8-4354-8b53-a5f4efce730a',
               '2c2978bb-29b2-4f57-8ac0-05851ccd871d',
               '4ba89d78-d481-4d38-8f02-a3ca5141a997',
               'ad348ade-5670-4090-a051-91e594ad0936',
               '182dac31-ec17-4228-bae0-9e3a962891c9',
               'cd174ea8-0484-4a52-88a6-778278d214ad',
               'b7b91df7-469b-4a11-8651-ef49be5073a5',
               '712adbcf-978a-4e65-bef3-d2e378320918',
               '2bb2a256-e8b7-400e-9155-fdd38325fccb',
               'b4154dcc-2ac0-4d58-829d-cab7c9bcb26f',
               '50d0164c-4079-4b82-a36a-f2f0c290a5bb',
               '528e394c-ad01-4999-9d97-58bc5f7a62ce',
               'd3e91307-5835-4b1f-81ca-02dced0646da',
               '8bcb4358-bab9-45ed-8426-873fab11ce79',
               'a218a0d6-a8bf-47c2-b258-364d5458994d',
               'cd4a6196-4eed-44d7-ab8f-74f41f24a0a4',
               '86e54442-1874-429a-9478-1603c859954f',
               '46d6da03-2f9c-47fb-9269-357718cf26f0',
               '08d750c8-54ef-4a7b-9060-7758ea924ed1',
               'cee627fb-b13c-419d-843f-942c6d56dded',
               'f44099c1-3ced-498a-b6b2-7a414344ab26',
               '8df04f7d-7743-4849-a618-05b3f5879a34',
               '781e0a08-2006-4461-a4d7-2fa337056229',
               '54abf11e-8267-4208-867b-3ae344f9743b',
               '9cb4e01d-d7e1-4b18-9bb5-6ed27b4bd8e5',
               'eb097602-0b92-485a-a4a0-7b109c9ccc61',
               '90f452ab-04b9-4fe0-8fba-cc66b9b9012a'
               ]


# # alternatively, read list of session IDs from CSV column
# from pathlib import Path
# import pandas as pd
# fpath = Path('~/Documents/paru/session_ids_fshd.csv')
# df = pd.read_csv(fpath)
# sessionList = df['sid'].dropna().unique()

             
# base directory for downloads. Specify None if you want to go to os.path.join(os.getcwd(),'Data')
downloadPath = os.path.join(os.getcwd(),'Data')

for session_id in sessionList:
    # If only interested in marker and OpenSim data, downladVideos=False will be faster
    download_session(session_id,sessionBasePath=downloadPath,downloadVideos=False)