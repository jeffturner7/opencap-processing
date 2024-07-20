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
sessionList = ["ae3b4aef-9a79-4c0f-8b7b-c4f51c1a78b4",
"d7a1f78f-b2ae-4f36-9606-755f01106065",
"1d23d144-5a61-4437-bf6d-c97e8ef31bf5",
"096a206f-a7b8-4ec8-8646-8f93aea80ef3",
"e307463b-e24e-49e9-b757-4f617980577e",
"9788c25d-2665-4e19-9dd3-f480dcb9ccc7",
"4a4b4092-d059-4c46-94f1-af4bda6c9d5b",
"0170fed3-2d26-4b81-a91f-c111f949e337",
"db4a8978-3e94-4609-867a-c3f668d2ee94",
"2cd52db6-ab58-4e46-a5d4-0994b8919cd7",
"58328c28-d582-4222-b647-a3495b5fa77b",
"532e592f-4dc8-4b7f-9c2f-b1ec1bd401ef",
"8987d69f-19f0-4e88-9023-bb405070d86a",
"db5ad326-5812-4a29-81e0-ffc29fa8dbb1",
"922048e9-45d1-4a64-a707-bd444341b0de",
"a204f7d7-6bdf-4978-a63a-8e13fc7509bd",
"8d5a0f2b-f7c4-4bce-8a71-c103e2254c43",
"b086defa-69bf-44fc-b76f-8b33f58ff942",
"4ea7a4ff-4cf2-43f8-8aba-c25b2a70377c",
"0543f46e-1b94-46d2-98ca-d3836b6a8d06",
"d5eb6b38-6e68-4686-8cd2-2efa0cd42356",
"00875ec5-a122-42b1-9e25-ce3dcf1ba2d7",
"78853c59-539d-43f0-90ad-5cda0318ec28",
"2833c130-0461-40b1-931e-e380f5304550",
"c2cdde75-3d3b-4878-a603-40fdb8db391d",
"c666e950-8502-452b-a339-5eff7795e6d7",
"18d32184-c6fb-42a8-ab98-c209ab50f4d5",
"15b44950-fce7-435b-80f5-a1233d8b094f",
"a9a1d84b-3f5a-4d9c-8aeb-3cbdfde3bf7a",
"a2c6d875-3da5-4ac3-aa5c-a44802ae5643",
"a83d868e-4838-4847-8e57-db9876714bb3",
"df766d60-2602-4324-aac4-66712019e278"]


# # alternatively, read list of session IDs from CSV column
# from pathlib import Path
# import pandas as pd
# fpath = Path('~/Documents/paru/session_ids_fshd.csv')
# df = pd.read_csv(fpath)
# sessionList = df['sid'].dropna().unique()

             
# base directory for downloads. Specify None if you want to go to os.path.join(os.getcwd(),'Data')
downloadPath = os.path.join(os.getcwd(),'UCL2023')

for session_id in sessionList:
    # If only interested in marker and OpenSim data, downladVideos=False will be faster
    download_session(session_id,sessionBasePath=downloadPath,downloadVideos=False)