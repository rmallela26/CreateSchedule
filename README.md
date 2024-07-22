# Schedule Fitter

This program automates the tedious process of finding what lecture times/recitations/labs can fit on your schedule without clashing with each other, once the user knows what classes they want to take. 

Given what classes a user wants to take, the program will automatically create a plausible schedule that has all the required components for each class, and identifies when a schedule can't be fit and which class caused the clash. It does so in a randomized fashion, so that the user can keep running the program to produce different schedules. Once a schedule is created, it is easier for the user to move things around as they wish, or they can decide to fit a new schedule. 

### Customizations

The program can be customized in two ways: 
The user can identify times they don't want to have class during (before 9 AM, after 5:00 PM, during lunch 1:00-2:00, etc.) and the program will try to create a schedule that fits these constraints, and return if it cannot. 

The user can also manually pick some classes (if they want a specific section), and the program will attempt to fit the rest of the classes around this class and return if it cannot. 