#Project Planning
## Problem Statement
Primary User
Me (A treasury analyst who is responsible for producing the global weekly cash report)

User Needs Statement
As a Treasury analyst I currently received weekly submissions from entities that reports their bank balances as of week end.  I now need to print out the spreadsheet and manually enter each number into a spreadsheet and calculate the global total.  I need a quicker and better way so when my manager asked me our cash position I can have a quick answer.

As-is Process Description
1. Download all spreadsheet (various format) from emails and print hard copies
2. Print a checklist to make sure all submission has been received
3. For each entity spreadsheet, Need to enter the balance for each account to the corresponding cell (Which bank, which currency)
4. Need to manually check if the amounts are adding up correctly.

To-Be process Description
1. Download all spreadsheet (All as .csv) from emails in a folder
2. Run a script to check if all submission has been received and process the data once all information has received
3. Produce summaries for:
   cash by currency by division
   cash by bank by division



## information Requirement
### Information Inputs
{ENTITY NAME}-submission.csv:
Submissions from each entity that includes entity name, bank name, account number, currency and account balances
FX Rate for the week:
Currently available for download from company website
### Information Outputs
This program should allow me to produce a summary from the terminal which tells me how much USD Equivalent do I have for each entity, as well as how much $ do I have for each currency globally.

## Technology Requirements
### APIs and Web Service Requirements
Currently not needed for data extraction.  For future Optimization, might have entities submit via encrypted google sheets and directly download all submission at once.
### Python Package Requirements
No 3rd party package required; require os csv modules.
### Hardware Requirements
This app should be run at any machine as long as the file path is matching.
