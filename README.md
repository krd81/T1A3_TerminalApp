# T1A3 Terminal Application : Movie Rental App

## Installation
All files required to run the application are in the `src` folder: T1A3_TerminalApp/src/

To run the application, type the following into the command line:
`movie_rental.sh`
This runs a bash file which executes the python file

System requirements:
Requires python ver 3.10 or above

The following package may be installed (but is not mandatory): pyinput
Install using: `pip install pyinput`

## Navigation with the app
Users need to correctly enter their username and password in order for the menu to be displayed.

During testing I have used -
username: ricky19@gmail.com
password: BaQlpSGv

The menu options are self explanatory and users can navigate by entering the specific number of the menu items.

When searching for titles, free text is allowed. If no titles are found, a message advising this will be displayed. Otherwise, titles will be displayed preceeded by a listing number. This listing number should be used for selecting titles.

It is possible to select a title, view its information and from there, rent the item or return back to the search page. If the latter option is chosen, the user will be returned back to the earlier search results. However, when exiting the search menu and searching again - the previous search results will be cleared and replaced with the results of the next search.

'Your Account' shows the user's personal information and lists current and historical rentals. Items can be returned from either within the 'Your Account' screen or by selecting '3' from the main menu.

When the user has finished using the app, they can exit by selecting '4' on the main menu. This option terminates the application.


## Source Control
[GitHib Repo](https://github.com/krd81/T1A3_TerminalApp)


## Project Management
There is a separate file with screenshots showing various stages of the project plan
[Screenshots](./docs/T1A3_Project_Screenshots.pdf)

[Github links](./docs/T1A3_Project_Plan.tsv)
