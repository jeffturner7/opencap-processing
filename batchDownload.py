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
sessionList = ['b8978da5-be70-410d-8933-69bdc49606aa','44db9704-3735-41e6-84cc-b9acd953c98e','9b565b8a-11fe-4e08-b3a9-2d5c9fde15ad',
               '29263267-09c9-4c58-baf0-ed4dce7fda73','10c534de-7eaf-4074-a33b-1c417dbdb1d3','33c2d8a4-4fe8-4661-87e9-688185748882',
               '5ae16740-4c5a-4c4f-be63-36a6a58d39ec','a1309643-c6f7-45f2-8cb0-36653bd704e3','f4d393c3-2329-4df5-9eac-8dd03e4968dc',
               'fc8a169d-8b38-4582-a06e-65a282c46f43','a26a3c19-a475-4efc-9d62-a9a90f761355','27049d30-1964-448c-9290-d0e6c0d6fb6e',
               '574c2553-3ed5-452d-9a76-40a5351c6aef','98e701ca-decf-4ba6-b576-d0a61c512fa6','b6f63a2e-9802-45dd-9ea4-1c1d1f140b06',
               '3385b46b-05d4-4ac0-9487-7903b908bb34','aa7806cf-79c7-4efb-8c0a-d1dc6e2833ac','f023203b-2a9d-49ff-ba5a-4b6f4f035437',
               '68597493-1fa3-430f-aac1-e2cbb312f408','f53e54e9-b708-4fc8-9169-3c87b3cf9c6f','64324780-a58f-41e0-890d-e94497a40728',
               'd99c8c5b-ba05-42ab-b819-6a3ec1c4d769','03203041-aaea-4879-9793-0aba711dab84','26e99e31-69c2-40ac-b0d6-27dbc6a074c3',
               '6e1afd51-7ffc-494e-abcc-5ad4a5740240','88bfc8ff-7236-421c-b6ba-fe55648bcb6a','a3e7b015-deca-48a8-ab1a-425a75cc790f',
               '9e778050-c9a7-4764-b68e-27d6dfc1cf8b']


# # alternatively, read list of session IDs from CSV column
# from pathlib import Path
# import pandas as pd
# fpath = Path('~/Documents/paru/session_ids_fshd.csv')
# df = pd.read_csv(fpath)
# sessionList = df['sid'].dropna().unique()

             
# base directory for downloads. Specify None if you want to go to os.path.join(os.getcwd(),'Data')
downloadPath = os.path.join(os.getcwd(),'Stride')

for session_id in sessionList:
    # If only interested in marker and OpenSim data, downladVideos=False will be faster
    download_session(session_id,sessionBasePath=downloadPath,downloadVideos=False)