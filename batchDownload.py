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
sessionList = ["98e591cd-202c-46a3-878d-4aa020e938a6"
"5e95a016-0e65-4e6e-9976-a93659c4e380"
"4a1c0ed2-72a5-4d67-bd1b-cb52780598c3"
"fd5ac144-99a0-42d0-a7f7-d2e5d2cc085b"
"b232c640-6899-40cf-a0b5-0f3d74698f97"
"0138b4bc-f0d5-4165-a7dd-e0fb294654d1"
"1b0e74b4-f29a-42b2-a3b9-f10d67e51763"
"aec6e8d8-3398-4d12-b00d-8538fc624999"
"70059d2d-705c-4d19-9f82-582d96b2e7f4"
"ca9e16fa-efc2-43c6-8ba4-ce7f65d335fc"
"a09e1204-a175-4665-a163-833b6a9159b9"
"e9b7b5e5-9e05-437a-b200-4e1c7520d88f"
"f4899c76-b551-4455-86e9-6b82607957fc"
"d00c2881-1d9e-43f1-9ca6-0a0c92a4d43a"
"53e6ea3e-987f-4a2d-87e4-5da1e26f45a2"
"8aac7cd9-de47-4f42-9b93-67a1e9192cdc"
"b07040cd-9cbe-4d13-b1b3-a874c478e5d0"
"41c97b90-3343-4714-9583-967bb1101724"
"ead1cf45-0cc5-4669-adfe-e6d75e32f5d4"
"fe9fe5cc-b1a7-4fd3-a92d-0c8ba5468ebe"
"a812478b-9b20-444e-b0a5-af235e013aac"
"a968c8a8-17cb-4fe6-b8ce-5ebed87e735b"
"534fe3db-43e2-401f-a555-742ca9b3e4db"
"8a86a383-742b-4912-83fb-f6ee7591be7d"
"d9533973-8798-40ea-bfb0-d3d4f10d58b4"
"53170d81-d163-4239-85d8-574ff71cdd8e"
"4265d9b5-9576-49c9-b8d9-edad24d64cbf"
"ff145278-2fad-43cd-8762-4b6f07fc4a08"
"6ea2ce2a-be08-4a8f-8e90-1e382dbd1ce2"
"a7e9eb9c-73f5-4e61-8770-596ffa8593d0"
"5eaf1fc5-8a48-48c0-b0ad-39e8a81976ac"
"eb4244fd-37b7-4569-9d7a-bc67cbda0042"
"8ba199b6-4f64-4340-bec5-547b34676e47"
"24c60d93-71bd-4ad6-8712-9f72052fe7a1"]


# # alternatively, read list of session IDs from CSV column
# from pathlib import Path
# import pandas as pd
# fpath = Path('~/Documents/paru/session_ids_fshd.csv')
# df = pd.read_csv(fpath)
# sessionList = df['sid'].dropna().unique()

             
# base directory for downloads. Specify None if you want to go to os.path.join(os.getcwd(),'Data')
downloadPath = os.path.join(os.getcwd(),'UCL')

for session_id in sessionList:
    # If only interested in marker and OpenSim data, downladVideos=False will be faster
    download_session(session_id,sessionBasePath=downloadPath,downloadVideos=False)