
javac *.java --compiles the code

java -cp .:sqlite-jdbc-3.8.11.2.jar SQLiteGUIDemo	# Mac users, it is colon
java -cp .;sqlite-jdbc-3.8.11.2.jar SQLiteGUIDemo	# Windows users, it is semi-colon

# Windows users: you will need to check your path if there are spaces
# For example, C:\Users\Jane Doe\COMP405\Workspace\ETC
# This will not work 

# Solution - move the Demo folder to the place that doesn't have spaces.

