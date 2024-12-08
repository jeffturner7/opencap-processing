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
sessionList = ["020a52a1-9f81-4397-919c-2fb51d28ae13",
"7e9d7d1e-81ce-4594-84e6-442fc5600c4d",
"faf935c7-d96e-4836-b5d8-084468b54893",
"faf3ca0e-2b70-4473-aece-907361eead8b",
"0b419b78-3f37-423c-b153-542b457ad2f9",
"aff4f739-d474-42a1-ad8d-10c36b9f858a",
"c452f5e2-511e-4b1c-bfa7-cdd5287eeac4",
"888cdd7d-e667-4367-ba7f-8f07c2a7300c",
"6656c1c9-bcff-4fbc-ae02-14b03c3b9d11",
"91a5cdbf-68c8-4bb9-9882-814ac0ffc3ba",
"4683fcf3-9095-4c40-90f3-d28d51e9ea2f",
"d28f76e3-7c73-47f2-9ffa-4169eda7b332",
"e33fa035-9c8b-4804-be95-bf2add896b33",
"f6f38b0f-89d1-44e2-a5f7-775416f891e6",
"9712a362-6d58-4b4b-a263-82a7f7e5ef53",
"bba7d155-8bd0-4a38-a64f-385dc4cfd967",
"82bf2539-de48-45e5-bba7-e9fb66c33e34",
"7c8ac96c-b604-404a-9d8c-b3e20d66f744",
"a7a9080c-2fc2-4cd1-974f-c2f0753135e7",
"183c8653-143b-4265-b985-1d7e64b90697",
"8d5fd2fa-4bd2-4fbe-bdc1-8ba7d3f7db81",
"17c6ea2d-5066-4b36-a99d-82428f6b9bd2",
"f475e82d-eb8b-4b53-8a7d-dde74ccd0595",
"e4aee237-e494-4ffb-95db-a1a327c117e4",
"24be6856-eb5c-4968-8227-6316dfe70e52",
"dae00de9-319b-4d1c-b1ad-7ddf9d6ee9c9",
"c2f65835-64dd-4e73-82b5-7aa6b4bc9207",
"dd589f19-b42a-4173-aa5b-61b67606e44b",
"bf03d7b2-aab5-46ba-9a6e-ac04e1841a43",
"97c75f9b-afe1-499a-bee1-74656c5465b3",
"f1c4ed2b-b69b-460a-bcd1-eaf24e8a2952",
"0a9173cc-9ef5-4fb8-b0d1-5efb0891ea8f",
"40fcea72-4fd7-47ba-9ffb-efc6b4f60cab",
"34b4c05d-8ca3-4bd8-aaf7-f3df5988ed9b",
"63c40bee-093c-4b76-96c0-ae21a8ed100f",
"6f2699ed-e48c-4b74-8076-2f5d254bc901",
"48acff60-52b8-4e02-8641-44470168a7fe",
"e975d170-8b66-4cde-80eb-4c1645199f93",
"f40efc12-02eb-4470-96cf-9177c80c004c",
"2c9a92d5-22d3-4b41-ad17-f0b1e6464857"

]

#uncmotion
#UNCmotion=1opencapAI

# # alternatively, read list of session IDs from CSV column
# from pathlib import Path
# import pandas as pd
# fpath = Path('~/Documents/paru/session_ids_fshd.csv')
# df = pd.read_csv(fpath)
# sessionList = df['sid'].dropna().unique()

             
# base directory for downloads. Specify None if you want to go to os.path.join(os.getcwd(),'Data')
downloadPath = os.path.join(os.getcwd(),'Aim3')

for session_id in sessionList:
    # If only interested in marker and OpenSim data, downladVideos=False will be faster
    download_session(session_id,sessionBasePath=downloadPath,downloadVideos=False)